"""
Main execution script for the Crew Execution Examples.

This script demonstrates two different ways to execute a CrewAI crew:
1. Asynchronously using `kickoff_async`.
2. Sequentially over a list of inputs using `kickoff_for_each`.
"""

import argparse
import logging
import asyncio
from .config import app_config
from .crew import create_analysis_crew

# Configure logging
logger = logging.getLogger(__name__)

async def run_async_crews():
    """Initializes and runs two crews to demonstrate async execution."""
    logger.info("Starting asynchronous crew execution example...")
    
    # Create two crews: one configured for async, one for sync
    async_crew = create_analysis_crew(async_execution=True)
    sync_crew = create_analysis_crew(async_execution=False)

    # Define inputs
    inputs_1 = {"ages": [25, 30, 35, 40, 45]}
    inputs_2 = {"ages": [20, 25, 30, 35, 40]}

    # Kick off both crews
    # The async crew is awaited directly.
    # The sync crew's blocking kickoff is run in an executor to not block the event loop.
    loop = asyncio.get_running_loop()
    sync_task = loop.run_in_executor(None, sync_crew.kickoff, inputs_2)
    
    # Await both tasks
    result_1 = await async_crew.kickoff_async(inputs=inputs_1)
    result_2 = await sync_task

    logger.info("Asynchronous execution example finished.")
    print("\n--- Async Crew Result ---")
    print(result_1)
    print("-------------------------\n")
    print("\n--- Sync Crew Result (run in parallel) ---")
    print(result_2)
    print("------------------------------------------\n")

def run_for_each_crew():
    """Initializes and runs a crew for each item in a list of inputs."""
    logger.info("Starting crew execution for a list of inputs...")
    
    analysis_crew = create_analysis_crew()

    datasets = [
        {"ages": [25, 30, 35, 40, 45]},
        {"ages": [20, 25, 30, 35, 40]},
        {"ages": [30, 35, 40, 45, 50]}
    ]

    results = analysis_crew.kickoff_for_each(inputs=datasets)
    
    logger.info("Crew execution for list finished.")
    print("\n--- Batch Crew Results ---")
    for result in results:
        print(result)
        print("--------------------------")
    print("\n")

async def main():
    """Parses command-line arguments to determine which execution method to run."""
    parser = argparse.ArgumentParser(description="Run a CrewAI example for different execution methods.")
    parser.add_argument(
        "method", 
        choices=["async", "batch"], 
        help="Specify which execution method to run ('async' or 'batch')."
    )
    args = parser.parse_args()

    _ = app_config

    if args.method == "async":
        await run_async_crews()
    elif args.method == "batch":
        # This function is synchronous, but we call it from an async main
        run_for_each_crew()

if __name__ == "__main__":
    asyncio.run(main())
