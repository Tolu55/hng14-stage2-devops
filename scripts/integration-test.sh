#!/bin/bash
set -e
echo "Starting HNG Integration Test..."
# Verify connection to the API through the frontend proxy/port
curl -f http://localhost:3000/jobs
