"""
Crew definition for the Human-in-the-Loop CrewAI Example.

This module defines the agents, tasks, and the crew responsible for
researching a YouTube video and generating an article with human feedback.
"""

from crewai import Agent, Task, Crew
from crewai_tools import YoutubeVideoSearchTool

def create_crew(youtube_url: str, topic: str):
    """Creates and configures the research crew with human-in-the-loop feedback."""
    
    # Initialize the YouTube search tool with the provided URL
    youtube_tool = YoutubeVideoSearchTool(youtube_video_url=youtube_url)

    # Define Agents
    researcher = Agent(
        role='Video Content Researcher',
        goal='Extract key insights from the provided YouTube video on the given topic.',
        backstory=(
            "You are a skilled researcher who excels at extracting valuable insights from video content. "
            "You focus on gathering accurate and relevant information from YouTube to support your team."
        ),
        verbose=True,
        tools=[youtube_tool],
        memory=True
    )

    writer = Agent(
        role='Tech Article Writer',
        goal='Craft an article based on the research insights.',
        backstory=(
            "You are an experienced writer known for turning complex information into engaging and accessible articles. "
            "Your work helps make advanced technology topics understandable to a broad audience."
        ),
        verbose=True,
        memory=True
    )

    # Define Tasks
    research_task = Task(
        description=(
            f"Research and extract key insights from the YouTube video regarding {topic}. "
            "Compile your findings in a detailed summary."
        ),
        expected_output=f'A summary of the key insights from the YouTube video about {topic}.',
        agent=researcher
    )

    writing_task = Task(
        description=(
            f"Using the summary provided by the researcher, write a compelling article on {topic}. "
            "Ensure the article is well-structured and engaging for a tech-savvy audience."
        ),
        expected_output=f'A well-written article on {topic} based on the YouTube video research.',
        agent=writer,
        human_input=True  # Allow for human feedback after the draft
    )

    # Define the crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True,
        memory=True
    )

    return crew
