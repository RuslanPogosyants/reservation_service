from datetime import timedelta

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import Reservation
from app.schemas.reservation_schema import ReservationCreate


async def get_all_reservations(session: AsyncSession):
    result = await session.execute(select(Reservation))
    return result.scalars().all()


async def create_reservation(session: AsyncSession, reservation_in: ReservationCreate):
    time_start = reservation_in.reservation_time
    time_end = time_start + timedelta(minutes=reservation_in.duration_minutes)

    result = await session.execute(
        select(Reservation).where(
            and_(
                Reservation.table_id == reservation_in.table_id,
                Reservation.reservation_time < time_end,
                (Reservation.reservation_time + timedelta(minutes=Reservation.duration_minutes)) > time_start
            )
        )
    )
    is_conflict = result.scalars().first()

    if is_conflict:
        return None

    reservation = Reservation(**reservation_in.model_dump())
    session.add(reservation)
    await session.commit()
    await session.refresh(reservation)
    return reservation


async def delete_reservation(session: AsyncSession, reservation_id: int):
    result = await session.execute(select(Reservation).where(Reservation.id == reservation_id))
    reservation = result.scalar_one_or_none()
    if reservation is None:
        return False
    await session.delete(reservation)
    await session.commit()
    return True
