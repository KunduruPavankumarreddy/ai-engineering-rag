import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.rag import ask_question
from app.pipeline import ingest_pdf
from app.upload import save_uploaded_file
if "messages" not in st.session_state:
    st.session_state.messages = []


st.set_page_config(
    page_title="AI Engineering RAG",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Engineering RAG Assistant")

st.write("Ask questions about your uploaded PDF.")
st.header("📂 Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type="pdf"
)
# -------------------------
# Process PDF
# -------------------------

if uploaded_file is not None:

    if st.button("📥 Process PDF"):

        with st.spinner("Processing PDF..."):

            pdf_path = save_uploaded_file(uploaded_file)

            ingest_pdf(pdf_path)

        st.success("PDF processed successfully!")
        
# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 
# -------------------------
# Ask Question
# -------------------------

question = st.chat_input("Ask a question")

if question:

    # User
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # AI
    with st.spinner("Searching..."):

        answer, docs = ask_question(question)

    with st.chat_message("assistant"):

        st.markdown(answer)

        st.divider()

        st.markdown("### 📚 Retrieved Sources")

        for i, doc in enumerate(docs, start=1):

            with st.expander(
                f"Chunk {i} | Page {doc.metadata.get('page', 0)+1}"
            ):

                st.write(doc.page_content)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )