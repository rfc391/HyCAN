
import requests

def fetch_data_from_api(api_url, params=None):
    """Fetches data from the specified API endpoint."""
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching data from API: {e}")

def fetch_example_data():
    """Fetches example data from a public API (JSON Placeholder)."""
    api_url = "https://jsonplaceholder.typicode.com/posts"
    return fetch_data_from_api(api_url)
