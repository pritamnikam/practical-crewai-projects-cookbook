"""
Main entry point for the Multi-Model CrewAI Application.

This script initializes and runs a crew that uses multiple LLM providers
for content creation.
"""

import argparse
import logging
from .crew import run_crew

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Run the multi-model crew to research and write an article on a given topic."
    )
    parser.add_argument(
        "topic",
        type=str,
        nargs='?',
        default="The latest advancements in AI",
        help="The topic for the crew to research and write about."
    )
    args = parser.parse_args()

    try:
        logger.info(f"Starting multi-model crew for topic: {args.topic}")
        
        # Run the crew
        result = run_crew(args.topic)
        
        # Display the result
        print("\n" + "="*80)
        print(f"RESULT FOR TOPIC: {args.topic}")
        print("="*80)
        print(result)
        print("="*80 + "\n")
        
        logger.info("Crew execution completed successfully.")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
