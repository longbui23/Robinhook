import uuid
from app.schemas.poll_request import PollRequest, PollResponse

class PollingService:
    def __init__(self):
        # Optionally pass a database, scheduler, or logger
        pass

    def create_polling_job(self, request: PollRequest):
        # Schedule a job or enqueue a task
        job_id = f"poll_{uuid.uuid4().hex[:6]}"
        
        return {
            "job_id": job_id,
            "status": "accepted",
            "config": {
                "symbols": request.symbols,
                "interval": request.interval,
                "provider": request.provider
            }
        }