from schemas.action_schemas import CreateIssueRequest, CreateIssueResponse, EditIssueRequest
from schemas.info_schemas import Issue
from server import mcp
from services.gitlab_api import gitlab_request

"""
ATTENTION:

Need to add the ability to list the available issue labels for a project so that they aren't created out of thin air.
This can be done by calling the GET /projects/:id/labels endpoint from the GitLab API.
"""


@mcp.tool(title="Create GitLab Issue")
def create_issue(payload: CreateIssueRequest) -> CreateIssueResponse:
    """Create a new GitLab issue in a specific project."""

    issue_info_data = payload.model_dump(exclude={'project_id'}, exclude_none=True)
    response = gitlab_request("POST", f"/projects/{payload.project_id}/issues", params=issue_info_data)

    return CreateIssueResponse(**response)


@mcp.tool(title="Edit GitLab Issue")
def edit_issue(payload: EditIssueRequest) -> Issue:
    """Edit an existing GitLab issue in a specific project."""

    issue_info_data = payload.model_dump(exclude={'project_id', 'issue_iid'}, exclude_none=True)
    response = gitlab_request("PUT", f"/projects/{payload.project_id}/issues/{payload.issue_iid}", params=issue_info_data)

    return Issue(**response)


@mcp.tool(title="Delete GitLab Issue")
def delete_issue(project_id: int, issue_iid: int) -> dict:
    """Delete an existing GitLab issue in a specific project. Only for administrators and project owners."""
    
    response = gitlab_request("DELETE", f"/projects/{project_id}/issues/{issue_iid}")
    success = response is None or response == ''
    
    return {"success": success}
