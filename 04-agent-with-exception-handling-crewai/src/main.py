"""
Main entry point for the CrewAI Exception Handling Example.

This script initializes and runs the crew with a topic provided via the command line.
It demonstrates how to handle potential errors, such as a missing topic.
"""

import argparse
import logging
from typing import Dict
from .crew import create_crew

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Run a CrewAI workflow to research and write about a topic.")
    parser.add_argument(
        "topic",
        type=str,
        nargs='?',
        default="",
        help="The topic for the crew to research and write about."
    )
    args = parser.parse_args()

    inputs: Dict[str, str] = {
        "topic": args.topic
    }

    try:
        # Create and run the crew
        crew = create_crew(inputs)
        logger.info(f"Crew created. Kicking off workflow for topic: '{args.topic}'")
        result = crew.kickoff()
        
        # Print the results
        print("\n" + "="*80)
        print("CrewAI Workflow Result:")
        print(result)
        print("="*80 + "\n")
        
        logger.info("Crew execution completed successfully.")
        
    except ValueError as ve:
        # Handle the specific error for a missing topic
        logger.error(f"Validation Error: {str(ve)}")
        print(f"\nError: {str(ve)}")
        print("Please provide a topic to run the crew. Example: python -m src.main \"Artificial Intelligence\"")
    except Exception as e:
        # Handle other potential errors (e.g., API keys)
        logger.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
