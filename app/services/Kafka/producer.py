from confluent_kafka import Producer
import json
import time
import os

producer_conf = {
    'bootstrap.servers': os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
}
producer = Producer(producer_conf)

def publish_price_update(data, retries=3):
    """
    Publish price update to Kafka topic with retry logic.
    """
    payload = json.dumps(data).encode('utf-8')
    for attempt in range(1, retries + 1):
        try:
            producer.produce('price-events', value=payload)
            producer.flush()
            return
        except Exception as e:
            print(f"Kafka publish attempt {attempt} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
    print("Failed to publish message to Kafka after retries.")