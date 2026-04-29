import logging
from typing import Any

from app.core.config import settings

logger = logging.getLogger(__name__)


class QdrantService:
    def __init__(
        self,
        url: str | None = None,
        collection_name: str | None = None,
    ) -> None:
        self.url = url or settings.qdrant_url
        self.collection_name = collection_name or settings.qdrant_collection
        self._client: Any | None = None

    @property
    def client(self) -> Any:
        if self._client is None:
            from qdrant_client import QdrantClient

            self._client = QdrantClient(url=self.url)
        return self._client

    def is_available(self) -> bool:
        try:
            self.client.get_collections()
            return True
        except Exception as exc:
            logger.warning("Qdrant is not available: %s", exc)
            return False

    def search(self, query: str, limit: int = 5) -> list[dict[str, str]]:
        # TODO: Embed the query and search Qdrant with LangChain or qdrant-client.
        logger.info("Mock Qdrant search for query=%r limit=%s", query, limit)
        return []
