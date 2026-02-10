from flask import Flask
import redis
import os
import time

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def connect_redis():
    for _ in range(10):
        try:
            r = redis.Redis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                decode_responses=True
            )
            r.ping()
            return r
        except Exception:
            time.sleep(1)
    return None

redis_client = connect_redis()

@app.route("/")
def home():
    if redis_client is None:
        return "Redis not available, but app is running", 200

    count = redis_client.incr("hits")
    return f"Hello! This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
