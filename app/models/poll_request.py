from sqlalchemy import Column, String, Integer
from app.core.db import Base

class PollJob(Base):
    __tablename__ = "poll_jobs"

    job_id = Column(String, primary_key=True, index=True)
    status = Column(String, nullable=False)
    symbols = Column(String, nullable=False)
    interval = Column(Integer, nullable=False)
    provider = Column(String, nullable=True)