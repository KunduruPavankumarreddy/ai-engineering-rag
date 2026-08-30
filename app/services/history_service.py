import streamlit as st

from app.llm import load_llm
from app.services.memory_service import get_conversation


def is_follow_up(question: str) -> bool:

    question = question.lower().strip()

    follow_up_patterns = [
        "what about",
        "what are its",
        "what is its",
        "how about",
        "why is it",
        "why does it",
        "how does it",
        "how is it",
        "explain that",
        "explain this",
        "tell me more",
        "more about",
        "what about that",
        "what about this",
        "and its",
        "and what",
    ]

    return any(
        pattern in question
        for pattern in follow_up_patterns
    )


@st.cache_data(ttl=3600)
def rewrite_question_cached(question: str, history: str):

    llm = load_llm()

    prompt = f"""
You are a query rewriting assistant.

Rewrite the user's latest question into a complete standalone question.

Rules:
- Use the conversation history.
- Preserve the original meaning.
- Do NOT answer the question.
- Return ONLY the rewritten question.

Conversation:
{history}

Latest Question:
{question}

Standalone Question:
"""

    response = llm.invoke(prompt)

    return response.content.strip()


def rewrite_question(question):

    history = get_conversation()

    # No conversation → nothing to rewrite
    if not history.strip():
        return question

    # Standalone question → don't waste an LLM call
    if not is_follow_up(question):
        return question

    try:

        return rewrite_question_cached(
            question,
            history
        )

    except Exception:

        # Fail-safe: use original question
        return question