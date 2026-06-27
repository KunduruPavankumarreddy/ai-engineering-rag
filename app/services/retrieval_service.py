from app.retrieval import get_retriever
from app.services.query_router import get_search_config


retriever = get_retriever()


def retrieve_documents(question):

    # Get search configuration based on question type
    config = get_search_config(question)

    # Update retriever search parameters dynamically
    retriever.search_kwargs = config

    print(f"📚 Search Config: {config}")

    docs = retriever.invoke(question)

    return docs