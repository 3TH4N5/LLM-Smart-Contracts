# src/utils/cuad_loader.py
import json
from pathlib import Path
from typing import List, Dict, Tuple


def load_cuad(filepath: Path) -> List[Dict]:
    """
    Load CUAD dataset and return a list of entries.

    Each entry contains:
    - document title
    - question text
    - answer string
    - answer_start index
    - full context (clause)
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    parsed = []
    for doc in data:
        doc_name = doc.get("doc_name") or doc.get("title")
        questions = doc.get("qas", [])
        context = doc.get("context", "")

        for qa in questions:
            parsed.append(
                {
                    "doc": doc_name,
                    "question": qa["question"],
                    "answer": qa["answer"],
                    "answer_start": qa.get("answer_start", -1),
                    "context": context,
                }
            )

    return parsed


def sample_cuad_entries(entries: List[Dict], n: int = 5) -> List[Tuple[str, str, str]]:
    """
    Return a few samples as (question, answer, context) tuples for inspection or testing.
    """
    return [(e["question"], e["answer"], e["context"]) for e in entries[:n]]
