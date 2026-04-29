from app.core.config import settings


def main() -> None:
    print("Gemma TFT Coach knowledge ingestion")
    print(f"Qdrant URL: {settings.qdrant_url}")
    print(f"Collection: {settings.qdrant_collection}")
    print("TODO: Load TFT guides/data, chunk documents, embed them, and upsert to Qdrant.")


if __name__ == "__main__":
    main()
