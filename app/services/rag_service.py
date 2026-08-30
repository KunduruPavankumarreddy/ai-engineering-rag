import time

from app.logger import logger

from app.services.memory_service import add_message
from app.services.retrieval_service import retrieve_documents
from app.services.generation_service import stream_answer
from app.services.history_service import rewrite_question


def ask_question(question):
    """
    Process a user question through the complete RAG pipeline.

    Flow:
    1. Store conversation message
    2. Rewrite follow-up question
    3. Retrieve relevant documents
    4. Build context
    5. Generate streaming response
    """

    add_message("user", question)

    # -------------------------
    # Question Rewriting
    # -------------------------

    rewrite_start = time.time()

    rewritten_question = rewrite_question(question)

    rewrite_time = time.time() - rewrite_start

    logger.info(
        f"Original Question: {question} | "
        f"Rewritten Question: {rewritten_question}"
    )

    logger.info(
        f"Question Rewrite Time: {rewrite_time:.2f} seconds"
    )

    # -------------------------
    # Retrieval
    # -------------------------

    retrieval_start = time.time()

    docs = retrieve_documents(rewritten_question)

    retrieval_time = time.time() - retrieval_start

    logger.info(
        f"Retrieval Time: {retrieval_time:.2f} seconds"
    )

    # -------------------------
    # Build Context
    # -------------------------

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # -------------------------
    # Generation
    # -------------------------

    stream = stream_answer(
        question,
        context
    )

    return (
        stream,
        docs,
        rewrite_time,
        retrieval_time,
    )