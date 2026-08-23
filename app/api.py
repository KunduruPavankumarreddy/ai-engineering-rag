
from fastapi import FastAPI, UploadFile, File
from typing import List
from app.services.health_service import check_health
from fastapi import HTTPException
from app.pipeline import ingest_pdf
from app.upload import save_uploaded_file
from app.logger import logger
from app.exceptions.handlers import global_exception_handler

from app.models.schemas import (
    QueryRequest,
    QueryResponse,
)

from app.services.rag_service import ask_question

app = FastAPI(
    title="AI Engineering RAG API",
    version="1.0.0"
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)


@app.get("/")
def home():

    return {
        "message": "AI Engineering RAG API"
    }


@app.post(
    "/query",
    response_model=QueryResponse
)
def query(request: QueryRequest):
    try:
        stream, docs, retrieval_time = ask_question(
            request.question
        )
    except Exception as e:
        
        logger.error(f"Query processing failed: {e}")
        
        raise HTTPException(status_code=500, detail=f"unable to process your request")

    answer = ""

    for chunk in stream:
        
        if chunk.content:
            answer += chunk.content

    return QueryResponse(
        answer=answer
    )
    
@app.post("/upload")
def upload_pdf(
    file: UploadFile = File(...)
):

    pdf_path = save_uploaded_file(file)

    ingest_pdf(pdf_path)

    return {
        "message": "PDF processed successfully.",
        "file": file.filename
    }

@app.get("/health")
def health():

     return check_health()
