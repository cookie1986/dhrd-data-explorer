import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dhrd_data_explorer.data.download import download_zenodo_dataset

DHRD_RECORD_ID = "10.5281/zenodo.21108267"

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record-id",
        default=DHRD_RECORD_ID,
        help="Zenodo record ID for the DHRD dataset (default: %(default)s)"
    )
    parser.add_argument(
        "--dest",
        default="dataset/",
        help="Destination directory to save the downloaded dataset (default %(default)s)"
    )
    args = parser.parse_args()

    dest = download_zenodo_dataset(args.record_id, args.dest)
    print(f"Downloaded record {args.record_id} to {dest.resolve()}")

if __name__ == "__main__":
    main()