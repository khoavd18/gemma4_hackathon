from pydantic import BaseModel, Field


class AnalyzeTextRequest(BaseModel):
    question: str = Field(..., min_length=1, description="TFT coaching question.")
    game_state: str | None = Field(
        default=None,
        description="Optional text summary of board, items, units, HP, gold, and stage.",
    )
    rank: str | None = Field(default=None, description="Optional player rank.")


class AnalyzeImageRequest(BaseModel):
    image_base64: str | None = Field(
        default=None,
        description="Base64-encoded TFT screenshot. Placeholder until upload support exists.",
    )
    question: str | None = Field(
        default=None,
        description="Optional question to ask about the image.",
    )


class SourceSnippet(BaseModel):
    source: str
    content: str


class AnalyzeTextResponse(BaseModel):
    answer: str
    sources: list[SourceSnippet] = Field(default_factory=list)
    mocked: bool = True


class AnalyzeImageResponse(BaseModel):
    answer: str
    mocked: bool = True
