# 📚 RobinHook API Documentation

This document describes the REST API for RobinHook, including endpoints, request/response examples, error codes, and rate limits.

---

## 🔗 OpenAPI/Swagger

- **Interactive Swagger UI:**  
  [http://localhost:8000/docs](http://localhost:8000/docs)
- **OpenAPI JSON:**  
  [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🛣️ Endpoints

### 1. Get Latest Price

**GET** `/prices/latest`

**Query Parameters:**
- `symbol` (string, required): Stock symbol (e.g., `AAPL`)
- `provider` (string, optional, default: `yfinance`): Data provider (`yfinance`, `alpha_vantage`, `finnhub`)

**Example Request:**
```http
GET /prices/latest?symbol=AAPL&provider=yfinance
   ```

**Example Response:**
```
{
  "symbol": "AAPL",
  "price": 150.25,
  "provider": "yfinance",
  "timestamp": "2024-06-15T10:30:00Z"
}
```

**Error Responses:**

*404 Not Found:* No data found for symbol
*422 Unprocessable Entity:* Missing required query parameter


### 2. Poll Prices (Background Job)

**POST** `/prices/poll`

**Request Body:**
```json
{
  "symbols": ["AAPL", "MSFT"],
  "interval": 60,
  "provider": "alpha_vantage"
}
```
- `symbols` (array of string, required): List of stock symbols
- `interval` (integer, required): Polling interval in seconds
- `provider` (string, required): Data provider

**Example Response (202 Accepted):**
```json
{
  "job_id": "poll_123",
  "status": "accepted",
  "config": {
    "symbols": ["AAPL", "MSFT"],
    "interval": 60,
    "provider": "alpha_vantage"
  }
}
```

**Error Responses:**

*422 Unprocessable Entity:* Invalid or missing fields  
*400 Bad Request:* Unsupported provider