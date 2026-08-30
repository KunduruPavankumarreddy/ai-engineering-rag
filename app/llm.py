import streamlit as st

from google import genai
from langchain_ollama import ChatOllama

from app.config import (
    LLM_PROVIDER,
    GEMINI_API_KEY,
    GEMINI_MODEL,
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)

from app.logger import logger


class GeminiResponse:

    def __init__(self, text):
        self.content = text


class GeminiLLM:

    def __init__(self, client, model):

        self.client = client
        self.model = model

    def invoke(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return GeminiResponse(response.text)

    def stream(self, prompt):

        response = self.client.models.generate_content_stream(
            model=self.model,
            contents=prompt,
        )

        for chunk in response:

            if chunk.text:
                yield chunk.text


@st.cache_resource
def load_llm():

    logger.info(
        f"Loading LLM provider: {LLM_PROVIDER}"
    )

    # --------------------------------
    # Gemini
    # --------------------------------

    if LLM_PROVIDER == "gemini":

        if not GEMINI_API_KEY:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        logger.info(
            f"Gemini model: {GEMINI_MODEL}"
        )

        return GeminiLLM(
            client=client,
            model=GEMINI_MODEL,
        )

    # --------------------------------
    # Ollama
    # --------------------------------

    if LLM_PROVIDER == "ollama":

        logger.info(
            f"Ollama model: {OLLAMA_MODEL}"
        )

        return ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0,
        )

    raise ValueError(
        f"Unsupported LLM provider: {LLM_PROVIDER}"
    )