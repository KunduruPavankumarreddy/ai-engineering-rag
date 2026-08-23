from qdrant_client import QdrantClient

from app.config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME
)

from app.services.bm25_service import bm25_exists
from app.llm import load_llm


def check_health():

    status = {
        "status": "healthy"
    }

    # -------------------
    # Qdrant
    # -------------------
    try:

        client = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT
        )

        client.get_collection(COLLECTION_NAME)

        status["qdrant"] = "connected"

    except Exception:

        status["qdrant"] = "disconnected"

    # -------------------
    # BM25
    # -------------------
    status["bm25"] = (
        "loaded"
        if bm25_exists()
        else "not loaded"
    )

    # -------------------
    # Ollama
    # -------------------
    try:

        load_llm()

        status["ollama"] = "loaded"

    except Exception:

        status["ollama"] = "not loaded"

    return status