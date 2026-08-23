from app.ingestion import load_pdf
from app.logger import logger
from app.chunking import split_documents
from app.embeddings import load_embedding_model
from app.vectorstore import upload_documents
from app.services.bm25_service import (
    build_bm25,
    save_bm25
)

def ingest_pdf(pdf_path):
    """
    Load a PDF, split it into chunks,
    generate embeddings, upload to Qdrant,
    and update the BM25 index.
    """

    logger.info("Loading PDF...")

    documents = load_pdf(pdf_path)

    logger.info("Chunking...")

    chunks = split_documents(documents)

    logger.info("Loading Embeddings...")

    embeddings = load_embedding_model()

    logger.info("Uploading to Qdrant...")

    upload_documents(chunks, embeddings)
    
    logger.info("Building BM25 index...")

    from app.services.bm25_service import update_bm25

    logger.info("Updating BM25 index...")

    update_bm25(chunks)

    logger.info("Finished!")