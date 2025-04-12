from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.schemas.reservation_schema import ReservationCreate, ReservationRead
from app.services.reservation_service import delete_reservation, create_reservation, get_all_reservations

router = APIRouter(prefix="/reservations", tags=["Reservations"])


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


@router.get("/", response_model=List[ReservationRead])
async def list_resrvations(session: AsyncSession = Depends(get_session)):
    return await get_all_reservations(session)


@router.post("/", response_model=ReservationRead)
async def add_reservation(reservation: ReservationCreate, session: AsyncSession = Depends(get_session)):
    created = await create_reservation(session, reservation)
    if not created:
        raise HTTPException(status_code=400, detail="Стол уже забронирован на это время")
    return created


@router.delete("/{reservation_id}")
async def remove_reservation(reservation_id: int, session: AsyncSession = Depends(get_session)):
    deleted = await delete_reservation(session, reservation_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Бронь не найдена")
    return {"message": f"Бронь {reservation_id} удалена"}
