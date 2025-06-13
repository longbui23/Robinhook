from sqlalchemy import Column, String, Float, DateTime, Index
from datetime import datetime
from app.core.db import Base

class Price(Base):
    __tablename__ = "market_prices"

    symbol = Column(String, primary=True)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        Index("idx_symbol", "symbol"),
        Index("idx_timestamp", "timestamp"),
    )