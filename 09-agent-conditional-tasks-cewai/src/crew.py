"""
Crew definition for the Conditional Tasks CrewAI Example.

This module defines the agents, tasks, and crew responsible for collecting,
verifying, and summarizing event data based on a conditional workflow.
"""

from typing import List
from pydantic import BaseModel
from crewai import Agent, Task, Crew
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput
from crewai_tools import SerperDevTool

# --- Pydantic Model for Task Output ---
class EventsData(BaseModel):
    """Data model for a list of events."""
    events: List[str]

# --- Condition Function for the Conditional Task ---
def should_fetch_more_data(output: TaskOutput) -> bool:
    """
    Determines if more data needs to be fetched based on the number of events found.

    Args:
        output (TaskOutput): The output from the previous task.

    Returns:
        bool: True if the number of events is less than 8, False otherwise.
    """
    # Check if the pydantic model is not None and has the 'events' attribute
    if output.pydantic and hasattr(output.pydantic, 'events'):
        return len(output.pydantic.events) < 8
    # Fallback if the output is not as expected
    return True

# --- Crew Definition ---
def create_event_crew():
    """Creates and configures the event planning crew."""
    # Define Agents
    data_collector = Agent(
        role="Data Collector",
        goal="Retrieve event data using the Serper tool",
        backstory="You have a knack for finding the most exciting events happening around.",
        verbose=True,
        tools=[SerperDevTool()],
        allow_delegation=False,
    )

    data_analyzer = Agent(
        role="Data Analyzer",
        goal="Analyze the collected data and trigger re-collection if needed",
        backstory="You're known for your analytical skills, ensuring data quality and completeness.",
        verbose=True,
        allow_delegation=False,
    )

    summary_creator = Agent(
        role="Summary Creator",
        goal="Produce a concise summary from the event data",
        backstory="You're a skilled writer, able to summarize information clearly and effectively.",
        verbose=True,
        allow_delegation=False,
    )

    # Define Tasks
    fetch_task = Task(
        description="Collect event data for New York City using the Serper tool",
        expected_output="A list of 8 exciting events happening in NYC this week",
        agent=data_collector,
        output_pydantic=EventsData,
    )

    verify_data_task = ConditionalTask(
        description="Ensure that sufficient event data has been collected. If fewer than 8 events are found, delegate back to the data_collector to gather more.",
        expected_output="An updated list of at least 8 events happening in NYC this week",
        condition=should_fetch_more_data,
        agent=data_analyzer,
        tasks=[fetch_task] # Task to run if condition is met
    )

    summary_task = Task(
        description="Summarize the collected events data for NYC into a clear, engaging paragraph.",
        expected_output="A well-written summary of the events.",
        agent=summary_creator,
        context=[fetch_task, verify_data_task]
    )

    # Assemble the crew
    event_crew = Crew(
        agents=[data_collector, data_analyzer, summary_creator],
        tasks=[fetch_task, verify_data_task, summary_task],
        verbose=True,
        planning=True  # Retain the planning feature
    )

    return event_crew
