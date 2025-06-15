import pytest
from httpx import AsyncClient
from app.main import app

#API endpoint test price stock
@pytest.mark.asyncio
async def test_get_latest_price():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/latest?symbol=AAPL&provider=yfinance")
        assert response.status_code == 200
        assert "symbol" in response.json()
        assert response.json()["symbol"] == "AAPL"


# Error handling test for invalid symbol
@pytest.mark.asyncio
async def test_get_latest_price_invalid_symbol():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/latest?symbol=INVALID")
        assert response.status_code == 404


# Error handling test for missing symbol
@pytest.mark.asyncio
async def test_get_latest_price_missing_symbol():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/latest")
        assert response.status_code == 400
        assert response.json()["detail"] == "Symbol query parameter is required"


# Error handling test for unsupported provider
@pytest.mark.asyncio
async def test_get_latest_price_unsupported_provider():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/latest?symbol=AAPL&provider=unsupported")
        assert response.status_code == 400
        assert response.json()["detail"] == "Unsupported provider"


# Test for poll
@pytest.mark.asyncio
async def test_poll_prices():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/poll?symbol=AAPL&provider=yfinance")
        assert response.status_code == 200
        assert "symbol" in response.json()
        assert response.json()["symbol"] == "AAPL"
        assert "price" in response.json()
        assert isinstance(response.json()["price"], (int, float))


# Error handling test for poll with invalid symbol
@pytest.mark.asyncio
async def test_poll_prices_invalid_symbol():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/poll?symbol=INVALID")
        assert response.status_code == 404


# Error handling test for poll with missing symbol
@pytest.mark.asyncio
async def test_poll_prices_missing_symbol():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/prices/poll")
        assert response.status_code == 400
        assert response.json()["detail"] == "Symbol query parameter is required"