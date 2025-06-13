from kafka import KafkaConsumer
import json 
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.models.price import Price
from app.models.price import Price
from app.models.moving_average import MovingAverage
from statistics import mean

consumer = KafkaConsumer(
    'price-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='ma-consumer-group',
)

def fetch_last_prices(db: Session, symbol: str, limit: int = 5):
    """
    Fetch the last 'limit' prices for a given symbol from the database.
    
    :param db: Database session.
    :param symbol: The symbol to fetch prices for.
    :param limit: Number of last prices to fetch.
    :return: List of Price objects.
    """
    return (
    db.query(Price)
      .filter(Price.symbol == symbol)
      .order_by(Price.timestamp.desc())
      .limit(limit)
      .all()
)

def save_moving_average(db: Session, symbol: str, moving_average: float):
    """
    Save the calculated moving average to the database.
    
    :param db: Database session.
    :param symbol: The symbol for which the moving average is calculated.
    :param moving_average: The calculated moving average value.
    """
    ma_record = MovingAverage(symbol=symbol, moving_average=moving_average)
    db.add(ma_record)
    db.commit()

    for msg in consumer:
        data = msg.value
        symbol = data.get('symbol')
        price = data.get('price')

        db = SessionLocal()
        try:
            prices = fetch_last_prices(db, symbol)
            if len(prices) >= 5:
                avg = mean([p.price for p in prices])
                save_moving_average(db, symbol, avg)
        except Exception as e:
            print(f"Error processing message: {e}")
        finally:
            db.close()