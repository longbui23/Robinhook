import redis
import json
import os 

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB =int(os.getenv("REIDS_DB", 0))

redis_client = redis.StrictRedis(
    host = REDIS_HOST,
    port = REDIS_PORT,
    db = REDIS_DB,
    decode_responses = True
)


def get_cache(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key: str, value: dict, ttl: int = 60):
    redis_client.set(key, json.dumps(value), ex=ttl)