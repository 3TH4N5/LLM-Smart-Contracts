# tests/test_cuad_loader.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pathlib import Path
from src.utils.cuad_loader import load_cuad, sample_cuad_entries


def test_load_cuad():
    sample_path = Path("test/sample_data/cuad_sample.json")
    entries = load_cuad(sample_path)
    assert isinstance(entries, list)
    assert len(entries) > 0
    assert all("question" in e and "answer" in e and "context" in e for e in entries)


def test_sample_output():
    sample_path = Path("test/sample_data/cuad_sample.json")
    entries = load_cuad(sample_path)
    samples = sample_cuad_entries(entries, n=3)
    assert all(isinstance(s, tuple) and len(s) == 3 for s in samples)
    for q, a, c in samples:
        print(f"Q: {q}\nA: {a}\n---")
