#!/bin/bash
set -e
echo "Starting Integration Test..."
# Submit job
JOB_ID=$(curl -s -X POST http://localhost:3000/submit | jq -r '.job_id')
echo "Job Created: $JOB_ID"
# Poll
for i in {1..10}; do
  STATUS=$(curl -s http://localhost:3000/status/$JOB_ID | jq -r '.status')
  if [ "$STATUS" == "completed" ]; then
    echo "Success: Job Completed!"
    exit 0
  fi
  sleep 2
done
echo "Fail: Job timed out"
exit 1
