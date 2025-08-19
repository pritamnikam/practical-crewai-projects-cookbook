"""
Main entry point for the Multi-Model CrewAI Application.

This script initializes and runs a crew that uses multiple LLM providers
for content creation.
"""

import logging
from .config import app_config
from .crew import run_crew

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    try:
        # Ensure config is loaded
        _ = app_config
        
        # Example topic
        topic = "The rise in global temperatures from 2018 onwards"
        
        logger.info(f"Starting multi-model crew for topic: {topic}")
        
        # Run the crew
        result = run_crew(topic)
        
        # Display the result
        print("\n" + "="*80)
        print(f"RESULT FOR TOPIC: {topic}")
        print("="*80)
        print(result['result'])
        print("="*80 + "\n")
        
        logger.info("Crew execution completed successfully.")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
