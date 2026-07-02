from sentence_transformers import CrossEncoder

print("Loading CrossEncoder...")

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

print("✅ CrossEncoder Loaded")


def rerank_documents(question, docs, top_k=3):

    if len(docs) <= top_k:
        return docs

    print(f"🤖 Reranking {len(docs)} documents...")

    # Create (question, document) pairs
    pairs = [
        (question, doc.page_content)
        for doc in docs
    ]

    # Predict relevance scores
    scores = reranker.predict(pairs)

    # Combine documents with scores
    ranked = list(zip(docs, scores))

    # Sort by score (highest first)
    ranked.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Keep only top_k documents
    top_docs = [
        doc
        for doc, score in ranked[:top_k]
    ]

    print(f"✅ Selected top {len(top_docs)} documents.")

    return top_docs
