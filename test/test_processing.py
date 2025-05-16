# tests/test_preprocessing.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.pre_processing import extract_pdf, extract_docx, clean_text, route_file


def test_extract_pdf():
    sample_path = "tests/sample_data/sample.pdf"
    if os.path.exists(sample_path):
        text = extract_pdf(sample_path)
        assert isinstance(text, str)
        assert len(text) > 0
    else:
        print(f"PDF sample not found: {sample_path}")


def test_extract_docx():
    sample_path = "tests/sample_data/sample.docx"
    if os.path.exists(sample_path):
        text = extract_docx(sample_path)
        assert isinstance(text, str)
        assert len(text) > 0
    else:
        print(f"DOCX sample not found: {sample_path}")


def test_clean_text():
    dirty_text = "CONFIDENTIAL\nThis is a draft document.\nPage 2 of 3\n"
    cleaned = clean_text(dirty_text)
    assert "CONFIDENTIAL" not in cleaned.upper()
    assert "PAGE 2 OF 3" not in cleaned.upper()
    assert "draft" not in cleaned.lower()


def test_route_file_docx():
    sample_path = "tests/sample_data/sample.docx"
    if os.path.exists(sample_path):
        raw, clean = route_file(sample_path)
        assert isinstance(raw, str) and isinstance(clean, str)
        assert len(clean) > 0
    else:
        print(f"DOCX sample not found: {sample_path}")


def test_route_file_pdf():
    sample_path = "tests/sample_data/sample.pdf"
    if os.path.exists(sample_path):
        raw, clean = route_file(sample_path)
        assert isinstance(raw, str) and isinstance(clean, str)
        assert len(clean) > 0
    else:
        print(f"PDF sample not found: {sample_path}")
