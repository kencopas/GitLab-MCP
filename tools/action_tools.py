from schemas.action_schemas import *
from schemas.info_schemas import Issue
from server import mcp
from services.gitlab_api import gitlab_request, validate_labels
from .info_tools import get_issue_details


@mcp.tool(title="Create GitLab Merge Request")
def create_merge_request(payload: CreateMergeRequestRequest) -> CreateMergeRequestResponse:
    """Create a new GitLab merge request in a specific project.

    Args:
        payload (CreateMergeRequestRequest): Parameters for the merge request, including required and optional fields

    Returns:
        CreateMergeRequestResponse: The created merge request object, matching the GitLab API response.
    """

    # Validate labels against existing project labels
    if payload.labels:
        labels_list = [label.strip() for label in payload.labels.split(',')]
        validate_labels(payload.project_id, labels_list)

    mr_data = payload.model_dump(exclude={'project_id'}, exclude_none=True)
    response = gitlab_request("POST", f"/projects/{payload.project_id}/merge_requests", params=mr_data)

    return CreateMergeRequestResponse(**response)


@mcp.tool(title="Create GitLab Issue")
def create_issue(payload: CreateIssueRequest) -> CreateIssueResponse:
    """Create a new GitLab issue in a specific project."""

    # Validate labels against existing project labels
    if payload.labels:
        labels_list = [label.strip() for label in payload.labels.split(',')]
        validate_labels(payload.project_id, labels_list)
    
    if payload.iid:
        try:
            existing_issue = get_issue_details(payload.project_id, payload.iid)
            raise ValueError(f"Issue with IID {payload.iid} already exists in project {payload.project_id}.")
        except Exception:
            pass  # Issue does not exist, proceed to create

    issue_info_data = payload.model_dump(exclude={'project_id'}, exclude_none=True)
    response = gitlab_request("POST", f"/projects/{payload.project_id}/issues", params=issue_info_data)

    return CreateIssueResponse(**response)


@mcp.tool(title="Edit GitLab Issue")
def edit_issue(payload: EditIssueRequest) -> Issue:
    """Edit an existing GitLab issue in a specific project."""

    # Validate labels against existing project labels
    if payload.labels:
        labels_list = [label.strip() for label in payload.labels.split(',')]
        validate_labels(payload.project_id, labels_list)

    issue_info_data = payload.model_dump(exclude={'project_id', 'issue_iid'}, exclude_none=True)
    response = gitlab_request("PUT", f"/projects/{payload.project_id}/issues/{payload.issue_iid}", params=issue_info_data)

    return Issue(**response)


@mcp.tool(title="Delete GitLab Issue")
def delete_issue(project_id: int, issue_iid: int) -> dict:
    """Delete an existing GitLab issue in a specific project. Only for administrators and project owners."""
    
    response = gitlab_request("DELETE", f"/projects/{project_id}/issues/{issue_iid}")
    success = response is None or response == ''
    
    return {"success": success}
