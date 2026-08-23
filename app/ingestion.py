from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from app.logger import logger


def load_pdf(pdf_path):

    loader = PyPDFLoader(str(pdf_path))

    documents = loader.load()

    # Add metadata to every page
    for doc in documents:

        doc.metadata["source"] = Path(pdf_path).name

    logger.info(f"Loaded {len(documents)} pages.")

    return documents