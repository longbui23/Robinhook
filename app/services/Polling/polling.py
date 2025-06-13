import asyncio
from app.services.providers.yfinance_provider import get_latest_price
from app.services.Kafka.producer import send_price_event
from app.core.db import SessionLocal
from app.models.price import Price

async def start_polling(symbols, interval, provider):
    while True:
        db = SessionLocal()
        try:
            for symbol in symbols:
                price_data = get_latest_price(symbol, provider)

                # Store to DB
                db_price = Price(
                    symbol=symbol,
                    price=price_data["price"],
                    timestamp=price_data["timestamp"],
                    provider=provider
                )
                db.merge(db_price)
                db.commit()

                # Produce to Kafka
                send_price_event(price_data)

        except Exception as e:
            print(f"[Polling Error] {e}")
        finally:
            db.close()

        await asyncio.sleep(interval)
