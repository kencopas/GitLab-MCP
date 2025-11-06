import os

import requests
from rich import print_json

from schemas import Issue, ProjectDetails, IssueList, ProjectList, Project
from server import mcp
from config.constants import GITLAB_URL


GITLAB_API_PAT = os.getenv("GITLAB_API_PAT")


@mcp.tool(title="List Projects")
def list_projects() -> ProjectList:
    """List all projects accessible by the user."""
    response = requests.get(
        f"{GITLAB_URL}/api/v4/projects",
        headers={"Authorization": f"Bearer {GITLAB_API_PAT}"}
    )

    response.raise_for_status()
    data = response.json()

    return ProjectList(projects=[Project(**project) for project in data])


@mcp.tool(title="Get Project Details")
def get_project_details(project_id: int) -> ProjectDetails:
    """Get details of a specific project."""
    response = requests.get(
        f"{GITLAB_URL}/api/v4/projects/{project_id}",
        headers={"Authorization": f"Bearer {GITLAB_API_PAT}"}
    )

    response.raise_for_status()
    data = response.json()

    return ProjectDetails(**data)


@mcp.tool(title="List Project Issues")
def list_project_issues(project_id: int):
    """List issues for a specific project."""
    response = requests.get(
        f"{GITLAB_URL}/api/v4/projects/{project_id}/issues",
        headers={"Authorization": f"Bearer {GITLAB_API_PAT}"}
    )

    # response.raise_for_status()
    data = response.json()

    return IssueList(issues=[Issue(**issue) for issue in data])
