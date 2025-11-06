from pydantic import BaseModel, Field, HttpUrl, AnyUrl
from typing import Optional, List, Dict, Any, Union, Literal, Tuple, Self
from datetime import datetime


class ProjectDetails(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    web_url: Optional[str] = None
    created_at: Optional[str] = None
    last_activity_at: Optional[str] = None
    visibility: Optional[str] = None


class User(BaseModel):
    id: int
    username: str
    public_email: Optional[str] = None
    name: Optional[str] = None
    state: Optional[Literal["active", "blocked", "deactivated", "ldap_blocked", "banned"] | str] = None
    locked: Optional[bool] = None
    avatar_url: Optional[str] = None
    web_url: Optional[HttpUrl] = None


class Milestone(BaseModel):
    id: int
    iid: int
    project_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    state: Optional[Literal["active", "closed"] | str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    expired: Optional[bool] = None
    web_url: Optional[HttpUrl] = None


class TimeStats(BaseModel):
    time_estimate: Optional[int] = None
    total_time_spent: Optional[int] = None
    human_time_estimate: Optional[str] = None
    human_total_time_spent: Optional[str] = None


class TaskCompletionStatus(BaseModel):
    count: Optional[int] = None
    completed_count: Optional[int] = None


class Links(BaseModel):
    self: Optional[HttpUrl] = None
    notes: Optional[HttpUrl] = None
    award_emoji: Optional[HttpUrl] = None
    project: Optional[HttpUrl] = None
    closed_as_duplicate_of: Optional[HttpUrl] = None


class References(BaseModel):
    short: Optional[str] = None
    relative: Optional[str] = None
    full: Optional[str] = None


class Issue(BaseModel):
    id: int
    iid: int
    project_id: int

    title: str
    description: Optional[str] = None

    state: Optional[Literal["opened", "closed"] | str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None

    closed_by: Optional[User] = None
    author: Optional[User] = None
    assignees: Optional[List[User]] = Field(default_factory=list)
    assignee: Optional[User] = None

    labels: Optional[List[str]] = Field(default_factory=list)
    milestone: Optional[Milestone] = None
    type: Optional[Literal["ISSUE"] | str] = None
    issue_type: Optional[Literal["issue", "incident", "test_case", "task"] | str] = None

    user_notes_count: Optional[int] = None
    merge_requests_count: Optional[int] = None
    upvotes: Optional[int] = None
    downvotes: Optional[int] = None

    due_date: Optional[datetime] = None
    confidential: Optional[bool] = None
    discussion_locked: Optional[bool] = None

    web_url: Optional[HttpUrl] = None
    _links: Optional[Links] = None
    references: Optional[References] = None

    time_stats: Optional[TimeStats] = None
    task_completion_status: Optional[TaskCompletionStatus] = None
    blocking_issues_count: Optional[int] = None
    has_tasks: Optional[bool] = None
    task_status: Optional[str] = None

    severity: Optional[str] = None
    moved_to_id: Optional[int] = None
    imported: Optional[bool] = None
    imported_from: Optional[str] = None
    service_desk_reply_to: Optional[str] = None

    class Config:
        anystr_strip_whitespace = False
        use_enum_values = True


class IssueList(BaseModel):
    issues: List[Issue] = Field(default_factory=list)


class Namespace(BaseModel):
    id: int
    name: Optional[str] = None
    path: Optional[str] = None
    kind: Optional[str] = None
    full_path: Optional[str] = None
    parent_id: Optional[int] = None
    avatar_url: Optional[str] = None
    web_url: Optional[HttpUrl] = None


class Project(BaseModel):
    id: int
    description: Optional[str] = None
    name: Optional[str] = None
    name_with_namespace: Optional[str] = None
    path: Optional[str] = None
    path_with_namespace: Optional[str] = None
    created_at: Optional[datetime] = None
    default_branch: Optional[str] = None
    tag_list: Optional[List[str]] = Field(default_factory=list)
    topics: Optional[List[str]] = Field(default_factory=list)
    ssh_url_to_repo: Optional[str] = None
    http_url_to_repo: Optional[HttpUrl] = None
    web_url: Optional[HttpUrl] = None
    avatar_url: Optional[str] = None
    star_count: Optional[int] = None
    last_activity_at: Optional[datetime] = None
    visibility: Optional[str] = None
    namespace: Optional[Namespace] = None

    class Config:
        anystr_strip_whitespace = False
        use_enum_values = True


class ProjectList(BaseModel):
    projects: List[Project] = Field(default_factory=list)
