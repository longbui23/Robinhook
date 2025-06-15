import pytest
from app.core.cache import set_cache, get_cache
from app.models.price import Price
from app.core.db import SessionLocal

# postgres test
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

# cache test
def test_cache_operations():
    cache_key = "test_key"
    cache_value = {"symbol": "AAPL", "price": 123.45, "provider": "test", "timestamp": "2024-01-01T00:00:00"}
    
    # Set cache
    set_cache(cache_key, cache_value)
    
    # Get cache
    cached_value = get_cache(cache_key)
    
    assert cached_value == cache_value
    
    # Clean up
    set_cache(cache_key, None)  # Clear the cache after test