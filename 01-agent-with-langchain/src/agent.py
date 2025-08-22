"""
ReAct Agent Module

This module defines the ReAct agent, its tools, and the logic for its execution.
"""

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAI
from .config import settings

def create_agent_executor() -> AgentExecutor:
    """Creates and returns the ReAct agent executor."""
    # Get the prompt from LangChain Hub
    prompt = hub.pull("hwchase17/react")
    
    # Initialize tools
    tools = [TavilySearchResults(max_results=1, tavily_api_key=settings.tavily_api_key)]
    
    # Initialize the language model
    llm = OpenAI(openai_api_key=settings.openai_api_key)
    
    # Create the agent
    agent = create_react_agent(llm, tools, prompt)
    
    # Create the agent executor
    return AgentExecutor(agent=agent, tools=tools, verbose=True)

def run_agent(agent_executor: AgentExecutor, question: str) -> dict:
    """Run the ReAct agent on a given question and return the response."""
    return agent_executor.invoke({"input": question})
