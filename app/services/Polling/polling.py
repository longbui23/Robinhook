import uuid
from app.schemas.poll_request import PollRequest, PollResponse

class PollService:
    def create_poll_job(self, config: PollRequest) -> PollResponse:
        job_id = f"poll_{uuid.uuid4().hex[:8]}"
        # Enqueue the job
        return PollResponse(
            job_id=job_id,
            status="accepted",
            config=config
        )