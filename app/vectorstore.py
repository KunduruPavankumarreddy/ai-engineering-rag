import uuid

from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

from app.config import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
)

from app.logger import logger


def get_client():

    client = QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT
    )

    return client


def create_vectorstore(embeddings):

    vectorstore = QdrantVectorStore.from_existing_collection(

        embedding=embeddings,

        collection_name=COLLECTION_NAME,

        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",

    )

    return vectorstore


def generate_chunk_id(chunk):

    source = chunk.metadata.get("source", "")
    page = chunk.metadata.get("page", "")
    content = chunk.page_content.strip()

    raw = f"{source}:{page}:{content}"

    return str(
        uuid.uuid5(
            uuid.NAMESPACE_URL,
            raw
        )
    )


def get_existing_ids(client, chunk_ids):

    existing_ids = set()

    if not chunk_ids:
        return existing_ids

    records = client.retrieve(
        collection_name=COLLECTION_NAME,
        ids=chunk_ids,
        with_payload=False,
        with_vectors=False,
    )

    for record in records:

        existing_ids.add(
            str(record.id)
        )

    return existing_ids


def upload_documents(chunks, embeddings):

    client = get_client()

    # --------------------------------
    # Generate deterministic IDs
    # --------------------------------

    chunk_ids = [
        generate_chunk_id(chunk)
        for chunk in chunks
    ]

    # --------------------------------
    # Find existing chunks
    # --------------------------------

    try:

        existing_ids = get_existing_ids(
            client,
            chunk_ids
        )

    except Exception as e:

        logger.warning(
            f"Could not check existing chunks: {e}"
        )

        existing_ids = set()

    # --------------------------------
    # Keep only new chunks
    # --------------------------------

    new_chunks = []
    new_ids = []

    for chunk, chunk_id in zip(
        chunks,
        chunk_ids
    ):

        if chunk_id not in existing_ids:

            new_chunks.append(chunk)
            new_ids.append(chunk_id)

    logger.info(
        f"Total chunks: {len(chunks)}"
    )

    logger.info(
        f"Existing chunks: {len(existing_ids)}"
    )

    logger.info(
        f"New chunks: {len(new_chunks)}"
    )

    # --------------------------------
    # Nothing new
    # --------------------------------

    if not new_chunks:

        logger.info(
            "No new chunks. "
            "Skipping embedding generation."
        )

        return (
            create_vectorstore(embeddings),
            []
        )

    # --------------------------------
    # Embed + upload new chunks
    # --------------------------------

    vectorstore = QdrantVectorStore.from_documents(

        documents=new_chunks,

        embedding=embeddings,

        ids=new_ids,

        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",

        collection_name=COLLECTION_NAME,

    )

    logger.info(
        f"Uploaded {len(new_chunks)} new chunks."
    )

    return (
        vectorstore,
        new_chunks
    )