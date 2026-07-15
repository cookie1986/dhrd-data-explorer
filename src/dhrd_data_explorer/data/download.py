from pathlib import Path
import subprocess


def download_zenodo_dataset(record_id: str, dest: Path | str = "dataset/") -> Path:
    """
    Download the DHRD dataset from Zenodo using the record ID.
    
    Args:
        record_id (str): The Zenodo record ID for this dataset
        dest (Path | str): The destination directory to save the downloaded dataset (defaults to "dataset/")
        
    Returns:
        Path: The path to the downloaded dataset directory
    
    Raises:
        subprocess.CalledProcessError: If the download command fails
    """

    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        ["zenodo_get", record_id, "-o", str(dest)],
        check=True
    )
    return dest