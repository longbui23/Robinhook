from fastapi import APIRouter, Query, HTTPException, status, Depends, status

from app.schemas.price import PriceResponse
from app.services.providers import get_price_by_provider

from app.schemas.poll_request import PollRequest, PollResponse
from app.services.Polling.polling import PollingService


router = APIRouter()

# API endpoint to get the latest market price for a given symbol
@router.get("/latest", response_model=PriceResponse)
def get_latest_price(symbol: str = Query(...), provider: str = Query("yfinance")):
    """
    Fetch the latest market price for a given symbol.
    """
    if not symbol or not provider:
        raise HTTPException(status_code=400, detail="Symbol and provider query parameters are required")

    try:
        price_data = get_price_by_provider(symbol, provider)
        response = PriceResponse(**price_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
def get_poll_service():
    return PollingService()

# API endpoint to create a polling job for market prices
@router.post("/poll", response_model=PollResponse, status_code=status.HTTP_202_ACCEPTED)
def poll_prices(
    request: PollRequest,
    service: PollingService = Depends(get_poll_service)
):
    response = service.create_polling_job(request)

    return response