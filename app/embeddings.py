import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings

from app.config import EMBEDDING_MODEL


@st.cache_resource
def load_embedding_model():

    print("Loading embedding model only once...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings