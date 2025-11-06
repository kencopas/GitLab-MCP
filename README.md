# Setup

### Clone the repository

```bash
git clone https://github.com/kencopas/GitLab-MCP
cd GitLab-MCP
```

### Install Dependencies

**Windows**
```bash
uv venv  # Or python3 -m venv .venv
.venv\Scripts\activate
uv sync  # Or pip install -r requirements.txt
```

**Linux**
```bash
uv venv  # Or python3 -m venv .venv
source .venv/bin/activate
uv sync  # Or pip install -r requirements.txt
```


### Add entry to `mcp.json`

Go to the search bar at the top of VS Code and select `>MCP: Open User Configuration` to open the `mcp.json` file. Make sure the following entry is included:

```json
{
    "servers": {
        "gitlab-mcp": {
			"type": "stdio",
			"command": "path/to/your/venv/python",
			"args": [
				"path/to/your/GitLab-MCP/main.py"
			]
		}
    }
}
```


### Run the MCP Server

In VS Code, upon adding a server entry you should be able to click the Start text that appears above the entry. Now GitHub Copilot should have access to the tools and resources within the server.
