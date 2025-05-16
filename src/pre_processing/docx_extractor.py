from docx import Document


def extract_docx(filepath):
    """Extract text from a DOCX file."""
    try:
        doc = Document(filepath)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""
