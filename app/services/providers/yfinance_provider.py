import yfinance as yf
from datetime import datetime, timezone

def fetch_latest_price(symbol: str):
    """
    Fetch the latest market price for a given symbol using yfinance.
    """
    
    ticker = yf.Ticker(symbol)
    data =  ticker.history(period="1d", interval="1m")

    if data.empty:
        raise ValueError(f"No data found for symbol: {symbol}")
    
    latest = data.tail(1).iloc[0]

    return {
        "symbol": symbol,
        "price": float(latest["Close"]),
        "timestamp": latest.name.to_pydatetime().replace(tzinfo=timezone.utc),
        "provider": "yfinance"
    }