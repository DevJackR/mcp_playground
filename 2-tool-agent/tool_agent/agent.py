from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from datetime import datetime

def get_current_datetime() -> datetime:
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Create the agent
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful tool agent with the following tools: google_search_tool, get_current_datetime",
    tools=[get_current_datetime]
    #[GoogleSearchTool(), get_current_datetime]
)

