# 📈 ROBINHOOK: REAL-TIME STOCK DATA

A **production-ready FastAPI microservice** that:

- Fetches real-time market data
- Processes it via a Kafka streaming pipeline
- Serves it through RESTful APIs
- Includes proper documentation, testing, DevOps tooling

---

## ✅ Tasks Breakdown

### 🧩 Core API
- FastAPI project structure
- Dependency injection
- `/prices/latest` endpoint

### 🧩 Database & Market Data Integration 
- PostgreSQL with SQLAlchemy
- Provider abstraction: Alpha Vantage / YFinance / Finnhub
- Store raw & processed data

### 🧩 Kafka Pipeline & Docs 
- Produce events to `price-events`
- Consumer: compute 5-point moving average
- Store into `symbol_averages` table
- Documentation (README, diagrams)

### 🧪 Testing Suite 
- Unit tests with `pytest`
- Integration tests for E2E flow

### 🐳 Docker & CI/CD 
- Dockerfile + `docker-compose`
- GitHub Actions CI
- Optional deployment to Heroku/AWS
---