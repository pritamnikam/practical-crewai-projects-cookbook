"""
CrewAI Exception Handling Crew Module

This module defines the agents, tasks, and crew for the exception handling workflow.
It includes a check to prevent running the crew without a topic, thus avoiding an infinite loop.
"""

from typing import Dict
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from . import config  # Ensures config is loaded

def create_crew(inputs: Dict[str, str]) -> Crew:
    """Creates and configures the CrewAI crew.

    Args:
        inputs: A dictionary containing the 'topic' for the crew to work on.

    Returns:
        An instance of the Crew.
        
    Raises:
        ValueError: If the 'topic' is missing from the inputs.
    """
    topic = inputs.get('topic')
    if not topic:
        raise ValueError("The 'topic' for the crew to research and write about cannot be empty.")

    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()

    # Define Agents
    article_researcher = Agent(
        role="Senior Researcher",
        goal=f'Uncover details regarding the {topic}.',
        verbose=True,
        memory=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of research, "
            "eager to explore and share knowledge about any given topic."
        ),
        tools=[search_tool]
    )

    article_writer = Agent(
        role='Senior Writer',
        goal=f'Narrate compelling tech stories about {topic}.',
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft "
            "engaging narratives that captivate and educate, bringing new "
            "discoveries to light in an accessible manner."
        ),
        allow_delegation=False  # No delegation needed for this simple workflow
    )

    # Define Tasks
    research_task = Task(
        description=(
            f"Conduct a thorough analysis on the given {topic}. "
            "Utilize the search tool for any necessary online research. "
            "Summarize key findings in a detailed report."
        ),
        expected_output='A detailed report on the data analysis with key insights.',
        tools=[search_tool, scrape_tool],
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

    # Assemble the Crew
    return Crew(
        agents=[article_researcher, article_writer],
        tasks=[research_task, writing_task],
        process=Process.sequential
    )
