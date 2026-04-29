from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Gemma TFT Coach"
    app_version: str = "0.1.0"
    environment: str = Field(default="local", validation_alias="APP_ENV")
    api_v1_prefix: str = "/api/v1"
    log_level: str = "INFO"

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "tft_knowledge"

    gemma_model_name: str = "gemma-4"
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    google_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()
