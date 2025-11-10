from typing import Optional, Literal

import requests
from config.config import GITLAB_URL, GITLAB_API_PAT


def gitlab_request(method: Literal['GET', 'POST'], endpoint: str, params: Optional[dict] = None) -> dict:
    """Helper function to perform requests to the GitLab API.
    
    Args:
        method (str): HTTP method ('GET' or 'POST').
        endpoint (str): API endpoint (e.g., '/projects').
        params (dict, optional): Parameters to include in the request.
    
    Returns:
        dict: JSON response from the API.

    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
        ValueError: If invalid HTTP method is provided.
    """
    url = f"{GITLAB_URL}/api/v4/{endpoint.lstrip('/')}"
    headers = {"Authorization": f"Bearer {GITLAB_API_PAT}"}

    match method:
        case "GET":
            response = requests.get(url, headers=headers, params=params)
        case "POST":
            response = requests.post(url, headers=headers, json=params)
        case _:
            raise ValueError("Invalid HTTP method")

    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON response"}
