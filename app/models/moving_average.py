from sqlalchemy import Column, String, Float, DateTime
from app.core.db import Base

class MovingAverage(Base):
    __tablename__ = "moving_averages"

    symbol = Column(String, primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    moving_average = Column(Float)