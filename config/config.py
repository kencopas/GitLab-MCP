import os

from dotenv import load_dotenv


load_dotenv()


GITLAB_API_PAT = os.getenv("GITLAB_API_PAT")
GITLAB_URL = os.getenv("GITLAB_URL", "https://gitlab.com").rstrip("/")
