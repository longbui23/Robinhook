from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://posgres:posgres@localhost/market_data"
    KAFKA_BORKER_URL: str = "kafka:9092"
    KAFKA_TOPIC: str = "price_events"

    class Config:
        env_file = ".env"

Settings = Settings()
