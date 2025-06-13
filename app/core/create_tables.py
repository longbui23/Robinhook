from app.core.db import engine, Base
from app.models.price import Price

Base.metadata.create_all(bind=engine)