from confluent_kafka import Consumer
import json
from sqlalchemy import desc
from app.core.db import SessionLocal
from app.models.price import Price
from app.models.moving_average import MovingAverage

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'ma-consumer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(['price-events'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    try:
        data = json.loads(msg.value().decode('utf-8'))
        symbol = data['symbol']
        price = data['price']
        timestamp = data.get('timestamp')

        db = SessionLocal()
        try:
            previous_prices = (
                db.query(Price)
                .filter(Price.symbol == symbol)
                .order_by(desc(Price.timestamp))
                .limit(4)
                .all()
            )
            prices = [price] + [p.price for p in previous_prices]
            prices = prices[:5]
            avg = sum(prices) / len(prices)

            print(f"Symbol: {symbol}, 5-point MA: {avg}")

            db_avg = MovingAverage(symbol=symbol, average=avg)
            db.merge(db_avg)
            db.commit()
        except Exception as e:
            print(f"Error processing moving average: {e}")
        finally:
            db.close()
    except Exception as e:
        print(f"Error decoding message: {e}")