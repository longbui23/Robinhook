import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.api.v1.endpoints import prices

from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(title="Market Data Service")

# Include the prices router
app.include_router(prices.router, prefix="/prices", tags=["prices"])

# Add Prometheus metrics endpoint
Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)