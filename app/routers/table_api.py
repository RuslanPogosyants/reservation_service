from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.schemas.table_schema import TableCreate, TableRead
from app.services.table_service import get_all_tables, create_table, delete_table

router = APIRouter(prefix="/tables", tags=["Tables"])


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


@router.get("/", response_model=List[TableRead])
async def list_tables(session: AsyncSession = Depends(get_session)):
    return await get_all_tables(session)


@router.post("/", response_model=TableRead)
async def add_table(table: TableCreate, session: AsyncSession = Depends(get_session)):
    return await create_table(session, table)


@router.delete("/{table_id}")
async def remove_table(table_id: int, session: AsyncSession = Depends(get_session)):
    deleted = await delete_table(session, table_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Стол не найден")
    return {"message": f"Стол {table_id} удален"}
