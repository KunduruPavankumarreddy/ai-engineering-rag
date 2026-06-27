from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):

    loader = PyPDFLoader(str(pdf_path))

    documents = loader.load()

    # Add metadata to every page
    for doc in documents:

        doc.metadata["source"] = Path(pdf_path).name

    print(f"Loaded {len(documents)} pages.")

    return documents