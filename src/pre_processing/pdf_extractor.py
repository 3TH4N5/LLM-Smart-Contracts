import fitz  # PyMuPDF


def extract_pdf(filepath):
    """Extract text from a PDF using PyMuPDF."""
    text = ""
    try:
        with fitz.open(filepath) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return text
