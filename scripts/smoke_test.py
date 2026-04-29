import os

import requests


API_URL = os.getenv("API_URL", "http://localhost:8000")


def main() -> None:
    health = requests.get(f"{API_URL}/health", timeout=10)
    print("GET /health:", health.status_code, health.json())

    payload = {
        "question": "Should I roll on 3-2 or level to 7?",
        "game_state": "Stage 3-2, 58 HP, 42 gold, weak board, two pairs on bench.",
        "rank": "Gold",
    }
    response = requests.post(f"{API_URL}/api/v1/analyze/text", json=payload, timeout=30)
    print("POST /api/v1/analyze/text:", response.status_code, response.json())


if __name__ == "__main__":
    main()
