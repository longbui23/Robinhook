from kafka import KafkaProducer
import json
import os
import time

# app/services/Kafka/producer.py
producer = KafkaProducer(
    bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    client_id='fastapi-service',
    retries=3
)


def delivery_report(err, msg):
    """
    Callback function to handle delivery reports from Kafka.
    
    :param err: Error if any occurred during message delivery.
    :param msg: The message that was attempted to be sent.
    """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered successfully: {msg.topic} [{msg.partition}] @ {msg.offset}")


def send_price_event(price_data: dict, max_retries: int = 3, topic='price_events'):
    """
    Sends a price event to the Kafka topic.
    
    :param price_data: Dictionary containing price data.
    """
    payload = json.dumps(price_data)

    for attempt in range(max_retries):
        try:
            producer.send(topic, value=payload)
            producer.flush()
            print(f"Price event sent: {price_data}")
        except BufferError as e:
            print(f"BufferError: {e}. Retrying...")
            time.sleep(1)
        except Exception as e:
            print(f"Failed to send price event: {e}")
    print("[Kafka] Failed to produce message after retries")