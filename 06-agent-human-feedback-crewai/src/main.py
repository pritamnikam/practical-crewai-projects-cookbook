"""
Main entry point for the Human-in-the-Loop CrewAI Example.

This script initializes and runs a crew to research a YouTube video and generate
an article based on a topic, incorporating human feedback.
"""

import sys
from src.config import logger
from src.crew import create_crew

def main():
    """Main function to run the crew."""
    try:
        if len(sys.argv) < 3:
            raise ValueError("Insufficient arguments. Please provide a YouTube URL and a topic.")

        youtube_url = sys.argv[1]
        topic = " ".join(sys.argv[2:])

        if not youtube_url or not topic:
            raise ValueError("YouTube URL and topic cannot be empty.")

        logger.info(f"Starting crew with YouTube URL: {youtube_url} and topic: {topic}")
        crew = create_crew(youtube_url, topic)
        result = crew.kickoff()

        logger.info("Crew execution finished.")
        print("\n---\n")
        print("Final Article:")
        print(result)
        print("\n---")

    except ValueError as e:
        logger.error(f"Error: {e}")
        print(f"Error: {e}")
        print('Example: python -m src.main "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "Rick Astley"')

if __name__ == "__main__":
    main()
