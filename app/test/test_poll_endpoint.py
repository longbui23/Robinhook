import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test for the /prices/poll endpoint
@pytest.mark.asyncio
async def test_post_poll_prices():
    payload = {
        "symbols": ["AAPL", "MSFT"],
        "interval": 60,
        "provider": "alpha_vantage"
    }
    response = client.post("/prices/poll", json=payload)
    assert response.status_code == 202
    data = response.json()
    assert "job_id" in data
    assert data["status"] == "accepted"
    assert "config" in data
    assert data["config"]["symbols"] == ["AAPL", "MSFT"]
    assert data["config"]["interval"] == 60
    assert data["config"]["provider"] == "alpha_vantage"

# Error handling: missing symbols
@pytest.mark.asyncio
async def test_post_poll_prices_missing_symbols():
    payload = {
        "interval": 60,
        "provider": "alpha_vantage"
    }

    response = client.post("/prices/poll", json=payload)
    assert response.status_code == 422  # Unprocessable Entity

# Error handling: invalid interval
@pytest.mark.asyncio
async def test_post_poll_prices_invalid_interval():
    payload = {
        "symbols": ["AAPL", "MSFT"],
        "interval": "sixty",  # invalid type
        "provider": "alpha_vantage"
    }

    response = client.post("/prices/poll", json=payload)
    assert response.status_code == 422  # Unprocessable Entity