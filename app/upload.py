from app.config import UPLOAD_DIR


def save_uploaded_file(uploaded_file):

    # Streamlit UploadedFile
    if hasattr(uploaded_file, "getbuffer"):

        filename = uploaded_file.name

        data = uploaded_file.getbuffer()

    # FastAPI UploadFile
    else:

        filename = uploaded_file.filename

        data = uploaded_file.file.read()

    file_path = UPLOAD_DIR / filename

    with open(file_path, "wb") as f:
        f.write(data)

    return file_path