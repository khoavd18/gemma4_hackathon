from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analyze_text() -> None:
    response = client.post(
        "/api/v1/analyze/text",
        json={
            "question": "Should I roll or level?",
            "game_state": "Stage 3-2, 40 gold, stable board.",
            "rank": "Gold",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["mocked"] is True
    assert "Mock Gemma TFT Coach response" in body["answer"]
    assert body["sources"] == []


def test_analyze_image_placeholder() -> None:
    response = client.post(
        "/api/v1/analyze/image",
        json={"question": "What positioning mistake do you see?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["mocked"] is True
    assert "Mock image analysis response" in body["answer"]
