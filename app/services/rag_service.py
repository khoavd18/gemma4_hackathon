from app.schemas.request_response import SourceSnippet
from app.services.qdrant_service import QdrantService


class RAGService:
    def __init__(self, qdrant_service: QdrantService | None = None) -> None:
        self.qdrant_service = qdrant_service or QdrantService()

    def retrieve_context(self, question: str) -> list[SourceSnippet]:
        # TODO: Replace this with a LangChain retriever backed by Qdrant.
        raw_results = self.qdrant_service.search(question)
        return [
            SourceSnippet(
                source=item.get("source", "unknown"),
                content=item.get("content", ""),
            )
            for item in raw_results
        ]

    @staticmethod
    def format_context(snippets: list[SourceSnippet]) -> str:
        if not snippets:
            return "No retrieved knowledge yet."

        return "\n\n".join(
            f"Source: {snippet.source}\n{snippet.content}" for snippet in snippets
        )
