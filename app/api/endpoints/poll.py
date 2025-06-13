import uuid
from fastapi import APIRouter, BackgroundTasks
from app.schemas.poll_request import PollRequest
from app.services.polling import start_polling

router = APIRouter()

@router.post("/poll")
def poll_prices(request: PollRequest, background_tasks: BackgroundTasks):
    """
    Start the background task to poll prices.
    
    :param request: PollRequest object containing the symbol and interval.
    :param background_tasks: FastAPI BackgroundTasks to run the polling in the background.
    """

    job_id = f'poll_{uuid.uuid4().hex[:8]}'
    background_tasks.add_task(
        start_polling, request.symbol, request.interval, job_id
    )

    return {
        "job_id": job_id,
        "status": "accepted",
        "config": {
            "symbol": request.symbol,
            "interval": request.interval
        }
    }