import os
import zipfile
import requests
import shutil
from tqdm import tqdm


# ----------------------------
# Download a file
# ----------------------------
def download_file_from_url(url, dest_path):
    """
    Downloads a file from the given URL to the destination path with a tqdm progress bar.
    """
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with open(dest_path, "wb") as file, tqdm(
        desc=f"Downloading {os.path.basename(dest_path)}",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(1024):
            file.write(data)
            bar.update(len(data))


# ----------------------------
# Extract a zip archive
# ----------------------------
def extract_zip(zip_path, extract_to):
    """
    Extracts the contents of a ZIP file to the specified directory.
    """
    print(f"Extracting {os.path.basename(zip_path)} to {extract_to}...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)


# ----------------------------
# Main function to download and prepare CUAD
# ----------------------------
def setup_cuad_dataset():
    """
    Downloads the CUAD dataset from GitHub, extracts it,
    flattens the structure, and removes unnecessary files.
    """
    # Define paths
    base_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )  # Go one level up from /scripts
    contracts_dir = os.path.join(base_dir, "data", "raw", "contracts")
    cuad_dir = os.path.join(contracts_dir, "cuad")
    os.makedirs(cuad_dir, exist_ok=True)

    # Define GitHub zip URL and download path
    github_zip_url = (
        "https://github.com/TheAtticusProject/cuad/archive/refs/heads/main.zip"
    )
    github_zip_path = os.path.join(cuad_dir, "cuad_repo.zip")

    try:
        # Step 1: Download CUAD GitHub repository ZIP
        print("[STEP 1] Downloading CUAD repository...")
        download_file_from_url(github_zip_url, github_zip_path)

        # Step 2: Extract ZIP to cuad_dir
        print("[STEP 2] Extracting CUAD repository ZIP...")
        extract_zip(github_zip_path, cuad_dir)
        os.remove(github_zip_path)  # Delete ZIP after extraction

        # Locate the extracted repo folder (cuad-main)
        extracted_repo_dir = os.path.join(cuad_dir, "cuad-main")

        # Step 3: Move category_descriptions.csv to main CUAD folder
        print("[STEP 3] Flattening and keeping relevant files...")
        shutil.move(
            os.path.join(extracted_repo_dir, "category_descriptions.csv"),
            os.path.join(cuad_dir, "category_descriptions.csv"),
        )

        # Step 4: Extract 'data.zip' inside the repo
        data_zip_path = os.path.join(extracted_repo_dir, "data.zip")
        cuad_data_dir = os.path.join(cuad_dir, "cuad_data")
        os.makedirs(cuad_data_dir, exist_ok=True)

        if not os.path.exists(data_zip_path):
            raise FileNotFoundError(f"'data.zip' not found in {extracted_repo_dir}")

        print("[STEP 4] Extracting CUAD data.zip...")
        extract_zip(data_zip_path, cuad_data_dir)

        # Step 5: Clean up everything except 'cuad_data' and CSV
        print("[STEP 5] Cleaning up non-essential files...")
        shutil.rmtree(extracted_repo_dir)  # Goodbye, repo clutter

        print("[DONE] CUAD dataset is ready for action.")
        print(f"-> Data folder: {cuad_data_dir}")
        print(f"-> Metadata CSV: {os.path.join(cuad_dir, 'category_descriptions.csv')}")

    except Exception as e:
        print(f"[ERROR] Failed to setup CUAD dataset: {e}")
        print(
            "Try downloading manually from: https://github.com/TheAtticusProject/cuad"
        )


# ----------------------------
# Run script
# ----------------------------
if __name__ == "__main__":
    setup_cuad_dataset()
