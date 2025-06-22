"""Configuration settings for the ADK A2A Notion-ElevenLabs integration."""

import os
from typing import Final
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GOOGLE_API_KEY: Final[str] = os.getenv("GOOGLE_API_KEY", "")

# A2A Service URLs
GIT_AGENT_A2A_URL: Final[str] = os.getenv("GIT_AGENT_A2A_URL", "http://localhost:8002")

# ADK Configuration
ADK_MODEL: Final[str] = os.getenv("ADK_MODEL", "gemini-2.0-flash") 