"""
Main execution script for the Conditional Tasks CrewAI Example.

This script initializes and runs a crew that demonstrates conditional task execution.
"""

import logging
from .config import app_config
from .crew import create_event_crew

# Configure logging
logger = logging.getLogger(__name__)

def main():
    """Initializes and runs the event planning crew."""
    logger.info("Starting the conditional event planning crew...")
    
    # Access the configuration to ensure it's loaded
    _ = app_config
    
    event_crew = create_event_crew()
    result = event_crew.kickoff()
    
    logger.info("Crew execution finished.")
    print("\n--- Final Result ---")
    print(result)
    print("--------------------\n")

if __name__ == "__main__":
    main()
