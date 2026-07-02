from app.retrieval import get_retriever
from app.services.bm25_service import search_bm25

retriever = get_retriever()


def hybrid_search(question, config):

    print("🚀 Hybrid Search Started")

    # Apply Query Router configuration
    retriever.search_kwargs = config

    print("🔍 Vector Search...")
    vector_docs = retriever.invoke(question)

    print("🔎 BM25 Search...")
    bm25_docs = search_bm25(
        question,
        top_k=config["k"]
    )

    merged = []
    seen = set()

    for doc in vector_docs + bm25_docs:

        text = doc.page_content.strip()

        if text not in seen:
            merged.append(doc)
            seen.add(text)

    print(f"Vector Docs : {len(vector_docs)}")
    print(f"BM25 Docs   : {len(bm25_docs)}")
    print(f"Final Docs  : {len(merged)}")

    return merged