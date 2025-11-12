from schemas.info_schemas import *
from server import mcp
from services.gitlab_api import gitlab_request


@mcp.tool(title="List GitLab Project Repository Branches")
def list_project_repository_branches(payload: ListBranchesRequest) -> BranchList:
    """
    List repository branches for a GitLab project, with optional regex or search filtering.

    Args:
        payload (ListBranchesRequest):
            - project_id (str|int): Project ID or URL-encoded path of the project (required)
            - regex (str): Return branches matching a re2 regex (optional)
            - search (str): Return branches containing the search string (optional)

    Returns:
        BranchList: List of branches with detailed info, including protection, merge status, and commit details.
    """
    params = payload.model_dump(exclude={'project_id'}, exclude_none=True)
    response = gitlab_request("GET", f"/projects/{payload.project_id}/repository/branches", params=params)
    return BranchList(branches=[BranchInfo(**branch) for branch in response])


@mcp.tool(title="GitLab API Health Check")
def gitlab_api_health_check() -> dict:
    """Check the health of the GitLab API connection."""

    try:
        response = gitlab_request("GET", "/version")
        return {"status": "healthy", "version": response.get("version", "unknown")}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


@mcp.tool(title="List GitLab Projects")
def list_projects() -> ProjectList:
    """List all GitLab projects accessible by the user."""

    response = gitlab_request("GET", "/projects")

    return ProjectList(projects=[Project(**project) for project in response])


@mcp.tool(title="Get GitLab Project Details")
def get_project_details(project_id: int) -> ProjectDetails:
    """Get details of a specific GitLab project."""

    response = gitlab_request("GET", f"/projects/{project_id}")

    return ProjectDetails(**response)


@mcp.tool(title="List GitLab Project Issues")
def list_project_issues(project_id: int) -> IssueList:
    """List issues for a specific GitLab project."""

    response = gitlab_request("GET", f"/projects/{project_id}/issues")

    return IssueList(issues=[Issue(**issue) for issue in response])


@mcp.tool(title="Get GitLab Issue Details")
def get_issue_details(project_id: int, issue_iid: int) -> Issue:
    """Get details of a specific issue in a GitLab project."""

    response = gitlab_request("GET", f"/projects/{project_id}/issues/{issue_iid}")

    return Issue(**response)


@mcp.tool(title="List GitLab Project Merge Requests")
def list_project_merge_requests(payload: ListMergeRequestsRequest) -> MergeRequestList:
    """List all merge requests for a specific GitLab project with optional filtering."""
    
    # Convert the payload to query parameters, excluding project_id and None values
    params = payload.model_dump(exclude={'project_id'}, exclude_none=True)
    
    # Handle special formatting for iids parameter (needs to be iids[])
    if 'iids' in params and params['iids']:
        iids_list = params.pop('iids')
        for i, iid in enumerate(iids_list):
            params[f'iids[{i}]'] = iid
    
    response = gitlab_request("GET", f"/projects/{payload.project_id}/merge_requests", params=params)
    
    return MergeRequestList(merge_requests=[MergeRequest(**mr) for mr in response])


@mcp.tool(title="List GitLab Project Labels")
def list_project_labels(payload: ListLabelsRequest) -> LabelList:
    """List all labels for a specific GitLab project with optional filtering."""
    
    # Convert the payload to query parameters, excluding project_id and None values
    params = payload.model_dump(exclude={'project_id'}, exclude_none=True)
    
    response = gitlab_request("GET", f"/projects/{payload.project_id}/labels", params=params)
    
    return LabelList(labels=[Label(**label) for label in response])
