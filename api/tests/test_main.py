import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from main import app, r

client = TestClient(app)

# Mock Redis for testing
@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    mock = MagicMock()
    # Mock the return value for getting a job status
    mock.hget.return_value = b"completed"
    # Mock lpush and hset for creating jobs
    mock.lpush.return_value = 1
    mock.hset.return_value = 1
    # Inject the mock into the main module's 'r' variable
    monkeypatch.setattr("main.r", mock)
    return mock

def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()

def test_get_job_status():
    # Since we mocked hget to return b"completed"
    response = client.get("/jobs/test-id")
    assert response.status_code == 200
    assert response.json()["status"] == "completed"

def test_get_job_not_found(monkeypatch):
    mock = MagicMock()
    mock.hget.return_value = None
    monkeypatch.setattr("main.r", mock)
    response = client.get("/jobs/non-existent")
    assert response.status_code == 200
    assert response.json() == {"error": "not found"}
