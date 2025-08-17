"""
Main entry point for the Hierarchical CrewAI Example.

This script initializes and runs a hierarchical crew to research a topic provided
via command-line arguments.
"""

import sys
from src.config import logger
from src.crew import create_crew

def main():
    """Main function to run the crew."""
    try:
        topic = " ".join(sys.argv[1:])
        if not topic:
            raise ValueError("The 'topic' for the crew to research and write about cannot be empty. Please provide a topic.")

        logger.info(f"Starting crew with topic: {topic}")
        crew = create_crew(topic)
        result = crew.kickoff()

        logger.info("Crew execution finished.")
        print("\n---\n")
        print("Research Report:")
        print(result)
        print("\n---")

    except ValueError as e:
        logger.error(f"Error: {e}")
        print(f"Error: {e}")
        print("Example: python -m src.main \"Artificial Intelligence\"")

if __name__ == "__main__":
    main()
