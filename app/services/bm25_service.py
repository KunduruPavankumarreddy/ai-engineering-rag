import pickle

from rank_bm25 import BM25Okapi

from app.logger import logger

from app.config import (
    BM25_INDEX_PATH,
    BM25_DOCUMENTS_PATH
)


def tokenize(text):
    return text.lower().split()


def get_chunk_key(chunk):

    source = chunk.metadata.get("source", "")
    page = chunk.metadata.get("page", "")
    content = chunk.page_content.strip()

    return (
        source,
        page,
        content
    )


def build_bm25(chunks):

    corpus = []

    for chunk in chunks:

        corpus.append(
            tokenize(chunk.page_content)
        )

    return BM25Okapi(corpus)


def save_bm25(bm25, chunks):

    with open(BM25_INDEX_PATH, "wb") as f:

        pickle.dump(
            bm25,
            f
        )

    with open(BM25_DOCUMENTS_PATH, "wb") as f:

        pickle.dump(
            chunks,
            f
        )

    logger.info(
        "BM25 index saved successfully."
    )


def load_bm25():

    with open(BM25_INDEX_PATH, "rb") as f:

        bm25 = pickle.load(f)

    with open(BM25_DOCUMENTS_PATH, "rb") as f:

        chunks = pickle.load(f)

    return bm25, chunks


def bm25_exists():

    return (
        BM25_INDEX_PATH.exists()
        and BM25_DOCUMENTS_PATH.exists()
    )


def deduplicate_chunks(chunks):

    unique_chunks = []
    seen = set()

    for chunk in chunks:

        key = get_chunk_key(chunk)

        if key in seen:
            continue

        seen.add(key)

        unique_chunks.append(chunk)

    return unique_chunks


def update_bm25(new_chunks):

    # --------------------------------
    # Nothing to update
    # --------------------------------

    if not new_chunks:

        logger.info(
            "No new chunks. Skipping BM25 update."
        )

        return

    # --------------------------------
    # Load existing chunks
    # --------------------------------

    if bm25_exists():

        try:

            _, existing_chunks = load_bm25()

        except Exception as e:

            logger.error(
                f"Failed to load BM25 index: {e}"
            )

            raise RuntimeError(
                "Existing BM25 index could not be loaded."
            )

    else:

        existing_chunks = []

    # --------------------------------
    # Combine
    # --------------------------------

    all_chunks = (
        existing_chunks +
        new_chunks
    )

    # --------------------------------
    # Remove duplicates
    # --------------------------------

    all_chunks = deduplicate_chunks(
        all_chunks
    )

    logger.info(
        f"BM25 unique chunks: "
        f"{len(all_chunks)}"
    )

    # --------------------------------
    # Rebuild BM25
    # --------------------------------

    bm25 = build_bm25(
        all_chunks
    )

    # --------------------------------
    # Persist
    # --------------------------------

    save_bm25(
        bm25,
        all_chunks
    )

    logger.info(
        f"BM25 updated with "
        f"{len(all_chunks)} chunks."
    )


def search_bm25(question, top_k=5):

    try:

        bm25, chunks = load_bm25()

    except Exception as e:

        logger.error(
            f"Failed to load BM25 index: {e}"
        )

        raise RuntimeError(
            "BM25 index could not be loaded."
        )

    tokenized_query = tokenize(
        question
    )

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    docs = []

    for index, score in ranked[:top_k]:

        docs.append(
            chunks[index]
        )

    logger.info(
        f"BM25 retrieved "
        f"{len(docs)} chunks."
    )

    return docs