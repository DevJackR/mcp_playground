from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Must be concise"
    )
    body: str = Field(
        description="The main content of the email. Must be well structured with proper greetings, spacing, paragraphs and tone"
    )

root_agent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    instruction="You are en email generation assistant. Your task is to generate an email as per the user's request IMPORTANT: your response must be a JSON matching {subject: subject here, body: body here}",
    description="You are an email agent you writes emails",
    output_schema=EmailContent,
    output_key="email" 
)