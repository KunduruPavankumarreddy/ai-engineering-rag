import time
from app.services.memory_service import get_conversation

from app.llm import load_llm

llm = load_llm()


def build_prompt(question, context):

    history = get_conversation()

    return f"""
You are an expert AI assistant answering questions from uploaded documents.

Instructions:

- Use the conversation history to understand follow-up questions.
- Answer ONLY using the provided document context.
- If the answer is not in the context, reply:
  "I couldn't find this information in the uploaded documents."
- Never invent facts.
- Be concise and well formatted.

Conversation History:
{history}

Document Context:
{context}

Current Question:
{question}

Answer:
"""


def stream_answer(question, context):

    prompt = build_prompt(question, context)

    start = time.time()

    for chunk in llm.stream(prompt):
        yield chunk

    generation_time = time.time() - start

    print(f"🤖 Generation Time: {generation_time:.2f} seconds")