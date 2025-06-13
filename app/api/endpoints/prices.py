from fastapi import APIRouter, Query, HTTPException
from app.schemas.price import PriceResponse
from app.services.providers import get_price_by_provider

router = APIRouter()

@router.get("/latest", response_model=PriceResponse)
def get_latest_price(symbol: str = Query(...), provider: str = Query("yfinance")):
    """
    Fetch the latest market price for a given symbol.
    """
    if not symbol:
        raise HTTPException(status_code=400, detail="Symbol query parameter is required")

    if provider.lower() != "yfinance":
        raise HTTPException(status_code=400, detail="Unsupported provider. Only 'yfinance' is supported.")

    try:
        price_data = get_price_by_provider(symbol, provider)
        return price_data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))