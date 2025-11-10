from schemas.info_schemas import Issue, ProjectDetails, IssueList, ProjectList, Project
from server import mcp
from services.gitlab_api import gitlab_request


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
