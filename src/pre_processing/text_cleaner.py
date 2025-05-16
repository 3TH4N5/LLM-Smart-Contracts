import re


def clean_text(text):
    """Clean and normalize text for NLP processing."""
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Page \d+ of \d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"CONFIDENTIAL|DRAFT|EXHIBIT [A-Z]", "", text, flags=re.IGNORECASE)
    return text.strip()
