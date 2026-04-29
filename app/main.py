from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.config import settings
from app.core.logging import setup_logging


def create_app() -> FastAPI:
    setup_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Gemma TFT Coach API for text and multimodal RAG analysis.",
    )

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(api_router, prefix=settings.api_v1_prefix)
    return app


app = create_app()
