from app.schemas.request_response import (
    AnalyzeImageRequest,
    AnalyzeImageResponse,
    AnalyzeTextRequest,
    AnalyzeTextResponse,
)
from app.services.gemma_service import GemmaService
from app.services.rag_service import RAGService


class StrategyService:
    def __init__(
        self,
        rag_service: RAGService | None = None,
        gemma_service: GemmaService | None = None,
    ) -> None:
        self.rag_service = rag_service or RAGService()
        self.gemma_service = gemma_service or GemmaService()

    def analyze_text(self, request: AnalyzeTextRequest) -> AnalyzeTextResponse:
        snippets = self.rag_service.retrieve_context(request.question)
        context = self.rag_service.format_context(snippets)
        answer = self.gemma_service.generate_strategy(
            question=request.question,
            context=context,
            game_state=request.game_state,
            rank=request.rank,
        )

        return AnalyzeTextResponse(answer=answer, sources=snippets, mocked=True)

    def analyze_image(self, request: AnalyzeImageRequest) -> AnalyzeImageResponse:
        answer = self.gemma_service.analyze_image(
            image_base64=request.image_base64,
            question=request.question,
        )
        return AnalyzeImageResponse(answer=answer, mocked=True)
