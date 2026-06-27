from app.retrieval import get_retriever


retriever = get_retriever()


def retrieve_documents(question):

    docs = retriever.invoke(question)

    return docs