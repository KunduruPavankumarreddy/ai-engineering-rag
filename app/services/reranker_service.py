import time
import streamlit as st

from sentence_transformers import CrossEncoder
from app.logger import logger


@st.cache_resource
def load_reranker():

    logger.info("Loading CrossEncoder...")

    reranker = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    logger.info("CrossEncoder loaded successfully.")

    return reranker


def rerank_documents(question, docs, top_k=5):

    if len(docs) <= top_k:
        return docs

    logger.info(f"Reranking {len(docs)} documents...")

    reranker = load_reranker()

    pairs = [
        (question, doc.page_content)
        for doc in docs
    ]

    rerank_start = time.time()

    scores = reranker.predict(pairs)

    rerank_time = time.time() - rerank_start

    logger.info(
        f"Cross-Encoder Reranking Time: "
        f"{rerank_time:.2f} seconds"
    )

    ranked = list(zip(docs, scores))

    ranked.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_docs = [
        doc
        for doc, score in ranked[:top_k]
    ]

    logger.info(
        f"Selected top {len(top_docs)} documents."
    )

    return top_docs