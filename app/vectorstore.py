from qdrant_client import QdrantClient

from langchain_qdrant import QdrantVectorStore

from app.config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
)


def get_client():

    client = QdrantClient(

        host=QDRANT_HOST,

        port=QDRANT_PORT

    )

    return client


def create_vectorstore(embeddings):

    client = get_client()

    vectorstore = QdrantVectorStore.from_existing_collection(

        embedding=embeddings,

        collection_name=COLLECTION_NAME,

        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",

    )

    return vectorstore


def upload_documents(chunks, embeddings):

    vectorstore = QdrantVectorStore.from_documents(

        documents=chunks,

        embedding=embeddings,

        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",

        collection_name=COLLECTION_NAME,

    )

    print("Documents uploaded successfully!")

    return vectorstore