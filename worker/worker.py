import redis
import time
import os
import signal
import sys

r = redis.Redis(host="redis", port=6379)
running = True

def handle_signal(signum, frame):
    global running
    print(f"Received signal {signum}, shutting down gracefully...")
    running = False

# Listen for termination signals from Docker
signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id.decode()}", "status", "completed")
    print(f"Done: {job_id.decode()}")

print("Worker started. Waiting for jobs...")
while running:
    # Use a short timeout so the loop can check the 'running' flag frequently
    job = r.brpop("job", timeout=2)
    if job:
        _, job_id = job
        process_job(job_id)

print("Worker shut down cleanly.")
sys.exit(0)
