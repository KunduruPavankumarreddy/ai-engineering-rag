import time

from app.services.hybrid_service import hybrid_search
from app.services.reranker_service import rerank_documents
from app.services.query_router import get_search_config
from app.logger import logger


def retrieve_documents(question):

    # 1. Query Router
    start = time.time()

    config = get_search_config(question)

    router_time = time.time() - start

    logger.info(
        f"Query Router Time: {router_time:.2f} seconds"
    )

    logger.info(f"Search Config: {config}")


    # 2. Hybrid Search
    start = time.time()

    docs = hybrid_search(
        question,
        config
    )

    hybrid_time = time.time() - start

    logger.info(
        f"Hybrid Search Time: {hybrid_time:.2f} seconds"
    )


    # 3. Reranking
    start = time.time()

    docs = rerank_documents(
        question,
        docs
    )

    rerank_time = time.time() - start

    logger.info(
        f"Reranking Time: {rerank_time:.2f} seconds"
    )


    return docs