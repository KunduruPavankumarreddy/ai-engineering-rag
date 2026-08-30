import streamlit as st

from langchain_core.documents import Document

from app.services.hybrid_service import hybrid_search
from app.services.reranker_service import rerank_documents
from app.services.query_router import get_search_config
from app.services.kb_service import get_kb_version
from app.logger import logger


@st.cache_data(ttl=3600)
def retrieve_documents_cached(
    question,
    knowledge_base_version
):

    logger.info("Retrieval Cache: MISS")

    config = get_search_config(question)

    docs = hybrid_search(
        question,
        config
    )

    logger.info(
        f"Candidates before reranking: {len(docs)}"
    )

    docs = rerank_documents(
        question,
        docs,
        top_k=2
    )

    logger.info(
        f"Documents after reranking: {len(docs)}"
    )

    return [
        {
            "page_content": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in docs
    ]


def retrieve_documents(question):

    knowledge_base_version = get_kb_version()

    cached_docs = retrieve_documents_cached(
        question,
        knowledge_base_version
    )

    return [
        Document(
            page_content=doc["page_content"],
            metadata=doc["metadata"]
        )
        for doc in cached_docs
    ]