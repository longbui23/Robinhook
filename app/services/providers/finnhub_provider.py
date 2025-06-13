import os
import requests
from datetime import datetime

API_KEY = os.getenv("FINNHUB_API_KEY")
BASE_URL = "https://finnhub.io/api/v1"

def fetch_latest_price(symbol: str):
    resp = requests.get(f"{BASE_URL}/quote", params={"symbol": symbol, "token": API_KEY})
    data = resp.json()
    if "c" not in data:
        raise Exception("Finnhub error or invalid symbol")

    return {
        "symbol": symbol,
        "price": float(data["c"]),
        "timestamp": datetime.utcnow().isoformat(),
        "provider": "finnhub"
    }
