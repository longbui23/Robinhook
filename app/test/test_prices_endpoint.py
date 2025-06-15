import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#API endpoint test price stock
@pytest.mark.asyncio
async def test_get_latest_price():
    response = client.get("/prices/latest?symbol=AAPL&provider=yfinance")
    assert response.status_code == 200
    assert "symbol" in response.json()
    assert response.json()["symbol"] == "AAPL"


# Error handling test for invalid symbol
@pytest.mark.asyncio
async def test_get_latest_price_invalid_symbol():
    response = client.get("/prices/latest?symbol=INVALID")
    assert response.status_code == 404
    assert response.json()["detail"] == "No data found for symbol: INVALID"


# Error handling test for missing symbol or/and provider
@pytest.mark.asyncio
async def test_get_latest_price_missing_symbol():
    response = client.get("/prices/latest")
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert any(
        err.get("loc") == ["query", "symbol"] and err.get("msg") == "Field required"
        for err in detail
    )


# Error handling test for unsupported provider
@pytest.mark.asyncio
async def test_get_latest_price_unsupported_provider():
    response = client.get("/prices/latest?symbol=AAPL&provider=unsupported")
    assert response.status_code == 404
    assert response.json()["detail"] == "Unsupported provider: unsupported"