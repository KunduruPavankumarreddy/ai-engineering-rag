import time

from app.llm import load_llm

llm = load_llm()


def build_prompt(question, context):

    return f"""
You are an expert AI assistant answering questions from uploaded documents.

Instructions:

- Answer ONLY using the provided context.
- If the answer is not found in the context, reply:
  "I couldn't find this information in the uploaded documents."
- Do not make up facts.
- Be concise but complete.
- Use bullet points whenever appropriate.
- If multiple documents contain relevant information, combine it into one clear answer.

Context:
{context}

Question:
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