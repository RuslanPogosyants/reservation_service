from typing import Optional, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class TableBase(BaseModel, Generic[T]):
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
