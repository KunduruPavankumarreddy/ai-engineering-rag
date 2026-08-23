import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import EMBEDDING_MODEL
from app.logger import logger


@st.cache_resource
def load_embedding_model():

    logger.info("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    logger.info("Embedding model loaded successfully.")

    return embeddings