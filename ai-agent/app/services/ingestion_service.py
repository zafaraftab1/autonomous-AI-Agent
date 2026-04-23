# Purpose: Process uploaded files and store in FAISS

from app.ingestion.pdf_loader import extract_text_from_pdf
from app.ingestion.image_ocr import extract_text_from_image
from app.ingestion.chunking import chunk_text
from app.memory.vector_store import vector_store


def process_file(file_path: str, file_type: str):
    """
    file_type: pdf or image
    """

    # Step 1: Extract text
    if file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    # Step 2: Chunk
    chunks = chunk_text(text)

    # Step 3: Store in FAISS
    for chunk in chunks:
        vector_store.add(chunk, source=file_path)

    return {"status": "processed", "chunks": len(chunks)}