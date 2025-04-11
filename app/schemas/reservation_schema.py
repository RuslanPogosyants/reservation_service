from datetime import datetime
from typing import TypeVar, Generic

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ReservationBase(BaseModel, Generic[T]):
    """
    Базовая схема
    """
    customer_name: str = Field(None, description="Имя клиента")
    table_id: int = Field(None, description="ID стола")
    reservation_time: datetime = Field(None, description="Дата и время бронирования")
    duration_minutes: int = Field(None, description="Длительность брони")


class ReservationCreate(ReservationBase):
    """
    Схема для создания брони
    """
    pass


class ReservationRead(ReservationBase):
    """
    Схема для вывода в ответах API
    """
    id: int

    model_config = ConfigDict(from_attributes=True)
