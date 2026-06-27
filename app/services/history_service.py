from app.llm import load_llm
from app.services.memory_service import get_conversation

llm = load_llm()


def rewrite_question(question):

    history = get_conversation()

    if not history.strip():
        return question

    prompt = f"""
You are a query rewriting assistant.

Your job is to rewrite the user's latest question into a complete standalone question.

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

    rewritten = response.content.strip()

    return rewritten