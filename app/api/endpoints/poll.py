from fastapi import APIRouter, Depends, status
from app.schemas.poll_request import PollRequest, PollResponse
from app.services.Polling.polling import create_poll_job

router = APIRouter()

def get_poll_service():
    return create_poll_job()

@router.post(
    "/poll",
    response_model=PollResponse,
    status_code=status.HTTP_202_ACCEPTED
)
def poll_prices(
    request: PollRequest,
    service: create_poll_job = Depends(get_poll_service)
):
    return service(request)