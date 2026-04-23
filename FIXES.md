# HNG Stage 2 Bug Fixes

- File: `api/main.py`
- Problem: Redis host was set to 'localhost', which prevents communication between containers.
- Fix: Updated host to 'redis' to utilize Docker's internal DNS/service naming.

- File: `worker/worker.py`
- Problem: Redis host was set to 'localhost'.
- Fix: Updated host to 'redis' so the worker can reach the shared queue container.
