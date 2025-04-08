from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Table(Base):
    """
    Модель стола
    """

    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    seats: Mapped[int] = mapped_column(Integer, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=True)


class Reservation(Base):
    """
    Модель брони
    """

    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_name: Mapped[str] = mapped_column(String, nullable=False)
    table_id: Mapped[int] = mapped_column(Integer, ForeignKey("tables.id"))
    table: Mapped["Table"] = relationship("Table")
    reservation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    durations_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
