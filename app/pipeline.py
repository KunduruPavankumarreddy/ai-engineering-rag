from app.ingestion import load_pdf
from app.chunking import split_documents
from app.embeddings import load_embedding_model
from app.vectorstore import upload_documents


def ingest_pdf(pdf_path):

    print("Loading PDF...")

    documents = load_pdf(pdf_path)

    print("Chunking...")

    chunks = split_documents(documents)

    print("Loading Embeddings...")

    embeddings = load_embedding_model()

    print("Uploading to Qdrant...")

    upload_documents(chunks, embeddings)

    print("Finished!")