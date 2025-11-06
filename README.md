# Setup

## Clone the repository

```bash
git clone https://github.com/kencopas/GitLab-MCP
cd GitLab-MCP
```

## Install Dependencies

### Windows

```bash
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Setup Environment Variables

Create a `.env` in the root of the project in the same manner as the `.env.example` file. Update the following environment variable:

```bash
GITLAB_API_PAT=your_personal_access_token_here
```

To get a GitLab access token, login to your GitLab account and click your user profile icon. Then navigate to **Edit profile** > **Access tokens** > **Add new token**. Select the required scopes (at least the **api** scope but the more the merrier) and then create the token.

## Register MCP Server

Go to the search bar at the top of VS Code and select `> MCP: Open User Configuration` to open the `mcp.json` file (for other IDEs find the equivalent file). Make sure the following entry is included:

### Windows

```json
{
    "servers": {
        "gitlab-mcp": {
			"type": "stdio",
			"command": "C:\\absolute\\path\\to\\your\\venv\\Scripts\\python.exe",
			"args": [
				"C:\\absolute\\path\\to\\your\\GitLab-MCP\\main.py"
			]
		}
    }
}
```

### Linux

```json
{
    "servers": {
        "gitlab-mcp": {
			"type": "stdio",
			"command": "/absolute/path/to/your/venv/bin/python",
			"args": [
				"/absolute/path/to/your/GitLab-MCP/main.py"
			]
		}
    }
}
```

!!!_ Ensure these filepaths are **absolute** and Windows paths have **double-escaped backslashes** (\\\\).


## Run the MCP Server

In VS Code, upon adding a server entry you should be able to click the *Start* text that appears above the entry.

Now GitHub Copilot should have access to the tools and resources within the server.
