import pytest
from app.core.cache import set_cache, get_cache
from app.models.price import Price
from app.core.db import SessionLocal


def test_store_and_retrieve_price():
    db = SessionLocal()
    try:
        price = Price(symbol="AAPL", price=123.45, provider="test", timestamp="2024-01-01T00:00:00")
        db.add(price)
        db.commit()
        result = db.query(Price).filter_by(symbol="AAPL").first()
        assert result.price == 123.45
    finally:
        db.rollback()
        db.close()