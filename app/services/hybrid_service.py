import time


from app.retrieval import get_retriever
from app.services.bm25_service import search_bm25
from app.logger import logger


def hybrid_search(question, config):

    logger.info("Hybrid Search Started")

    retriever = get_retriever()

    # Number of documents retrieved BEFORE reranking
    candidate_k = max(config.get("k", 3), 10)

    # Apply query-router configuration
    search_config = config.copy()
    search_config["k"] = candidate_k

    # If using MMR, make sure fetch_k is large enough
    if "fetch_k" in search_config:
        search_config["fetch_k"] = max(
            search_config["fetch_k"],
            candidate_k
        )

    retriever.search_kwargs = search_config

    logger.info(
        f" Vector candidate retrieval: top {candidate_k}"
    )

    try:
        vector_docs = retriever.invoke(question)

    except Exception as e:
        logger.error(f"Vector Search failed: {e}")
        raise RuntimeError("Vector search failed.")

    logger.info(
        f" BM25 candidate retrieval: top {candidate_k}"
    )

    bm25_docs = search_bm25(
        question,
        top_k=candidate_k
    )

    merged = []
    seen = set()

    for doc in vector_docs + bm25_docs:

        text = doc.page_content.strip()

        if text not in seen:
            merged.append(doc)
            seen.add(text)

    logger.info(f"Vector Docs : {len(vector_docs)}")
    logger.info(f"BM25 Docs   : {len(bm25_docs)}")
    logger.info(f"Final Candidates : {len(merged)}")

    return merged