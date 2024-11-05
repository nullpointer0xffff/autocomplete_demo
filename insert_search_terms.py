import redis

# Connect to the Redis instance
redis_conn = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

# Sample data: search terms and their popularity counts
sample_data = {
    "python tutorial": 150,
    "python redis example": 120,
    "python fastapi": 200,
    "fastapi tutorial": 100,
    "redis docker setup": 90,
    "fastapi redis autocomplete": 180,
    "docker tutorial": 130,
    "docker fastapi": 70,
}

# Insert each term with its popularity count
for term, count in sample_data.items():
    redis_conn.set(term, count)

print("Sample data inserted into Redis.")
