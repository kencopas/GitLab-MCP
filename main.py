from server import mcp
from tools import *
from dotenv import load_dotenv


load_dotenv()


def main():
    print("Hello from gitlab-mcp!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
