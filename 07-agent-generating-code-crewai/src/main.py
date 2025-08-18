"""
Main execution script for the Code Generation & Debugging CrewAI Example.

This script initializes and runs one of two crews based on user input:
1. A coding crew that generates and executes Python code.
2. A debugging crew that identifies and fixes bugs in Python code.
"""

import argparse
import logging
from .config import app_config
from .crew import create_coding_crew, create_debugging_crew

# Configure logging
logger = logging.getLogger(__name__)

def run_coding_crew():
    """Initializes and runs the coding crew."""
    logger.info("Starting the coding crew...")
    coding_crew = create_coding_crew()
    result = coding_crew.kickoff()
    logger.info("Coding crew finished.")
    print("\n--- Coding Crew Result ---")
    print(result)
    print("--------------------------\n")

def run_debugging_crew():
    """Initializes and runs the debugging crew."""
    logger.info("Starting the debugging crew...")
    debugging_crew = create_debugging_crew()
    result = debugging_crew.kickoff()
    logger.info("Debugging crew finished.")
    print("\n--- Debugging Crew Result ---")
    print(result)
    print("----------------------------\n")

def main():
    """Parses command-line arguments to determine which crew to run."""
    parser = argparse.ArgumentParser(description="Run a CrewAI example for code generation or debugging.")
    parser.add_argument(
        "crew", 
        choices=["coding", "debugging"], 
        help="Specify which crew to run ('coding' or 'debugging')."
    )
    args = parser.parse_args()

    # Access the configuration to ensure it's loaded
    _ = app_config

    if args.crew == "coding":
        run_coding_crew()
    elif args.crew == "debugging":
        run_debugging_crew()

if __name__ == "__main__":
    main()
