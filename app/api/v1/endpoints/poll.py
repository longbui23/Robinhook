from fastapi import APIRouter, Depends, status, Query, HTTPException
from app.services.Polling.polling import POLL_JOBS
from app.schemas.poll_request import PollRequest, PollResponse
from app.services.Polling.polling import PollService

router = APIRouter()

def get_poll_service():
    return PollService()

# Endpoint to poll prices for a given symbol and provider
@router.post(
    "/poll",
    response_model=PollResponse,
    status_code=status.HTTP_202_ACCEPTED
)

def poll_prices(request: PollRequest):
    service = get_poll_service()
    return service.create_poll_job(request)

# Endpoint to get the status of a poll job
@router.get(
    "/poll",
    response_model=PollResponse,
    status_code=status.HTTP_202_ACCEPTED
)
def get_poll(job_id: str=Query(..., description="The ID of the poll job")):
    service = get_poll_service()
    return service.get_poll_job_status(job_id)

# Endpoint to cancel a poll job
@router.delete(
    "/poll",
    response_model=PollResponse,
    status_code=status.HTTP_202_ACCEPTED
)

def delete_poll(
   job_id: str=Query(..., description="The ID of the poll job")
):
    if job_id in POLL_JOBS:
        del POLL_JOBS[job_id]
        return PollResponse(message="Poll job cancelled successfully", job_id=job_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Poll job with ID {job_id} not found"
    )