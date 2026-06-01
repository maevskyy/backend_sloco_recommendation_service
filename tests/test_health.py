from fastapi.testclient import TestClient

from recommendation_service.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "recommendation-service",
        "environment": "development",
    }


def test_ready_returns_ok() -> None:
    response = client.get("/v1/health/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_meta_returns_empty_algorithm_list() -> None:
    response = client.get("/v1/meta")

    assert response.status_code == 200
    assert response.json() == {
        "service": "recommendation-service",
        "environment": "development",
        "version": "0.1.0",
        "algorithms": [],
    }

