import streamlit as st

from langchain_qdrant import QdrantVectorStore

from app.embeddings import load_embedding_model

from app.config import (
    COLLECTION_NAME,
    QDRANT_HOST,
    QDRANT_PORT,
)


@st.cache_resource
def get_retriever():

    print("Loading retriever only once...")

    embeddings = load_embedding_model()

    vectorstore = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",
    )

    retriever = vectorstore.as_retriever(

    search_type="mmr",

    search_kwargs={
        "k":2,
        "fetch_k":10,
        "lambda_mult":0.5
    }
    )

    return retriever