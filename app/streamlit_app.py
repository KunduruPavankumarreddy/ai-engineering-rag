import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.services.rag_service import ask_question
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

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type="pdf",
    accept_multiple_files=True
)
# -------------------------
# Process PDF
# -------------------------

if uploaded_files:

    if st.button("📥 Process PDF"):

        with st.spinner("Processing PDF..."):

           for uploaded_file in uploaded_files:

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
        
        stream, docs, retrieval_time = ask_question(question)

    with st.chat_message("assistant"):

        answer = st.write_stream(stream)

        st.divider()

        st.markdown("### 📚 Retrieved Sources")

        for i, doc in enumerate(docs, start=1):
           
           from pathlib import Path

           source = Path(
           doc.metadata.get("source", "Unknown PDF")
           ).name
           
           page = doc.metadata.get("page", "Unknown")
           
           with st.expander(
                f"📄 {source} • Page {page}"
            ):

                st.write(doc.page_content)
                
                
        st.divider()

        st.markdown("### ⚡ Performance")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Retrieval",
                f"{retrieval_time:.2f}s"
        )

        with col2:
            st.metric(
              "Generation",
              "Streaming..."
          )
    st.divider()

            
        

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )