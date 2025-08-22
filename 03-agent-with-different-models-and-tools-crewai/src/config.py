"""
Configuration module for the Multi-Model CrewAI Application.

This module handles loading and validating environment variables required by the application.
"""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class Settings:
    """Configuration settings for the application."""
    def __init__(self):
        env_path = Path(__file__).resolve().parent.parent / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
            logger.info(f"Loaded environment variables from {env_path}")
        
        self.openai_api_key = self._get_required_env("OPENAI_API_KEY")
        self.google_api_key = self._get_required_env("GOOGLE_API_KEY")
        self.serper_api_key = self._get_required_env("SERPER_API_KEY")
        
        # Optional LangChain tracing
        if os.getenv("LANGCHAIN_API_KEY"):
            os.environ["LANGCHAIN_TRACING_V2"] = "true"
            logger.info("LangChain tracing enabled.")

    def _get_required_env(self, var_name: str) -> str:
        """Get a required environment variable."""
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"Missing required environment variable: {var_name}")
        return value

# Create a single instance of the settings
settings = Settings()
