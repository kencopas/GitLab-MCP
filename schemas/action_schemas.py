# Output schema for deleting an issue
from pydantic import BaseModel, Field, HttpUrl, AnyUrl
from typing import Optional, List, Dict, Any, Union, Literal, Tuple
from datetime import datetime


class CreateIssueRequest(BaseModel):
    project_id: str | int = Field(..., description="Project ID or URL-encoded path of the project")
    title: str = Field(..., description="Title of the issue")

    # Optional fields
    assignee_id: Optional[int] = None
    assignee_ids: Optional[List[int]] = None
    confidential: Optional[bool] = False
    created_at: Optional[str] = None  # ISO 8601 format
    description: Optional[str] = None
    discussion_to_resolve: Optional[str] = None
    due_date: Optional[str] = None  # YYYY-MM-DD
    epic_id: Optional[int] = None
    epic_iid: Optional[int] = None
    iid: Optional[int | str] = None
    issue_type: Optional[str] = Field("issue", description="One of issue, incident, test_case, or task")
    labels: Optional[str] = None
    merge_request_to_resolve_discussions_of: Optional[int] = None
    milestone_id: Optional[int] = None
    weight: Optional[int] = None


# Input schema for editing an issue
class EditIssueRequest(BaseModel):
    project_id: str | int = Field(..., description="Project ID or URL-encoded path of the project")
    issue_iid: int | str = Field(..., description="Issue IID or ID")

    # Editable fields
    title: Optional[str] = None
    description: Optional[str] = None
    confidential: Optional[bool] = None
    discussion_to_resolve: Optional[str] = None
    due_date: Optional[str] = None  # YYYY-MM-DD
    labels: Optional[str] = None
    milestone_id: Optional[int] = None
    weight: Optional[int] = None
    assignee_id: Optional[int] = None
    assignee_ids: Optional[List[int]] = None
    state_event: Optional[str] = Field(None, description="close or reopen")
    issue_type: Optional[str] = Field(None, description="One of issue, incident, test_case, or task")
    epic_id: Optional[int] = None
    epic_iid: Optional[int] = None
    merge_request_to_resolve_discussions_of: Optional[int] = None


class Author(BaseModel):
    id: int
    name: str
    username: str
    state: str
    web_url: HttpUrl
    avatar_url: Optional[HttpUrl]

class References(BaseModel):
    short: str
    relative: str
    full: str

class TimeStats(BaseModel):
    time_estimate: int
    total_time_spent: int
    human_time_estimate: Optional[str]
    human_total_time_spent: Optional[str]

class Links(BaseModel):
    self: HttpUrl
    notes: HttpUrl
    award_emoji: HttpUrl
    project: HttpUrl
    closed_as_duplicate_of: Optional[HttpUrl]

class TaskCompletionStatus(BaseModel):
    count: int
    completed_count: int

class Epic(BaseModel):
    id: int
    iid: int
    title: str
    url: str
    group_id: int

class CreateIssueResponse(BaseModel):
    id: int
    iid: int
    project_id: int
    title: str
    description: Optional[str]
    state: str
    created_at: str
    updated_at: str
    closed_at: Optional[str]
    confidential: bool
    issue_type: str
    labels: List[str]
    author: Author
    web_url: HttpUrl
    references: References
    time_stats: TimeStats
    _links: Links
    task_completion_status: TaskCompletionStatus
    epic: Optional[Epic] = None
    weight: Optional[int] = None
    due_date: Optional[str] = None
    severity: Optional[str] = None
    merge_requests_count: Optional[int] = None

    assignees: Optional[List[Author]] = None


# Input schema for creating a merge request
class CreateMergeRequestRequest(BaseModel):
    project_id: str | int = Field(..., description="Project ID or URL-encoded path of the project")
    source_branch: str = Field(..., description="The source branch.")
    target_branch: str = Field(..., description="The target branch.")
    title: str = Field(..., description="Title of MR.")
    allow_collaboration: Optional[bool] = None
    approvals_before_merge: Optional[int] = None
    allow_maintainer_to_push: Optional[bool] = None
    assignee_id: Optional[int] = None
    assignee_ids: Optional[List[int]] = None
    description: Optional[str] = None
    labels: Optional[str] = None
    merge_after: Optional[str] = None
    milestone_id: Optional[int] = None
    remove_source_branch: Optional[bool] = None
    reviewer_ids: Optional[List[int]] = None
    squash: Optional[bool] = None
    target_project_id: Optional[int] = None

# Output schema for the response
from schemas.info_schemas import MergeRequest
CreateMergeRequestResponse = MergeRequest
