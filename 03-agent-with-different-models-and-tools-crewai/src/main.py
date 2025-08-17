"""
Multi-Model CrewAI Application

This script demonstrates how to use CrewAI to coordinate multiple agents,
each powered by different LLM providers (Gemini, GPT-4o), for collaborative content creation.
"""

import os
import logging
from typing import Dict, Any
from pathlib import Path
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    logger.info("Loaded environment variables from .env file")


class MultiModelCrew:
    """Orchestrates multiple AI agents with different LLM backends."""

    def __init__(self):
        """Initialize the MultiModelCrew with required tools and models."""
        self._validate_environment()
        self._initialize_tools()
        self._initialize_models()
        self._create_agents()
        self._create_tasks()

    def _validate_environment(self):
        """Validate that all required environment variables are set."""
        required_vars = ["OPENAI_API_KEY", "GOOGLE_API_KEY", "SERPER_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}. "
                "Please check your .env file or environment variables."
            )

    def _initialize_tools(self):
        """Initialize the tools that agents can use."""
        from crewai_tools import ScrapeWebsiteTool, SerperDevTool
        
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        logger.info("Initialized tools: search_tool, scrape_tool")

    def _initialize_models(self):
        """Initialize the language models from different providers."""
        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain_openai import ChatOpenAI

        # Initialize Gemini model
        self.gemini = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            verbose=True,
            temperature=0.5,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

        # Initialize GPT-4 model
        self.gpt = ChatOpenAI(
            model="gpt-4o-2024-08-06",
            verbose=True,
            temperature=0.5,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )
        logger.info("Initialized language models: gemini-1.5-flash, gpt-4o-2024-08-06")

    def _create_agents(self):
        """Create the AI agents with specific roles and models."""
        from crewai import Agent

        # Data Researcher Agent using Gemini
        self.article_researcher = Agent(
            role="Senior Researcher",
            goal='Uncover groundbreaking technologies in {topic}',
            verbose=True,
            memory=True,
            backstory=(
                "Driven by curiosity, you're at the forefront of innovation, "
                "eager to explore and share knowledge that could change the world."
            ),
            tools=[self.search_tool],
            llm=self.gemini,
            allow_delegation=True
        )

        # Article Writer Agent using GPT
        self.article_writer = Agent(
            role='Writer',
            goal='Narrate compelling tech stories about {topic}',
            verbose=True,
            memory=True,
            backstory=(
                "With a flair for simplifying complex topics, you craft "
                "engaging narratives that captivate and educate, bringing new "
                "discoveries to light in an accessible manner."
            ),
            tools=[self.search_tool],
            llm=self.gpt,
            allow_delegation=False
        )
        logger.info("Created agents: article_researcher, article_writer")

    def _create_tasks(self):
        """Define the tasks for the agents."""
        from crewai import Task

        # Research Task
        self.research_task = Task(
            description=(
                "Conduct a thorough analysis on the given {topic}. "
                "Utilize SerperSearch for any necessary online research. "
                "Summarize key findings in a detailed report."
            ),
            expected_output='A detailed report on the data analysis with key insights.',
            tools=[self.search_tool],
            agent=self.article_researcher,
        )

        # Writing Task
        self.writing_task = Task(
            description=(
                "Write an insightful article based on the data analysis report. "
                "The article should be clear, engaging, and easy to understand."
            ),
            expected_output='A 6-paragraph article summarizing the data insights.',
            agent=self.article_writer,
        )
        logger.info("Created tasks: research_task, writing_task")

    def run(self, topic: str) -> Dict[str, Any]:
        """
        Run the crew with the given topic.
        
        Args:
            topic: The topic to research and write about.
            
        Returns:
            Dict containing the results and metadata.
        """
        from crewai import Crew, Process
        from IPython.display import Markdown

        logger.info(f"Starting crew with topic: {topic}")
        
        # Form the crew and define the process
        crew = Crew(
            agents=[self.article_researcher, self.article_writer],
            tasks=[self.research_task, self.writing_task],
            process=Process.sequential,
            verbose=True
        )

        # Kick off the crew
        inputs = {'topic': topic}
        result = crew.kickoff(inputs=inputs)
        
        # Prepare the result
        output = {
            'topic': topic,
            'result': result.raw,
            'markdown': Markdown(result.raw)
        }
        
        logger.info("Crew execution completed successfully")
        return output


def main():
    """Main entry point for the application."""
    try:
        # Example topic
        topic = "The rise in global temperatures from 2018 onwards"
        
        # Initialize and run the crew
        crew = MultiModelCrew()
        result = crew.run(topic)
        
        # Display the result
        print("\n" + "="*80)
        print(f"RESULT FOR TOPIC: {topic}")
        print("="*80)
        print(result['result'])
        print("="*80 + "\n")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
