import uuid
from app.schemas.poll_request import PollRequest, PollResponse
from app.core.db import SessionLocal
from app.models.poll_request import PollJob

POLL_JOBS = {}

class PollService:
    def create_poll_job(self, config: PollRequest) -> PollResponse:
        job_id = f"poll_{uuid.uuid4().hex[:8]}"
        db = SessionLocal()
        try:
            db_job = PollJob(
                job_id=job_id,
                symbols=",".join(config.symbols),
                interval=config.interval,
                provider=config.provider,
                status="accepted"
            )
            db.add(db_job)
            db.commit()
        finally:
            db.close()
        return PollResponse(
            job_id=job_id,
            status="accepted",
            config=config
        )
    
    def get_poll_job_status(self, job_id: str) -> PollResponse:
        db = SessionLocal()
        try:
            db_job = db.query(PollJob).filter_by(job_id=job_id).first()
            if not db_job:
                return PollResponse(
                    job_id=job_id,
                    status="not_found",
                    config=None
                )
            config = PollRequest(
                symbols=db_job.symbols.split(","),
                interval=db_job.interval,
                provider=db_job.provider
            )
            return PollResponse(
                job_id=db_job.job_id,
                status=db_job.status,
                config=config
            )
        finally:
            db.close()