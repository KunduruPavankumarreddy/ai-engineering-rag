import time

from app.retrieval import get_retriever
from app.llm import load_llm

retriever = get_retriever()
llm = load_llm()


def ask_question(question):
    
    print("+"*50)
    print("ask_question() called")

    retrieval_start = time.time()

    docs = retriever.invoke(question)

    retrieval_time = time.time() - retrieval_start

    print(f"Retrieval Time: {retrieval_time:.2f} seconds")

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an expert AI assistant answering questions from uploaded documents.

Instructions:

- Answer ONLY from the provided context.
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

    generation_start = time.time()

    response = llm.invoke(prompt)

    generation_time = time.time() - generation_start

    print(f" Generation Time: {generation_time:.2f} seconds")

    return response.content, docs