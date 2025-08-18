"""
Crew definition for the Code Generation & Debugging CrewAI Example.

This module defines the agents and tasks for two separate crews:
1. A coding crew that generates and executes Python code.
2. A debugging crew that identifies and fixes bugs in Python code.
"""

from crewai import Agent, Task, Crew

# 1. Coding Crew
def create_coding_crew():
    """Creates and configures the coding crew."""
    # Create an agent with code execution enabled
    coding_agent = Agent(
        role="Python Data Analyst",
        goal="Write and execute Python code to perform calculations",
        backstory="You are an experienced Python developer, skilled at writing efficient code to solve problems.",
        allow_code_execution=True,
        verbose=True,
        memory=True
    )

    # Define the task with explicit instructions to generate and execute Python code
    data_analysis_task = Task(
        description=(
            "Write Python code to calculate the average of the following list of ages: [23, 35, 31, 29, 40]. "
            "Output the result in the format: 'The average age of participants is: <calculated_average_age>'"
        ),
        agent=coding_agent,
        expected_output="The generated code based on the requirments and the average age of participants is: <calculated_average_age>."
    )

    # Create a crew and add the task
    analysis_crew = Crew(
        agents=[coding_agent],
        tasks=[data_analysis_task]
    )
    
    return analysis_crew

# 2. Debugging Crew
def create_debugging_crew():
    """Creates and configures the debugging crew."""
    # Create a debugging agent with code execution enabled
    debugging_agent = Agent(
        role="Python Debugger",
        goal="Identify and fix issues in existing Python code",
        backstory="You are an experienced Python developer with a knack for finding and fixing bugs.",
        allow_code_execution=True,
        verbose=True,
        memory=True
    )

    # Define a task that involves debugging the provided code
    debug_task = Task(
        description=(
            "The following Python code is supposed to return the square of each number in the list, "
            "but it contains a bug. Please identify and fix the bug:\n"
            "```\n"
            "numbers = [2, 4, 6, 8]\n"
            "squared_numbers = [n*m for n in numbers]\n"
            "print(squared_numbers)\n"
            "```"
        ),
        agent=debugging_agent,
        expected_output="The corrected code should output the squares of the numbers in the list. Provide the updated code and tell what was the bug and how you fixed it."
    )

    # Form a crew and assign the debugging task
    debug_crew = Crew(
        agents=[debugging_agent],
        tasks=[debug_task]
    )
    
    return debug_crew
