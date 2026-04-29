STRATEGY_SYSTEM_PROMPT = """
You are Gemma TFT Coach, a practical Teamfight Tactics assistant.
Give concise, actionable advice based on the player's current board, items,
economy, health, stage, and rank. Prefer concrete next steps over vague tips.
"""


def build_strategy_prompt(
    question: str,
    context: str,
    game_state: str | None = None,
    rank: str | None = None,
) -> str:
    return f"""
{STRATEGY_SYSTEM_PROMPT.strip()}

Player rank:
{rank or "Unknown"}

Current game state:
{game_state or "Not provided"}

Retrieved TFT knowledge:
{context}

Player question:
{question}
""".strip()
