#!/bin/bash
set -e
echo "Testing connectivity..."
curl -v http://localhost:3000/submit
