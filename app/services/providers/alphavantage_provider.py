import os
import requests
from datetime import datetime

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

def fetch_latest_price(symbol: str):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY,
    }
    resp = requests.get(BASE_URL, params=params)
    data = resp.json()
    if "Global Quote" not in data:
        raise Exception("Alpha Vantage error or invalid symbol")
    
    quote = data["Global Quote"]
    return {
        "symbol": symbol,
        "price": float(quote["05. price"]),
        "timestamp": datetime.utcnow().isoformat(),
        "provider": "alphavantage"
    }
