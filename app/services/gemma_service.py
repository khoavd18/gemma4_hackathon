from app.prompts.strategy_prompt import build_strategy_prompt


class GemmaService:
    def generate_strategy(
        self,
        question: str,
        context: str,
        game_state: str | None = None,
        rank: str | None = None,
    ) -> str:
        prompt = build_strategy_prompt(
            question=question,
            context=context,
            game_state=game_state,
            rank=rank,
        )

        # TODO: Send this prompt to Gemma 4 and return the model response.
        return (
            "Mock Gemma TFT Coach response.\n\n"
            "I would use retrieved TFT knowledge plus the current board state to "
            "recommend a line, items, positioning, and next carousel priorities.\n\n"
            f"Prompt preview:\n{prompt}"
        )

    def analyze_image(
        self,
        image_base64: str | None = None,
        question: str | None = None,
    ) -> str:
        # TODO: Use Gemma 4 multimodal input to analyze a TFT board screenshot.
        has_image = "yes" if image_base64 else "no"
        return (
            "Mock image analysis response. "
            f"Image provided: {has_image}. "
            f"Question: {question or 'No question provided.'}"
        )
