from fastapi import APIRouter

from app.schemas.request_response import (
    AnalyzeImageRequest,
    AnalyzeImageResponse,
    AnalyzeTextRequest,
    AnalyzeTextResponse,
)
from app.services.strategy_service import StrategyService

router = APIRouter(tags=["analysis"])
strategy_service = StrategyService()


@router.post("/analyze/text", response_model=AnalyzeTextResponse)
async def analyze_text(request: AnalyzeTextRequest) -> AnalyzeTextResponse:
    return strategy_service.analyze_text(request)


@router.post("/analyze/image", response_model=AnalyzeImageResponse)
async def analyze_image(request: AnalyzeImageRequest) -> AnalyzeImageResponse:
    return strategy_service.analyze_image(request)
