from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.logger import logger
from app.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP

    )

    chunks = splitter.split_documents(documents)

    logger.info(f"Created {len(chunks)} chunks.")

    return chunks