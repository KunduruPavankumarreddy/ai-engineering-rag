import time

from app.logger import logger
from app.services.memory_service import get_conversation
from app.llm import load_llm


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
- Provide a detailed and well-structured answer.
- Explain the topic step by step when appropriate.
- Include important concepts, reasoning, examples, and comparisons when supported by the document context.
- Do not unnecessarily shorten the answer.
- Use headings, bullet points, and numbered lists when they improve readability..

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

    llm = load_llm()

    start = time.time()
    first_token = True

    try:

        for chunk in llm.stream(prompt):

            if first_token:

                first_token_time = (
                    time.time() - start
                )

                logger.info(
                    f"Time To First Token: "
                    f"{first_token_time:.2f} seconds"
                )

                first_token = False

            if hasattr(chunk, "content"):
                yield chunk.content
            else:
                yield chunk

        generation_time = time.time() - start

        logger.info(
            f"Generation Time: "
            f"{generation_time:.2f} seconds"
        )

    except Exception as e:

        logger.exception(
            "LLM generation failed"
        )

        raise RuntimeError(
            f"LLM generation failed: {e}"
        ) from e