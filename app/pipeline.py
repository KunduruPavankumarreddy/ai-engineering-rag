from app.ingestion import load_pdf
from app.logger import logger
from app.chunking import split_documents
from app.embeddings import load_embedding_model
from app.vectorstore import upload_documents
from app.services.bm25_service import update_bm25


def ingest_pdf(pdf_path):
    """
    Load PDF, split into chunks,
    deduplicate chunks,
    generate embeddings only for new chunks,
    upload new vectors to Qdrant,
    and update BM25 with new chunks.
    """

    logger.info("Loading PDF...")

    documents = load_pdf(pdf_path)

    logger.info("Chunking...")

    chunks = split_documents(documents)

    logger.info("Loading embeddings...")

    embeddings = load_embedding_model()

    logger.info("Uploading to Qdrant...")

    vectorstore, new_chunks = upload_documents(
        chunks,
        embeddings
    )

    # --------------------------------
    # Update BM25 only with new chunks
    # --------------------------------

    if new_chunks:

        logger.info(
            f"Updating BM25 with "
            f"{len(new_chunks)} new chunks..."
        )

        update_bm25(new_chunks)

    else:

        logger.info(
            "No new chunks. "
            "Skipping BM25 update."
        )

    logger.info("Finished!")

    return vectorstore