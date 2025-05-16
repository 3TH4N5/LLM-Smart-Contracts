# run_preprocessing.py
"""
This script handles raw contract files (PDF and DOCX),
extracts their text, cleans it, and saves the outputs
for use in NLP pipelines. It does NOT handle CUAD JSON data.
"""

import os
from pathlib import Path
from src.pre_processing import route_file  # Our unified extraction + cleaner


def collect_files(input_dir, valid_exts={".pdf", ".docx"}):
    """
    Recursively collect all files from input_dir that have the correct extensions.
    This supports large nested directories.
    """
    all_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in valid_exts:
                all_files.append(Path(root) / file)
    return all_files


def ensure_dir(path):
    """
    Create the output directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


def preprocess_all(raw_root, output_raw_dir, output_clean_dir):
    """
    Main pipeline function. Walks through all valid files in raw_root,
    applies extraction and cleaning, and saves outputs to the processed folders.
    """
    files = collect_files(raw_root)
    if not files:
        print("[!] No valid files found to process.")
        return

    ensure_dir(output_raw_dir)
    ensure_dir(output_clean_dir)

    for file_path in files:
        name = file_path.stem.replace(" ", "_").lower()

        print(f"[*] Processing: {file_path}")
        try:
            # Step 1: Extract raw and clean text using the router
            raw_text, cleaned_text = route_file(file_path)

            # Step 2: Define output file paths
            raw_out = output_raw_dir / f"{name}.txt"
            clean_out = output_clean_dir / f"{name}_cleaned.txt"

            # Step 3: Save the outputs
            raw_out.write_text(raw_text, encoding="utf-8")
            clean_out.write_text(cleaned_text, encoding="utf-8")

            print(f"    └─ Saved: {raw_out.name}, {clean_out.name}")

        except Exception as e:
            print(f"[ERROR] Failed to process {file_path}: {e}")


if __name__ == "__main__":
    # Define input/output paths
    raw_root = Path("data/raw/contracts")  # Folder with your PDFs and DOCXs
    output_raw_dir = Path("data/processed/extracted_text")
    output_clean_dir = Path("data/processed/cleaned_text")

    # Run the full preprocessing step
    preprocess_all(raw_root, output_raw_dir, output_clean_dir)
