import requests
import streamlit as st

@st.cache_data
def get_latest_version(record_id: str, timeout: float = 30) -> str | None:
    """
    Fetch the latest version string for the DHRD via REST API.

    Args:
        record_id (str): The Zenodo record ID for the DHRD
        timeout (float): Request timeout in seconds (default is 30)
    
    Returns:
        str | None: The version string of the dataset as recorded by 
        the Zenodo API, or None if the record has no version set.
    
    Raises:
        requests.HTTPError: If the API request fails.
    """

    response = requests.get(
        f"https://zenodo.org/api/records/{record_id}",
        timeout=timeout,
    )
    response.raise_for_status()
    metadata = response.json().get("metadata", {})
    return metadata.get("version")