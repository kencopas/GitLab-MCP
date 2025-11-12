from typing import Optional, Literal

import requests
from config.config import GITLAB_URL, GITLAB_API_PAT


def gitlab_request(method: Literal['GET', 'POST', 'PUT', 'DELETE'], endpoint: str, params: Optional[dict] = None) -> dict:
    """Helper function to perform requests to the GitLab API.
    
    Args:
        method (str): HTTP method ('GET', 'POST', 'PUT', or 'DELETE').
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
        case "PUT":
            response = requests.put(url, headers=headers, json=params)
        case "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        case _:
            raise ValueError("Invalid HTTP method")

    response.raise_for_status()

    # Handle empty responses (common with DELETE requests)
    if not response.content:
        return {}

    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON response"}


def validate_labels(project_id, labels) -> None:
    """Validate that the labels in the payload exist in the project."""
    labels_response = gitlab_request("GET", f"/projects/{project_id}/labels")
    existing_labels = {label['name'] for label in labels_response}

    if any(label not in existing_labels for label in labels):
        invalid_labels = [label for label in labels if label not in existing_labels]
        raise ValueError(f"Invalid labels: {', '.join(invalid_labels)}. Please use existing project labels: {', '.join(existing_labels)}")
