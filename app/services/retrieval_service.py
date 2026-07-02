from app.services.hybrid_service import hybrid_search

from app.services.reranker_service import rerank_documents

from app.services.query_router import get_search_config

def retrieve_documents(question):

    config = get_search_config(question)

    print(f"📚 Search Config: {config}")

    docs = hybrid_search(
        question,
        config
    )
    docs = rerank_documents(question, docs)

    return docs