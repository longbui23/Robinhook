from fastapi import FastAPI
from app.api.endpoints import prices, poll

app = FastAPI(title="Market Data Service")

app.include_router(prices.router, prefix="/prices", tags=["prices"])
app.include_router(poll.router, prefix="/prices", tags= ["polling"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)