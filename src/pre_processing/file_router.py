import os
from .pdf_extractor import extract_pdf
from .docx_extractor import extract_docx
from .text_cleaner import clean_text


def route_file(filepath):
    """Route file to appropriate extractor and return raw + cleaned text."""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        raw_text = extract_pdf(filepath)
    elif ext == ".docx":
        raw_text = extract_docx(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    cleaned_text = clean_text(raw_text)
    return raw_text, cleaned_text
