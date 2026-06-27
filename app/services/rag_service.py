import time

from httpcore import stream
from app.services.memory_service import add_message
from app.services.retrieval_service import retrieve_documents
from app.services.generation_service import stream_answer


def ask_question(question):
    add_message("user", question)
    retrieval_start = time.time()
    docs = retrieve_documents(question)

    retrieval_time = time.time() - retrieval_start

    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    stream = stream_answer(
    question,
    context
    )

    print(f"🔍 Retrieval Time: {retrieval_time:.2f} seconds")
    return (
    stream,
    docs,
    retrieval_time,
    )