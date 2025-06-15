from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings

engine = create_engine(
    Settings.DATABASE_URL, 
    pool_pre_ping=True,
    pool_size=10,            # Number of connections to keep in the pool
    max_overflow=20,         # Number of connections allowed above pool_size
    pool_timeout=30,         # Seconds to wait before giving up on getting a connection
    pool_recycle=1800,       # Recycle connections after 30 minutes
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()