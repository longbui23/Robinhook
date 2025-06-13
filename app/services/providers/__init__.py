from app.core.cache import get_cache, set_cache
from app.services.providers.yfinance_provider import fetch_latest_price as yf_price
from app.services.providers.alphavantage_provider import fetch_latest_price as av_price
from app.services.providers.finnhub_provider import fetch_latest_price as fh_price

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
    set_cache(cache_key, price, ttl=60)
    return price