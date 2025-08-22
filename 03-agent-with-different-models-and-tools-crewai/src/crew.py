"""
Crew definition for the Multi-Model CrewAI Application.

This module defines the agents, tasks, and crew responsible for researching and
writing an article using different LLM providers (Gemini and GPT-4o).
"""

import logging
from typing import Dict, List, Any

from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from .config import settings

logger = logging.getLogger(__name__)

def _initialize_llms() -> Dict[str, Any]:
    """Initializes and returns the language models."""
    gemini = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=True,
        temperature=0.5,
        google_api_key=settings.google_api_key,
    )
    gpt = ChatOpenAI(
        model="gpt-4o-2024-08-06",
        verbose=True,
        temperature=0.5,
        openai_api_key=settings.openai_api_key,
    )
    logger.info("Initialized models: gemini-1.5-flash, gpt-4o-2024-08-06")
    return {"gemini": gemini, "gpt": gpt}

def _define_agents(llms: Dict[str, Any], search_tool: SerperDevTool) -> List[Agent]:
    """Defines the agents for the multi-model crew."""
    article_researcher = Agent(
        role="Senior Researcher",
        goal='Uncover groundbreaking technologies in {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of innovation, "
            "eager to explore and share knowledge that could change the world."
        ),
        tools=[search_tool],
        llm=llms['gemini'],
        allow_delegation=True
    )

    article_writer = Agent(
        role='Writer',
        goal='Narrate compelling tech stories about {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft "
            "engaging narratives that captivate and educate, bringing new "
            "discoveries to light in an accessible manner."
        ),
        tools=[search_tool],
        llm=llms['gpt'],
        allow_delegation=False
    )
    logger.info("Created agents: article_researcher, article_writer")
    return [article_researcher, article_writer]

def _define_tasks(agents: List[Agent], search_tool: SerperDevTool) -> List[Task]:
    """Defines the tasks for the multi-model crew."""
    article_researcher, article_writer = agents

    research_task = Task(
        description=(
            "Conduct a thorough analysis on the given {topic}. "
            "Utilize SerperSearch for any necessary online research. "
            "Summarize key findings in a detailed report."
        ),
        expected_output='A detailed report on the data analysis with key insights.',
        tools=[search_tool],
        agent=article_researcher,
    )

    writing_task = Task(
        description=(
            "Write an insightful article based on the data analysis report. "
            "The article should be clear, engaging, and easy to understand."
        ),
        expected_output='A 6-paragraph article summarizing the data insights.',
        agent=article_writer,
    )
    logger.info("Created tasks: research_task, writing_task")
    return [research_task, writing_task]

def run_crew(topic: str) -> str:
    """
    Initializes and runs the crew for the given topic.

    Args:
        topic: The topic to research and write about.

    Returns:
        The result of the crew's execution.
    """
    search_tool = SerperDevTool(api_key=settings.serper_api_key)
    llms = _initialize_llms()
    agents = _define_agents(llms, search_tool)
    tasks = _define_tasks(agents, search_tool)

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    logger.info(f"Starting crew with topic: {topic}")
    inputs = {'topic': topic}
    result = crew.kickoff(inputs=inputs)
    
    logger.info("Crew execution completed successfully")
    return result
