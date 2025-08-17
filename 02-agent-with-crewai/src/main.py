"""
Main entry point for the CrewAI Event Planning Crew.

This script initializes the crew and runs it with inputs provided via
the command line.
"""

import argparse
import logging
from typing import Dict
from .crew import run_event_planning_crew

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Run a multi-agent CrewAI workflow for event planning.")
    parser.add_argument(
        '--conference_name',
        type=str,
        default="AI Innovations Summit",
        help="Name of the conference."
    )
    parser.add_argument(
        '--requirements',
        type=str,
        default="Capacity for 5000, central location, modern amenities, budget up to $50,000",
        help="Requirements for the venue."
    )
    args = parser.parse_args()

    inputs: Dict[str, str] = {
        "conference_name": args.conference_name,
        "requirements": args.requirements
    }

    try:
        logger.info(f"Running CrewAI event planning workflow for: {inputs['conference_name']}")
        result = run_event_planning_crew(inputs)
        
        print("\n" + "="*80)
        print("CrewAI Result:")
        print(result)
        print("="*80 + "\n")
        
        logger.info("Crew execution completed successfully.")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
