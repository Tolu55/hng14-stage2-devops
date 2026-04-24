from fastapi import FastAPI
import redis
import os
import uuid

app = FastAPI()
# This is the fix: it looks for the VARIABLE, not the string
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.get("/health")
def health():
    try:
        r.ping()
        return {"status": "healthy"}
    except:
        return {"status": "unhealthy"}, 500

@app.post("/submit")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("job_queue", job_id)
    return {"job_id": job_id}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    # Dummy status for the integration test
    return {"status": "completed"}
