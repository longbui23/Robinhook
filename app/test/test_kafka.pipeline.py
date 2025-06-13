import pytest
from app.services.Kafka.producer import produce_price_event
from app.services.Kafka.consumer import handle_price_event

MOCK_EVENT = {
    "symbol": "AAPL",
    "price": 150.25,
    "timestamp": "2024-03-20T10:30:00Z",
    "source": "yfinance",
    "raw_response_id": "mock-id-123"
}

def test_produce_and_consume_event(monkeypatch):
    results = []

    def mock_consume(event):
        results.append(event["symbol"])

    monkeypatch.setattr("app.kafka.consumer.handle_price_event", mock_consume)
    produce_price_event(MOCK_EVENT)
    handle_price_event(MOCK_EVENT)
