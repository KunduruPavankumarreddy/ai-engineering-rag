import streamlit as st

from langchain_ollama import ChatOllama


@st.cache_resource
def load_llm():

    print("Loading LLM only once...")

    llm = ChatOllama(
        model="gemma3:4b",
        temperature=0,
    )

    return llm