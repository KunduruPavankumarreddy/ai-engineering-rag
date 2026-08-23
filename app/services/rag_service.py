import time
from app.logger import logger

from app.services.memory_service import add_message
from app.services.retrieval_service import retrieve_documents
from app.services.generation_service import stream_answer
from app.services.history_service import rewrite_question

def ask_question(question):
    add_message("user", question)
    retrieval_start = time.time()
    rewritten_question = rewrite_question(question)

    logger.info(
        f"Original Question: {question} | Rewritten Question: {rewritten_question}"
    )

    docs = retrieve_documents(rewritten_question)

    retrieval_time = time.time() - retrieval_start

    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    stream = stream_answer(
    question,
    context
    )

    logger.info(f" Retrieval Time: {retrieval_time:.2f} seconds")
    return (
    stream,
    docs,
    retrieval_time,
    )