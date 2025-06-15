# 📈 ROBINHOOK: REAL-TIME STOCK DATA

## 🚀 Overview

- Fetches real-time market data from multiple providers
- Processes data via a Kafka streaming pipeline
- Computes moving averages and stores results in PostgreSQL
- Exposes RESTful APIs for data access
- Includes robust documentation, testing, and DevOps tooling

---

## ⚙️ Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/robinhook.git
   cd robinhook
   ```

2. **Environment variables**
   - Copy `.env.example` to `.env` and adjust as needed (DB, Redis, Kafka, provider keys).

3. **Start services with Docker Compose**
   ```sh
   docker-compose up --build
   ```

4. **Run tests**
   ```sh
   pip install -r requirements.txt
   pytest
   ```

## 🛠️ Local Development

- Use the provided `docker-compose.yaml` for all dependencies
- Hot-reload enabled with `uvicorn` in development
- Set `PYTHONPATH` to project root for local testing:
  - Windows: `set PYTHONPATH=%cd%`
  - Unix/Mac: `export PYTHONPATH=$(pwd)`
- Run tests with `pytest`

## 🏗️ Architecture Decisions

- **FastAPI** for async, type-safe APIs
- **PostgreSQL** for transactional storage
- **Kafka** for event streaming and decoupled processing
- **Redis** for caching
- **Prometheus & Grafana** for monitoring
- **Docker Compose** for local orchestration
- **GitHub Actions** for CI/CD

---

## System Architecture
![image](https://github.com/user-attachments/assets/9667daf3-d702-4141-80e1-6d1e981a700d)
![image](https://github.com/user-attachments/assets/e52f163d-c92a-4eeb-a89f-f9935fb0257a)

---

## 📚 API Documentation

- See [APIdoc.md](APIdoc.md) for full API documentation and usage examples.

---

## ☁️ Cloud Deployment

- For AWS deployment and cloud infrastructure configuration, see [Terraform/Readme.md](Terraform/Readme.md).
