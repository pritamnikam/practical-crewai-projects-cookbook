"""
Crew definition for the Crew Execution Examples.

This module defines a function to create a crew of agents designed to
analyze numerical data.
"""

from crewai import Agent, Task, Crew

def create_analysis_crew(async_execution=False):
    """
    Creates and configures an analysis crew.

    Args:
        async_execution (bool): Whether the tasks should be executed asynchronously.

    Returns:
        Crew: An instance of the analysis crew.
    """
    # Create an analysis agent
    analysis_agent = Agent(
        role="Mathematician",
        goal="Analyze data and provide insights.",
        backstory="You are an experienced mathematician with a strong background in statistics.",
        verbose=True,
        memory=True
    )

    # Create a data analysis task
    data_analysis_task = Task(
        description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
        agent=analysis_agent,
        expected_output="A report with the dataset and the calculated average age.",
        async_execution=async_execution
    )

    # Create a crew with the agent and task
    analysis_crew = Crew(
        agents=[analysis_agent],
        tasks=[data_analysis_task]
    )

    return analysis_crew
