from sqlalchemy import Column, String, Float, DateTime, Index
from datetime import datetime
from app.core.db import Base

class Price(Base):
    __tablename__ = "market_prices"

    symbol = Column(String, primary_key=True)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    provider = Column(String, nullable=False)