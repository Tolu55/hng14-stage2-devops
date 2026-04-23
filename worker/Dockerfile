FROM python:3.11-slim
WORKDIR /app
RUN useradd -m appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
USER appuser
COPY . .
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD pgrep python || exit 1
CMD ["python", "worker.py"]
