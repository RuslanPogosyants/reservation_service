from datetime import datetime
from typing import Optional, Generic, TypeVar

from pydantic import BaseModel, ConfigDict


class TableBase(BaseModel):
    """
    Базовая схема
    """

    name: str
    seats: int
    location: Optional[str] = None


class TableCreate(TableBase):
    """
    Схема для создания столика
    """
    pass


class TableRead(TableBase):
    """
    Схема для возврата из API
    """
    id: int

    model_config = ConfigDict(from_attributes=True)