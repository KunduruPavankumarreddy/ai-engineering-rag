from app.config import PDF_PATH

from app.ingestion import load_pdf

from app.chunking import split_documents

from app.embeddings import load_embedding_model

from app.vectorstore import upload_documents


def main():

    print("=" * 60)

    print("RAG INGESTION PIPELINE")

    print("=" * 60)

    documents = load_pdf(PDF_PATH)

    chunks = split_documents(documents)

    embeddings = load_embedding_model()

    upload_documents(

        chunks,

        embeddings

    )

    print()

    print("Pipeline Completed Successfully!")

    print()

    print(f"Pages Loaded : {len(documents)}")

    print(f"Chunks Stored : {len(chunks)}")


if __name__ == "__main__":

    main()