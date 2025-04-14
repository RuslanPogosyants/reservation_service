from datetime import datetime
from typing import TypeVar, Generic, Optional

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ReservationBase(BaseModel, Generic[T]):
    """
    Базовая схема
    """

    customer_name: Optional[str] = Field(None, description="Имя клиента")
    table_id: Optional[int] = Field(None, description="ID стола")
    reservation_time: Optional[datetime] = Field(
        None, description="Дата и время бронирования"
    )
    duration_minutes: Optional[int] = Field(None, description="Длительность брони")


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
