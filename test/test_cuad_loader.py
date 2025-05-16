# tests/test_cuad_loader.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pathlib import Path
from src.utils.cuad_loader import load_cuad, sample_cuad_entries


def test_load_cuad():
    sample_file = Path("tests/sample_data/cuad_sample.json")
    if sample_file.exists():
        entries = load_cuad(sample_file)
        assert isinstance(entries, list)
        assert len(entries) > 0
        assert all(
            "question" in e and "answer" in e and "context" in e for e in entries
        )
    else:
        print(f"[SKIPPED] CUAD sample not found: {sample_file}")


def test_sample_output():
    sample_file = Path("tests/sample_data/cuad_sample.json")
    if sample_file.exists():
        entries = load_cuad(sample_file)
        samples = sample_cuad_entries(entries, n=3)
        assert isinstance(samples, list)
        assert all(isinstance(s, tuple) and len(s) == 3 for s in samples)
        print("\nSample Questions:")
        for q, a, ctx in samples:
            print(f"Q: {q}\nA: {a}\n---")
    else:
        print(f"[SKIPPED] CUAD sample not found: {sample_file}")
