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

# Load environment variables from .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    logger.info(f"Loaded environment variables from {env_path}")

def get_config():
    """Validates and returns configuration from environment variables."""
    required_vars = ["OPENAI_API_KEY", "GOOGLE_API_KEY", "SERPER_API_KEY"]
    config = {var: os.getenv(var) for var in required_vars}
    
    missing_vars = [var for var, value in config.items() if value is None]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
    # Optional LangChain tracing
    if os.getenv("LANGCHAIN_API_KEY"):
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        logger.info("LangChain tracing enabled.")
        
    return config

# Load configuration on import
app_config = get_config()
