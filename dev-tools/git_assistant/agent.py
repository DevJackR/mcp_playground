import json
from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm
import os
from utils.custom_adk_patches import CustomMCPToolset
#from utils.custom_adk_patches import CustomMCPToolset

from git_assistant.prompt import GIT_PROMPT

def create_git_agent(GIT_REPO_PATH: str) -> Agent:
    # GIT_REPO_PATH = "/Users/jack/Documents/programming/mcp/mcp_playground"

    # server_params = StdioServerParameters(
    #     command="mcp-server-git",
    #     args=["--repository", GIT_REPO_PATH],
    # )

    # toolset = MCPToolset(server_params=server_params)

    toolset = CustomMCPToolset(
                connection_params=StdioServerParameters(
                    command='mcp-server-git',
                    args=["--repository", GIT_REPO_PATH]
                )
            )

    return Agent(
        name="git_assistant",
        model =  "gemini-2.0-flash",
        description="Agent for git",
        instruction=GIT_PROMPT,
        tools=[toolset]
    )

root_agent = create_git_agent(GIT_REPO_PATH="/Users/jack/Documents/programming/mcp/mcp_playground")