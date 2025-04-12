from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import Table
from app.schemas.table_schema import TableCreate


async def get_all_tables(session: AsyncSession):
    result = await session.execute(select(Table))
    return result.scalars().all()


async def create_table(session: AsyncSession, table_in: TableCreate):
    table = Table(**table_in.model_dump())
    session.add(table)
    await session.commit()
    await session.refresh(table)
    return table


async def delete_table(session: AsyncSession, table_id: int):
    result = await session.execute(select(Table).where(Table.id == table_id))
    table = result.scalar_one_or_none()
    if table is None:
        return False
    await session.delete(table)
    await session.commit()
    return True

