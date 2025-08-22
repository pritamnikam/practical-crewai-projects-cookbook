"""
CrewAI Event Planning Crew Module

This module defines the agents, tasks, and crew for the event planning workflow.
"""

from typing import Dict, List
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from .config import settings

def define_agents() -> List[Agent]:
    """Defines the agents for the event planning crew."""
    search_tool = SerperDevTool(api_key=settings.serper_api_key)
    
    venue_finder = Agent(
        role="Conference Venue Finder",
        goal="Find the best venue for the upcoming conference",
        backstory=(
            "You are an experienced event planner with a knack for finding the perfect venues. "
            "Your expertise ensures that all conference requirements are met efficiently. "
            "Your goal is to provide the client with the best possible venue options."
        ),
        tools=[search_tool],
        verbose=True
    )

    venue_quality_assurance_agent = Agent(
        role="Venue Quality Assurance Specialist",
        goal="Ensure the selected venues meet all quality standards and client requirements",
        backstory=(
            "You are meticulous and detail-oriented, ensuring that the venue options provided "
            "are not only suitable but also exceed the client's expectations. "
            "Your job is to review the venue options and provide detailed feedback."
        ),
        tools=[search_tool],
        verbose=True
    )
    return [venue_finder, venue_quality_assurance_agent]

def define_tasks(agents: List[Agent]) -> List[Task]:
    """Defines the tasks for the event planning crew."""
    venue_finder, venue_quality_assurance_agent = agents
    search_tool = SerperDevTool(api_key=settings.serper_api_key)

    find_venue_task = Task(
        description=(
            "Conduct a thorough search to find the best venue for the upcoming conference in Las Vegas, USA. "
            "Consider factors such as capacity, location, amenities, and pricing. "
            "Use online resources and databases to gather comprehensive information."
        ),
        expected_output=(
            "A list of 5 potential venues with detailed information on capacity, location, amenities, pricing, and availability."
        ),
        tools=[search_tool],
        agent=venue_finder,
    )

    quality_assurance_review_task = Task(
        description=(
            "Review the venue options provided by the Conference Venue Finder. "
            "Ensure that each venue meets all the specified requirements and standards. "
            "Provide a detailed report on the suitability of each venue."
        ),
        expected_output=(
            "A detailed review of the 5 potential venues, highlighting any issues, strengths, and overall suitability."
        ),
        tools=[search_tool],
        agent=venue_quality_assurance_agent,
    )
    return [find_venue_task, quality_assurance_review_task]

def create_and_run_crew(agents: List[Agent], tasks: List[Task], inputs: Dict[str, str]) -> str:
    """Creates and runs the event planning crew."""
    event_planning_crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )
    result = event_planning_crew.kickoff(inputs=inputs)
    return result

def run_event_planning_crew(inputs: Dict[str, str]) -> str:
    """Run the multi-agent CrewAI workflow for event planning."""
    agents = define_agents()
    tasks = define_tasks(agents)
    result = create_and_run_crew(agents, tasks, inputs)
    return result
