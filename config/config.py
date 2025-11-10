import os

from dotenv import load_dotenv


load_dotenv()


GITLAB_API_PAT = os.getenv("GITLAB_API_PAT")
GITLAB_URL = os.getenv("GITLAB_URL", "https://gitlab.com").rstrip("/")

if not GITLAB_API_PAT:
    raise ValueError("GITLAB_API_PAT environment variable is not set.")

if not GITLAB_URL:
    raise ValueError("GITLAB_URL environment variable is not set.")
