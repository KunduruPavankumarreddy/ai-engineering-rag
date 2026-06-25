from langchain_ollama import ChatOllama


def load_llm():

    llm = ChatOllama(
        model="gemma3:4b",
        temperature=0
    )

    return llm