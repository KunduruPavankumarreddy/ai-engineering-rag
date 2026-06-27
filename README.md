# AI Engineering RAG Assistant

An end-to-end **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural language questions about their content.

The application retrieves relevant information from uploaded documents using semantic search and generates answers with a **locally running Large Language Model (LLM)**. Instead of relying solely on the model's pre-trained knowledge, responses are grounded in the uploaded document, making the answers more accurate and context-aware.

This project was built to understand how production-style RAG systems work by integrating document processing, vector databases, embeddings, and local LLM inference into a single application.

---

## Features

- Upload PDF documents through a Streamlit interface
- Automatic PDF ingestion and processing
- Intelligent document chunking
- Semantic search using vector embeddings
- HuggingFace embedding model
- Qdrant Vector Database (Docker)
- Local LLM inference using Ollama (Gemma 3)
- Interactive chat interface
- Displays retrieved source chunks
- Modular and scalable project structure

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| UI | Streamlit |
| Framework | LangChain |
| Embedding Model | HuggingFace Sentence Transformers |
| Vector Database | Qdrant |
| LLM | Ollama (Gemma 3) |
| Containerization | Docker |

---

## Project Structure

```text
ai-engineering-rag/
│
├── app/
│   ├── chunking.py
│   ├── config.py
│   ├── embeddings.py
│   ├── ingestion.py
│   ├── llm.py
│   ├── pipeline.py
│   ├── rag.py
│   ├── retrieval.py
│   ├── streamlit_app.py
│   ├── upload.py
│   └── vectorstore.py
│
├── data/
├── uploads/
├── vectorstore/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

1. Upload a PDF document.
2. Extract text from the document.
3. Split the text into smaller chunks.
4. Generate embeddings using a HuggingFace embedding model.
5. Store embeddings in Qdrant Vector Database.
6. Retrieve the most relevant chunks for a user's question.
7. Send the retrieved context and question to Ollama.
8. Display the generated answer along with the retrieved sources.

---

## Installation

Clone the repository.

```bash
git clone https://github.com/KunduruPavankumarreddy/ai-engineering-rag.git

cd ai-engineering-rag
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Run Qdrant

```bash
docker run -d \
--name qdrant \
-p 6333:6333 \
-v qdrant_storage:/qdrant/storage \
qdrant/qdrant
```

---

## Run Ollama

Download Ollama:

https://ollama.com/download

Pull the model.

```bash
ollama pull gemma3:4b
```

---

## Run the Application

```bash
streamlit run app/streamlit_app.py
```

---

## Example Questions

After uploading a PDF, you can ask questions like:

- What is this document about?
- Summarize the document.
- Explain the main concepts.
- What are the important topics discussed?
- Give me a short summary.
- List the key points.

---

## Challenges Faced

During development, I worked through several practical engineering challenges, including:

- Integrating LangChain with Qdrant
- Running Qdrant inside Docker
- Switching from a cloud-based LLM to a local Ollama model
- Organizing the project into modular components
- Improving retrieval quality
- Optimizing model loading for faster responses
- Building an interactive chat interface with Streamlit

These challenges helped me gain a deeper understanding of how modern AI applications are designed and deployed.

---

## Future Improvements

Planned improvements include:

- Multiple PDF support
- Conversation memory
- Hybrid Search (Vector + BM25)
- Cross-Encoder Reranking
- Streaming LLM responses
- FastAPI backend
- Docker Compose support
- Cloud deployment
- User authentication

---

## Key Learnings

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- LangChain
- HuggingFace Embeddings
- Qdrant Vector Database
- Docker
- Ollama
- Streamlit
- Building modular AI applications

This project strengthened my understanding of how retrieval systems, vector databases, and local language models work together to build real-world AI applications.

---

## Author

**Pavan Kumar Reddy**

GitHub: https://github.com/KunduruPavankumarreddy

---

If you found this project interesting or have suggestions for improvement, feel free to open an issue or contribute to the repository.