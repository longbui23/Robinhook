from app.core.cache import get_cache, set_cache
from app.core.db import SessionLocal
from app.models.price import Price
from app.services.Kafka.producer import publish_price_update

from app.services.providers.yfinance_provider import fetch_latest_price as yf_price
from app.services.providers.alphavantage_provider import fetch_latest_price as av_price
from app.services.providers.finnhub_provider import fetch_latest_price as fh_price

from datetime import timedelta

def get_price_by_provider(symbol: str, provider: str):

    # find caches
    cache_key = f"price:{provider.lower()}:{symbol.upper()}"
    cached = get_cache(cache_key)
    if cached:
        cached["provider"] += " (cached)"
        return cached

    # if no cache, fetch from provider
    provider = provider.lower()    
    if provider == "yfinance":
        price = yf_price(symbol)
    elif provider == "alphavantage":
        price = av_price(symbol)
    elif provider == "finnhub":
        price = fh_price(symbol)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

    # set cache
    set_cache(cache_key, price, ttl=timedelta(seconds=60))

    #store in postgres
    db = SessionLocal()
    try:
        db_price = Price(
            symbol = price["symbol"],
            price = price["price"],
            provider = price["provider"],
            timestamp = price["timestamp"]
        )
        db.merge(db_price)
        db.commit()
    except Exception as e:
        print(f"Error storing price in database: {e}")
    finally:
        db.close()

    # push price to kafka
    publish_price_update(price)

    return price
