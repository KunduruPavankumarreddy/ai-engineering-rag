from pathlib import Path

from app.config import UPLOAD_DIR


def save_uploaded_file(uploaded_file):

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path