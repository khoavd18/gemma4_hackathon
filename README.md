# Gemma TFT Coach

Initial production-style skeleton for a FastAPI + Qdrant + LangChain + Gemma 4
multimodal RAG app for the Kaggle Gemma 4 Good Hackathon.

## What is included

- FastAPI backend with health, text analysis, and image analysis placeholder routes
- Pydantic settings loaded from environment variables or `.env`
- Qdrant service boundary with Docker Compose
- RAG, Gemma, and strategy service layers
- Streamlit frontend shell
- Smoke test script and basic API tests

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
docker compose up -d qdrant
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API endpoints

- `GET /health`
- `POST /api/v1/analyze/text`
- `POST /api/v1/analyze/image`

Example text request:

```json
{
  "question": "Should I roll on 3-2 or level to 7?",
  "game_state": "Stage 3-2, 58 HP, 42 gold, weak board, two pairs on bench.",
  "rank": "Gold"
}
```

## Streamlit frontend

```powershell
streamlit run frontend/streamlit_app.py
```

## Smoke test

With the API running:

```powershell
python scripts/smoke_test.py
```

## Tests

```powershell
pytest
```

## Still mocked

- Gemma 4 text generation in `app/services/gemma_service.py`
- Gemma 4 multimodal image understanding in `app/services/gemma_service.py`
- LangChain retriever and Qdrant vector search in `app/services/rag_service.py`
- Knowledge ingestion, chunking, embedding, and Qdrant upsert in `scripts/ingest_knowledge.py`
