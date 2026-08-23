import streamlit as st

from langchain_ollama import ChatOllama

from app.config import OLLAMA_BASE_URL, OLLAMA_MODEL
from app.logger import logger


@st.cache_resource
def load_llm():

    logger.info("Loading LLM...")

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0,
    )

    logger.info("LLM loaded successfully.")

    return llm