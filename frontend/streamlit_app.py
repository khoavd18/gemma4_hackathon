import requests
import streamlit as st


st.set_page_config(page_title="Gemma TFT Coach", page_icon="G")

st.title("Gemma TFT Coach")

api_url = st.sidebar.text_input("API URL", "http://localhost:8000")

question = st.text_area("Question", "What should I do from this spot?")
game_state = st.text_area(
    "Game state",
    "Stage 3-2, 58 HP, 42 gold, weak board, two pairs on bench.",
)
rank = st.text_input("Rank", "Gold")

if st.button("Analyze Text"):
    payload = {
        "question": question,
        "game_state": game_state,
        "rank": rank,
    }

    try:
        response = requests.post(
            f"{api_url}/api/v1/analyze/text",
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        st.subheader("Coach response")
        st.write(data["answer"])
        st.caption(f"Mocked: {data['mocked']}")
    except requests.RequestException as exc:
        st.error(f"API request failed: {exc}")
