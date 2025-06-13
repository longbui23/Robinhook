import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_latest_price():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/latest?symbol=AAPL&provider=yfinance")
        assert response.status_code == 200
        assert "symbol" in response.json()
        assert response.json()["symbol"] == "AAPL"