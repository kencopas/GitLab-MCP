from pydantic import BaseModel, Field, HttpUrl, AnyUrl
from typing import Optional, List, Dict, Any, Union, Literal, Tuple
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
    subscribed: Optional[bool] = None

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
        str_strip_whitespace = False
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
        str_strip_whitespace = False
        use_enum_values = True


class ProjectList(BaseModel):
    projects: List[Project] = Field(default_factory=list)


class MergeRequest(BaseModel):
    id: int
    iid: int
    project_id: int
    
    title: str
    description: Optional[str] = None
    
    state: Optional[Literal["opened", "closed", "merged", "locked"] | str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    prepared_at: Optional[datetime] = None
    
    author: Optional[User] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = Field(default_factory=list)
    reviewers: Optional[List[User]] = Field(default_factory=list)
    merged_by: Optional[User] = None  # Deprecated, use merge_user instead
    merge_user: Optional[User] = None
    closed_by: Optional[User] = None
    
    source_branch: Optional[str] = None
    target_branch: Optional[str] = None
    source_project_id: Optional[int] = None
    target_project_id: Optional[int] = None
    
    labels: Optional[List[str]] = Field(default_factory=list)
    milestone: Optional[Milestone] = None
    
    draft: Optional[bool] = None
    work_in_progress: Optional[bool] = None  # Deprecated, use draft instead
    
    merge_status: Optional[str] = None  # Deprecated, use detailed_merge_status instead
    detailed_merge_status: Optional[str] = None
    merge_when_pipeline_succeeds: Optional[bool] = None
    
    has_conflicts: Optional[bool] = None
    blocking_discussions_resolved: Optional[bool] = None
    discussion_locked: Optional[bool] = None
    
    upvotes: Optional[int] = None
    downvotes: Optional[int] = None
    user_notes_count: Optional[int] = None
    
    sha: Optional[str] = None
    merge_commit_sha: Optional[str] = None
    squash_commit_sha: Optional[str] = None
    
    should_remove_source_branch: Optional[bool] = None
    force_remove_source_branch: Optional[bool] = None
    squash: Optional[bool] = None
    squash_on_merge: Optional[bool] = None
    
    web_url: Optional[HttpUrl] = None
    reference: Optional[str] = None  # Deprecated, use references instead
    references: Optional[References] = None
    
    time_stats: Optional[TimeStats] = None
    task_completion_status: Optional[TaskCompletionStatus] = None
    
    approvals_before_merge: Optional[int] = None  # Premium and Ultimate only
    imported: Optional[bool] = None
    imported_from: Optional[str] = None
    
    class Config:
        str_strip_whitespace = False
        use_enum_values = True


class MergeRequestList(BaseModel):
    merge_requests: List[MergeRequest] = Field(default_factory=list)



class ListMergeRequestsRequest(BaseModel):
    project_id: str | int = Field(..., description="Project ID or URL-encoded path of the project")
    
    # Filter parameters
    approved_by_ids: Optional[List[int]] = Field(None, description="Returns merge requests approved by all the users with the given id, up to 5 users. Premium and Ultimate only.")
    approver_ids: Optional[List[int]] = Field(None, description="Returns merge requests which have specified all the users with the given id as individual approvers. Premium and Ultimate only.")
    assignee_id: Optional[int] = Field(None, description="Returns merge requests assigned to the given user id. None returns unassigned merge requests. Any returns merge requests with an assignee.")
    author_id: Optional[int] = Field(None, description="Returns merge requests created by the given user id. Mutually exclusive with author_username.")
    author_username: Optional[str] = Field(None, description="Returns merge requests created by the given username. Mutually exclusive with author_id.")
    created_after: Optional[str] = Field(None, description="Returns merge requests created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).")
    created_before: Optional[str] = Field(None, description="Returns merge requests created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).")
    environment: Optional[str] = Field(None, description="Returns merge requests deployed to the given environment.")
    iids: Optional[List[int]] = Field(None, description="Returns the request having the given iid.")
    labels: Optional[str] = Field(None, description="Returns merge requests matching a comma-separated list of labels. None lists all merge requests with no labels. Any lists all merge requests with at least one label.")
    merge_user_id: Optional[int] = Field(None, description="Returns merge requests merged by the user with the given user id. Mutually exclusive with merge_user_username.")
    merge_user_username: Optional[str] = Field(None, description="Returns merge requests merged by the user with the given username. Mutually exclusive with merge_user_id.")
    milestone: Optional[str] = Field(None, description="Returns merge requests for a specific milestone. None returns merge requests with no milestone. Any returns merge requests that have an assigned milestone.")
    my_reaction_emoji: Optional[str] = Field(None, description="Returns merge requests reacted by the authenticated user by the given emoji. None returns issues not given a reaction. Any returns issues given at least one reaction.")
    order_by: Optional[str] = Field("created_at", description="Returns requests ordered by created_at, title or updated_at fields. Default is created_at.")
    reviewer_id: Optional[int] = Field(None, description="Returns merge requests which have the user as a reviewer with the given user id. None returns merge requests with no reviewers. Any returns merge requests with any reviewer. Mutually exclusive with reviewer_username.")
    reviewer_username: Optional[str] = Field(None, description="Returns merge requests which have the user as a reviewer with the given username. Mutually exclusive with reviewer_id.")
    scope: Optional[str] = Field(None, description="Returns merge requests for the given scope: created_by_me, assigned_to_me, or all.")
    search: Optional[str] = Field(None, description="Search merge requests against their title and description.")
    sort: Optional[str] = Field("desc", description="Returns requests sorted in asc or desc order. Default is desc.")
    source_branch: Optional[str] = Field(None, description="Returns merge requests with the given source branch.")
    state: Optional[str] = Field(None, description="Returns all merge requests (all) or just those that are opened, closed, locked, or merged.")
    target_branch: Optional[str] = Field(None, description="Returns merge requests with the given target branch.")
    updated_after: Optional[str] = Field(None, description="Returns merge requests updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).")
    updated_before: Optional[str] = Field(None, description="Returns merge requests updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).")
    view: Optional[str] = Field(None, description="If simple, returns the iid, URL, title, description, and basic state of merge request.")
    wip: Optional[str] = Field(None, description="Filter merge requests against their wip status. yes to return only draft merge requests, no to return non-draft merge requests.")
    with_labels_details: Optional[bool] = Field(False, description="If true, response returns more details for each label in labels field. Default is false.")
    with_merge_status_recheck: Optional[bool] = Field(False, description="If true, this projection requests an asynchronous recalculation of the merge_status field. Default is false.")


class Label(BaseModel):
    id: int
    name: str
    color: str
    text_color: Optional[str] = None
    description: Optional[str] = None
    description_html: Optional[str] = None
    open_issues_count: Optional[int] = None
    closed_issues_count: Optional[int] = None
    open_merge_requests_count: Optional[int] = None
    subscribed: Optional[bool] = None
    priority: Optional[int] = None
    is_project_label: Optional[bool] = None
    archived: Optional[bool] = None


class LabelList(BaseModel):
    labels: List[Label]


class ListLabelsRequest(BaseModel):
    project_id: Union[str, int] = Field(description="Project ID or URL-encoded path of the project")
    with_counts: Optional[bool] = Field(False, description="Whether or not to include issue and merge request counts. Defaults to false.")
    include_ancestor_groups: Optional[bool] = Field(True, description="Include ancestor groups. Defaults to true.")
    search: Optional[str] = Field(None, description="Keyword to filter labels by.")
    archived: Optional[bool] = Field(None, description="Whether the label is archived. Returns all labels, when not set. Requires the labels_archive feature flag to be enabled.")

class CommitInfo(BaseModel):
    id: str
    short_id: str
    created_at: Optional[datetime] = None
    parent_ids: Optional[List[str]] = None
    title: Optional[str] = None
    message: Optional[str] = None
    author_name: Optional[str] = None
    author_email: Optional[str] = None
    authored_date: Optional[datetime] = None
    committer_name: Optional[str] = None
    committer_email: Optional[str] = None
    committed_date: Optional[datetime] = None
    trailers: Optional[Dict[str, Any]] = None
    extended_trailers: Optional[Dict[str, Any]] = None
    web_url: Optional[HttpUrl] = None

class BranchInfo(BaseModel):
    name: str
    merged: Optional[bool] = None
    protected: Optional[bool] = None
    default: Optional[bool] = None
    developers_can_push: Optional[bool] = None
    developers_can_merge: Optional[bool] = None
    can_push: Optional[bool] = None
    web_url: Optional[HttpUrl] = None
    commit: Optional[CommitInfo] = None

class ListBranchesRequest(BaseModel):
    project_id: Union[str, int] = Field(..., description="Project ID or URL-encoded path of the project")
    regex: Optional[str] = Field(None, description="Return branches matching a re2 regex.")
    search: Optional[str] = Field(None, description="Return branches containing the search string.")

class BranchList(BaseModel):
    branches: List[BranchInfo] = Field(default_factory=list)
    project_id: Union[str, int] = Field(description="Project ID or URL-encoded path of the project")
    with_counts: Optional[bool] = Field(False, description="Whether or not to include issue and merge request counts. Defaults to false.")
    include_ancestor_groups: Optional[bool] = Field(True, description="Include ancestor groups. Defaults to true.")
    search: Optional[str] = Field(None, description="Keyword to filter labels by.")
    archived: Optional[bool] = Field(None, description="Whether the label is archived. Returns all labels, when not set. Requires the labels_archive feature flag to be enabled.")
