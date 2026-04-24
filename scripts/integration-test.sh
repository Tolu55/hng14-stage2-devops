#!/bin/bash
set -e
echo "Testing connectivity..."
# Hits the new endpoint
RESPONSE=$(curl -s -X POST http://localhost:3000/jobs)
JOB_ID=$(echo $RESPONSE | jq -r '.job_id // empty')
if [ -z "$JOB_ID" ] || [ "$JOB_ID" == "null" ]; then
  echo "Failed: $RESPONSE"
  exit 1
fi
echo "Success: Job $JOB_ID created."
