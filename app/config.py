from pathlib import Path

# ----------------------------
# Paths
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(exist_ok=True)

PDF_PATH = BASE_DIR / "data" / "python_handbok.pdf"

VECTOR_DB_PATH = BASE_DIR / "vectorstore"

# ----------------------------
# Qdrant
# ----------------------------

COLLECTION_NAME = "python_docs"

QDRANT_HOST = "localhost"

QDRANT_PORT = 6333

# ----------------------------
# Chunking
# ----------------------------

CHUNK_SIZE = 700

CHUNK_OVERLAP = 100

# ----------------------------
# Embedding Model
# ----------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

VECTOR_SIZE = 384