# 🚀 Production-Ready RAG System

A production-style Retrieval-Augmented Generation (RAG) application built using **FastAPI**, **LangChain**, **Qdrant**, **Ollama**, and **Docker**.

The system enables users to upload PDF documents, retrieve relevant information using **Hybrid Search (Vector + BM25)**, rerank results using a **Cross Encoder**, and generate accurate responses using a local **Gemma 3** Large Language Model.

---
## Key Highlights

- Production-ready FastAPI backend
- Dockerized deployment
- Hybrid Retrieval (Dense + Sparse)
- Cross Encoder reranking
- Conversation-aware RAG
- Local LLM using Ollama
- Evaluation with DeepEval

# 📌 Features

- 📄 PDF Upload & Ingestion
- ✂️ Intelligent Text Chunking
- 🧠 Sentence Transformer Embeddings
- 📦 Qdrant Vector Database
- 🔍 Hybrid Search
  - Dense Vector Search
  - BM25 Keyword Search
- 🎯 Cross Encoder Reranking
- 🧠 Query Rewriting
- 💬 Conversation Memory
- ⚡ Streaming LLM Responses
- 🌐 FastAPI REST API
- 🐳 Dockerized Deployment
- 📊 DeepEval Integration
- ❤️ Health Check Endpoint

---

# 🏗️ System Architecture

```

```text
                    User
                      │
                      ▼
                 FastAPI API
                      │
          ┌───────────┴────────────┐
          │                        │
     Upload PDF               Ask Question
          │                        │
          ▼                        ▼
    PDF Loader             Query Rewriter
          │                        │
          ▼                        ▼
     Chunk Documents        Query Router
          │                        │
          ▼                        ▼
 Generate Embeddings      Hybrid Retrieval
          │              ┌───────────────┐
          ▼              │               │
      Qdrant DB      Vector Search   BM25 Search
          │              │               │
          └──────────────┴───────────────┘
                         │
                         ▼
                Cross Encoder Reranker
                         │
                         ▼
                 Gemma3 (Ollama)
                         │
                         ▼
                    Final Response
```

---

# ⚙️ Tech Stack

## Backend

- FastAPI
- Uvicorn
- Python

## LLM Framework

- LangChain

## Embeddings

- sentence-transformers
- all-MiniLM-L6-v2

## Vector Database

- Qdrant

## LLM

- Ollama
- Gemma3:4B

## Retrieval

- Dense Vector Search
- BM25
- Hybrid Search
- Query Routing

## Reranking

- Cross Encoder
- ms-marco-MiniLM-L6-v2

## Evaluation

- DeepEval

## Deployment

- Docker
- Docker Compose

---

# 📂 Project Structure

```

```text
rag-system
│
├── app
│   ├── api.py
│   ├── config.py
│   ├── pipeline.py
│   ├── retrieval.py
│   ├── vectorstore.py
│   ├── ingestion.py
│   ├── embeddings.py
│   ├── chunking.py
│   ├── logger.py
│   │
│   ├── prompts
│   ├── services
│   └── indexes
│
├── evaluation
│
├── uploads
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

# 🔄 RAG Pipeline

```

```text
PDF
 │
 ▼
Load PDF
 │
 ▼
Chunking
 │
 ▼
Embedding Generation
 │
 ▼
Upload to Qdrant
 │
 ▼
Build BM25 Index
 │
 ▼
────────────────────────────
User Question
 │
 ▼
Conversation History
 │
 ▼
Question Rewriting
 │
 ▼
Query Router
 │
 ▼
Hybrid Search
 │
 ▼
Cross Encoder
 │
 ▼
Gemma3
 │
 ▼
Streaming Response
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone <your-repository-url>

cd rag-system
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create

```
.env
```

from

```
.env.example
```

---

## Start Ollama

```bash
ollama serve
```

Pull model

```bash
ollama pull gemma3:4b
```

---

## Run with Docker

```bash
docker compose up --build
```

---

# 📡 API Endpoints

## Health Check

```
GET /health
```

Returns application health.

---

## Upload PDF

```
POST /upload
```

Uploads a PDF and builds

- Vector Database
- BM25 Index

---

## Query

```
POST /query
```

Returns an answer generated using

- Hybrid Retrieval
- Cross Encoder
- Gemma3

---

# 🐳 Docker Services

| Service | Purpose |
|----------|----------|
| FastAPI | Backend API |
| Qdrant | Vector Database |
| Ollama | Local LLM |

---

# 📈 Future Improvements

- Authentication
- Multi-user support
- Redis caching
- LangSmith Monitoring
- Kubernetes Deployment
- CI/CD Pipeline
- Cloud Deployment (AWS/GCP/Azure)
- Observability with Prometheus & Grafana

---

# 📊 Evaluation

The project supports evaluation using **DeepEval** to measure response quality and validate retrieval performance.

---

# 📸 Screenshots

Add screenshots here

- Swagger UI
- Streamlit UI
- Docker Containers
- Qdrant Dashboard

---

# 👨‍💻 Author

**Pavan Kunduru**

AI Engineer | Machine Learning | Generative AI | LLM Engineering
