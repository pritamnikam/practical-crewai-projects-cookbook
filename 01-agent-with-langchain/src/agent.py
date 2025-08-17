"""
ReAct Agent Module

This module defines the ReAct agent, its tools, and the logic for its execution.
"""

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAI
from . import config  # Ensures config is loaded

def run_agent(question: str) -> dict:
    """Run the ReAct agent on a given question and return the response."""
    # Get the prompt from LangChain Hub
    prompt = hub.pull("hwchase17/react")
    
    # Initialize tools
    tools = [TavilySearchResults(max_results=1)]
    
    # Initialize the language model
    llm = OpenAI()
    
    # Create the agent
    agent = create_react_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    # Invoke the agent
    response = agent_executor.invoke({"input": question})
    
    return response
