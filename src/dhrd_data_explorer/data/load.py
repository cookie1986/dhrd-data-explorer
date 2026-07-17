import pandas as pd
from pathlib import Path
from zipfile import ZipFile
import subprocess
import streamlit as st

def find_file(directory: Path, filename: str) -> Path:
    """Recursive search through directory."""
    matches = list(directory.rglob(filename))

    # Error handling
    if not matches:
        available = [
            str(path.relative_to(directory)) for path in directory.rglob("*") if path.is_file()
        ]
        raise FileNotFoundError(
            f"{filename!r} not found. Available files: {available}."
        )
    
    if len(matches) > 1:
        raise RuntimeError(
            f"Multiple files named {filename!r} found: {matches}"
        )
    
    return matches[0]


@st.cache_data
def load_data(record_id: str) -> dict[str, pd.DataFrame]:
    # File setup
    download_dir = Path("/tmp") / f"zenodo-{record_id}"
    extract_dir = download_dir / "extracted"

    download_dir.mkdir(parents=True, exist_ok=True)
    extract_dir.mkdir(parents=True, exist_ok=True)

    # API call
    subprocess.run(
        ["zenodo_get", record_id, "-o", str(download_dir)],
        check=True,
        capture_output=True,
        text=True
    )
    archives = list(download_dir.glob("*.zip"))

    # Error handling
    if not archives:
        raise FileNotFoundError(
            f"No Zip file found in {download_dir}"
        )
    if len(archives) > 1:
        raise RuntimeError(
            f"Multiple Zip files found in {archives}"
        )
    
    # Extract
    with ZipFile(archives[0]) as archive:
        archive.extractall(extract_dir)

    return {
        "documents": pd.read_csv(
            find_file(extract_dir, "documents.csv")
        ),
        "incidents": pd.read_csv(
            find_file(extract_dir, "incidents.csv")
        ),
        "victims": pd.read_csv(
            find_file(extract_dir, "victims.csv")
        ),
        "perpetrators": pd.read_csv(
            find_file(extract_dir, "perpetrators.csv")
        )
    }
    