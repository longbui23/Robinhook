import os
from dotenv import load_dotenv

load_dotenv(".env")

class Settings:
    DATABASE_URL: str = "postgresql://posgres:root@localhost/market_data"
    KAFKA_BROKER_URL: str = "kafka:9092"
    KAFKA_TOPIC: str = "price_events"
    REDIS_URL: str = "redis://localhost:6379/0"

Settings = Settings()
