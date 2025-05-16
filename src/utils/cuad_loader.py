# src/utils/cuad_loader.py
import json
from pathlib import Path
from typing import List, Dict, Tuple


def load_cuad(filepath: Path) -> List[Dict]:
    """
    Load CUAD (SQuAD-style) format.
    Extract document title, question, first answer, and context.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    parsed = []
    for doc in data["data"]:  # this is correct
        title = doc.get("title", "unknown_title")
        for para in doc.get("paragraphs", []):
            context = para.get("context", "")
            for qa in para.get("qas", []):
                if qa.get("answers"):
                    answer = qa["answers"][0]["text"]
                    answer_start = qa["answers"][0]["answer_start"]
                else:
                    answer = ""
                    answer_start = -1

                parsed.append(
                    {
                        "doc": title,
                        "question": qa["question"],
                        "answer": answer,
                        "answer_start": answer_start,
                        "context": context,
                    }
                )

    return parsed


def sample_cuad_entries(entries: List[Dict], n: int = 5) -> List[Tuple[str, str, str]]:
    """
    Return a few samples as (question, answer, context) tuples for inspection or testing.
    """
    return [(e["question"], e["answer"], e["context"]) for e in entries[:n]]
