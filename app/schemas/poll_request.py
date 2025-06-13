from pydantic import BaseModel, Field
from typing import List

class PollRequest(BaseModel):
    symbols: List[str]
    interval: int = Field(gt=0, description="Polling interval in seconds")
    provider: str = "yfinance"

class PollResponse(BaseModel):
    job_id: str
    status: str
    config: PollRequest
