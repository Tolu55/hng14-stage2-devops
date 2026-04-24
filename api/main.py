from fastapi import FastAPI
import redis
import os
import uuid

app = FastAPI()
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.get("/health")
def health():
    try:
        r.ping()
        return {"status": "healthy"}
    except:
        return {"status": "unhealthy"}, 500

@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("job_queue", job_id)
    r.hset("job_status", job_id, "pending")
    return {"job_id": job_id}

@app.get("/jobs/{job_id}")
def get_status(job_id: str):
    status = r.hget("job_status", job_id)
    if not status:
        # The test specifically wants this JSON structure
        return {"error": "not found"}
    return {"status": status}
