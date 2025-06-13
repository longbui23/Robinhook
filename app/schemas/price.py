from pydantic import BaseModel
from datetime import datetime

class PriceResponse(BaseModel):
    '''Ensure data integrity'''

    symbol: str
    price: float 
    timestamp: datetime
    provider: str