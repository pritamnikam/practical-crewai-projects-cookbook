"""
Main entry point for the ReAct LangChain Agent.

This script initializes the agent and runs it with a question provided via
the command line.
"""

import argparse
import logging
from .agent import create_agent_executor, run_agent

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="Run a ReAct agent with a specific question.")
    parser.add_argument(
        "question",
        type=str,
        nargs='?',
        default="What is the latest news on AI?",
        help="The question to ask the ReAct agent."
    )
    args = parser.parse_args()

    try:
        logger.info("Creating ReAct agent executor...")
        agent_executor = create_agent_executor()
        logger.info(f"Running ReAct agent for question: {args.question}")
        response = run_agent(agent_executor, args.question)
        
        print("\n" + "="*80)
        print("Agent Response:")
        print(response)
        print("="*80 + "\n")
        
        logger.info("Agent execution completed successfully.")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
