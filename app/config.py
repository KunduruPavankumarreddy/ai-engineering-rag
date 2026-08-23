from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# Project Paths
# ----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

BASE_DIR = PROJECT_ROOT

UPLOAD_DIR = BASE_DIR / "uploads"

VECTOR_DB_PATH = BASE_DIR / "vectorstore"

INDEX_DIR = BASE_DIR / "app" / "indexes"

BM25_INDEX_PATH = INDEX_DIR / "bm25_index.pkl"

BM25_DOCUMENTS_PATH = INDEX_DIR / "documents.pkl"

UPLOAD_DIR.mkdir(exist_ok=True)

INDEX_DIR.mkdir(exist_ok=True)

# ----------------------------
# Qdrant
# ----------------------------

QDRANT_HOST = os.getenv("QDRANT_HOST")

QDRANT_PORT = int(os.getenv("QDRANT_PORT"))

COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# ----------------------------
# Embeddings
# ----------------------------

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

VECTOR_SIZE = int(os.getenv("VECTOR_SIZE"))

# ----------------------------
# Chunking
# ----------------------------

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

# ----------------------------
# Ollama
# ----------------------------

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")