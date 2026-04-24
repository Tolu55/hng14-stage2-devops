#!/bin/bash
set -e
echo "Starting Integration Test..."
RESPONSE=$(curl -s -X POST http://localhost:3000/submit)
JOB_ID=$(echo $RESPONSE | jq -r '.job_id // empty')
if [ -z "$JOB_ID" ] || [ "$JOB_ID" == "null" ]; then
  echo "Failed: $RESPONSE"
  exit 1
fi
echo "Success: Job $JOB_ID created."
