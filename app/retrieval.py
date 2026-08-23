from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from app.embeddings import load_embedding_model
from app.config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
)

def get_retriever():
    embeddings = load_embedding_model()

    client = QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT
    )

    collections = client.get_collections()

    exists = any(
        c.name == COLLECTION_NAME
        for c in collections.collections
    )

    if not exists:
        raise RuntimeError(
            "No documents uploaded yet. Please upload a PDF first."
        )

    vectorstore = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",
    )

    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 2,
            "fetch_k": 10,
            "lambda_mult": 0.5,
        },
    )