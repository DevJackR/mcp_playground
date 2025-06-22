from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful greeting agent. Ask for the user's name then greet them"
) # Root agent is the entry point for requests 
# Name of the agent is important the name must be the same as the folder name