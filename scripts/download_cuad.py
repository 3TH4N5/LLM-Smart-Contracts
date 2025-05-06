# scripts/download_cuad.py
import os
import json
import shutil
import pandas as pd
import sys
import subprocess

# Check if required packages are installed
required_packages = ["datasets", "pandas", "tqdm"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

from datasets import load_dataset
from tqdm import tqdm


def download_cuad_dataset():
    """
    Download the CUAD dataset and organize it in the project structure.
    """
    print("Downloading CUAD dataset...")

    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cuad_dir = os.path.join(base_dir, "data", "raw", "contracts", "cuad")
    train_dir = os.path.join(cuad_dir, "train")
    test_dir = os.path.join(cuad_dir, "test")
    annotations_dir = os.path.join(cuad_dir, "annotations")

    # Ensure directories exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(annotations_dir, exist_ok=True)

    # Load the CUAD dataset from Hugging Face
    try:
        print("Loading CUAD dataset from Hugging Face...")
        dataset = load_dataset("cuad")

        # Process the dataset
        train_data = dataset["train"]
        test_data = dataset["validation"]  # Note: CUAD uses "validation" as test set

        # Save contract texts
        print("Saving contract documents...")

        # Process training set
        for i, example in enumerate(tqdm(train_data)):
            contract_id = f"train_{i:04d}"
            contract_text = example["contract_text"]

            # Save contract text
            with open(
                os.path.join(train_dir, f"{contract_id}.txt"), "w", encoding="utf-8"
            ) as f:
                f.write(contract_text)

            # Save annotations
            annotations = []
            for clause_idx, has_clause in enumerate(example["labels"]):
                if has_clause == 1:
                    clause_type = train_data.features["labels"].feature.names[
                        clause_idx
                    ]
                    clause_text = example["excerpts"][clause_idx]

                    if clause_text:  # Some annotations might be empty
                        annotations.append(
                            {"clause_type": clause_type, "text": clause_text}
                        )

            # Save annotations as JSON
            with open(
                os.path.join(annotations_dir, f"{contract_id}_annotations.json"),
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(annotations, f, indent=2)

        # Process test set
        for i, example in enumerate(tqdm(test_data)):
            contract_id = f"test_{i:04d}"
            contract_text = example["contract_text"]

            # Save contract text
            with open(
                os.path.join(test_dir, f"{contract_id}.txt"), "w", encoding="utf-8"
            ) as f:
                f.write(contract_text)

            # Save annotations
            annotations = []
            for clause_idx, has_clause in enumerate(example["labels"]):
                if has_clause == 1:
                    clause_type = test_data.features["labels"].feature.names[clause_idx]
                    clause_text = example["excerpts"][clause_idx]

                    if clause_text:  # Some annotations might be empty
                        annotations.append(
                            {"clause_type": clause_type, "text": clause_text}
                        )

            # Save annotations as JSON
            with open(
                os.path.join(annotations_dir, f"{contract_id}_annotations.json"),
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(annotations, f, indent=2)

    except Exception as e:
        print(f"Error downloading CUAD dataset from Hugging Face: {str(e)}")
        print(
            "You may need to download it manually from: https://github.com/TheAtticusProject/cuad"
        )
        return False

    # Create a catalog of available contracts
    create_contract_catalog(cuad_dir)

    print(f"CUAD dataset successfully downloaded and processed!")
    print(f"- Training contracts: {len(train_data)}")
    print(f"- Test contracts: {len(test_data)}")
    print(f"- Total contracts: {len(train_data) + len(test_data)}")
    return True


def create_contract_catalog(cuad_dir):
    """Create a catalog CSV of available contracts and their clause types."""
    train_dir = os.path.join(cuad_dir, "train")
    test_dir = os.path.join(cuad_dir, "test")
    annotations_dir = os.path.join(cuad_dir, "annotations")

    catalog_data = []

    # Process training contracts
    for filename in os.listdir(train_dir):
        if filename.endswith(".txt"):
            contract_id = os.path.splitext(filename)[0]
            annotation_file = os.path.join(
                annotations_dir, f"{contract_id}_annotations.json"
            )

            if os.path.exists(annotation_file):
                with open(annotation_file, "r", encoding="utf-8") as f:
                    annotations = json.load(f)

                clause_types = [a["clause_type"] for a in annotations]

                catalog_data.append(
                    {
                        "contract_id": contract_id,
                        "split": "train",
                        "file_path": os.path.join(train_dir, filename),
                        "annotation_path": annotation_file,
                        "clause_count": len(annotations),
                        "clause_types": ", ".join(clause_types),
                    }
                )

    # Process test contracts
    for filename in os.listdir(test_dir):
        if filename.endswith(".txt"):
            contract_id = os.path.splitext(filename)[0]
            annotation_file = os.path.join(
                annotations_dir, f"{contract_id}_annotations.json"
            )

            if os.path.exists(annotation_file):
                with open(annotation_file, "r", encoding="utf-8") as f:
                    annotations = json.load(f)

                clause_types = [a["clause_type"] for a in annotations]

                catalog_data.append(
                    {
                        "contract_id": contract_id,
                        "split": "test",
                        "file_path": os.path.join(test_dir, filename),
                        "annotation_path": annotation_file,
                        "clause_count": len(annotations),
                        "clause_types": ", ".join(clause_types),
                    }
                )

    # Create a DataFrame and save to CSV
    catalog_df = pd.DataFrame(catalog_data)
    catalog_file = os.path.join(cuad_dir, "contract_catalog.csv")
    catalog_df.to_csv(catalog_file, index=False)
    print(f"Contract catalog created: {catalog_file}")


if __name__ == "__main__":
    download_cuad_dataset()
