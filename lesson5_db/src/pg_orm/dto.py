from sqlalchemy import MetaData, String, DATETIME, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class BaseDto(DeclarativeBase):
    metadata = MetaData()


class City(BaseDto):
    
    __tablename__ = 'city'

    city_id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    city:Mapped[str] = mapped_column(String(length=50), nullable=False)
    country_id: Mapped[Integer] = mapped_column(Integer)
    last_update: Mapped[datetime] = mapped_column(DATETIME)
