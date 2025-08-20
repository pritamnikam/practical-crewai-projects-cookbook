# Automated Project: Planning, Estimation, and Allocation

# Initial imports

# Warning control
import warnings
warnings.filterwarnings('ignore')

# Load environment variables
from helper import load_env
load_env()

import os
import yaml
from crewai import Agent, Task, Crew

# Set OpenAI Model
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'

# Loading Tasks and Agents YAML files

# Define file paths for YAML configurations
files = {
    'agents': 'config/agents.yaml',
    'tasks': 'config/tasks.yaml'
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)

# Assign loaded configurations to specific variables
agents_config = configs['agents']
tasks_config = configs['tasks']


# Create Pydantic Models for Structured Output
from typing import List
from pydantic import BaseModel, Field

class TaskEstimate(BaseModel):
    task_name: str = Field(..., description="Name of the task")
    estimated_time_hours: float = Field(..., description="Estimated time to complete the task in hours")
    required_resources: List[str] = Field(..., description="List of resources required to complete the task")

class Milestone(BaseModel):
    milestone_name: str = Field(..., description="Name of the milestone")
    tasks: List[str] = Field(..., description="List of task IDs associated with this milestone")

class ProjectPlan(BaseModel):
    tasks: List[TaskEstimate] = Field(..., description="List of tasks with their estimates")
    milestones: List[Milestone] = Field(..., description="List of project milestones")


# Create Crew, Agents and Tasks
# Creating Agents
project_planning_agent = Agent(
  config=agents_config['project_planning_agent']
)

estimation_agent = Agent(
  config=agents_config['estimation_agent']
)

resource_allocation_agent = Agent(
  config=agents_config['resource_allocation_agent']
)

# Creating Tasks
task_breakdown = Task(
  config=tasks_config['task_breakdown'],
  agent=project_planning_agent
)

time_resource_estimation = Task(
  config=tasks_config['time_resource_estimation'],
  agent=estimation_agent
)

resource_allocation = Task(
  config=tasks_config['resource_allocation'],
  agent=resource_allocation_agent,
  output_pydantic=ProjectPlan # This is the structured output we want
)

# Creating Crew
crew = Crew(
  agents=[
    project_planning_agent,
    estimation_agent,
    resource_allocation_agent
  ],
  tasks=[
    task_breakdown,
    time_resource_estimation,
    resource_allocation
  ],
  verbose=True
)

# Crew's Inputs
from IPython.display import display, Markdown

project = 'Online Stock Trading Platform'
industry = 'Fintech'
project_objectives = 'Develop a secure, high-performance online platform for stock trading and portfolio management'
team_members = """
- Alex Chen (Project Manager)
- Maria Rodriguez (Solutions Architect)
- David Kim (Full-Stack Engineer)
- Emily White (Backend Engineer)
- Sarah Lee (Frontend Engineer)
- Ben Carter (QA Engineer)
- Jessica Green (DevOps Engineer)
- Mike Johnson (UI/UX Designer)
- Chloe Davis (Compliance & Legal Specialist)
"""
project_requirements = """
- **Requirement Analysis & Planning:**
    - Define user personas (e.g., Novice Investor, Day Trader).
    - Comply with financial regulations (e.g., KYC, AML) and data privacy laws (e.g., GDPR).
    - Specify functional requirements: real-time market data, various order types (market, limit), portfolio tracking, and secure account funding.
    - Set non-functional requirements: low-latency performance, high security (encryption, MFA), and scalability.
- **Architecture & Design:**
    - Design a microservices architecture for independent, scalable components (e.g., Order Service, User Service).
    - Implement a real-time data processing pipeline using message queues (e.g., Kafka) and WebSockets for client updates.
    - Design a robust database schema optimized for high-volume transactions and real-time data retrieval.
    - Plan for cloud deployment on a major provider (e.g., AWS, GCP) using services like Kubernetes for orchestration.
- **Development:**
    - **Front-end:** Build an intuitive trading dashboard with real-time charts, order forms, and portfolio views.
    - **Back-end:** Develop a reliable order matching engine, integrate with market data APIs, and implement risk management logic.
    - Implement secure user authentication (including MFA) and API gateways.
- **Testing:**
    - Conduct comprehensive unit, integration, and end-to-end testing for all services.
    - Perform performance and load testing to simulate high trading volumes and ensure system stability.
    - Execute security testing (penetration testing, vulnerability scans) to protect user data and assets.
    - Conduct User Acceptance Testing (UAT) with a select group of users.
- **CI/CD & Deployment:**
    - Set up a Continuous Integration/Continuous Deployment (CI/CD) pipeline using tools like GitLab CI or GitHub Actions.
    - Use Docker for containerization and Kubernetes for automated deployment and scaling.
    - Implement a monitoring and logging solution (e.g., Prometheus, Grafana) to track system health in production.
- **Production & Maintenance:**
    - Deploy the platform to a secure cloud environment.
    - Establish a disaster recovery plan to ensure business continuity.
    - Set up an ongoing maintenance schedule for security patches, software updates, and new feature releases.
    - Provide a robust customer support system for user inquiries and technical issues.
"""

# Format the dictionary as Markdown for a better display in Jupyter Lab
formatted_output = f"""
**Project Type:** {project}

**Project Objectives:** {project_objectives}

**Industry:** {industry}

**Team Members:**
{team_members}
**Project Requirements:**
{project_requirements}
"""
# Display the formatted output as Markdown
display(Markdown(formatted_output))


# Kicking off the crew
# The given Python dictionary
inputs = {
  'project_type': project,
  'project_objectives': project_objectives,
  'industry': industry,
  'team_members': team_members,
  'project_requirements': project_requirements
}

# Run the crew
result = crew.kickoff(
  inputs=inputs
)


# Usage Metrics and Costs: Let’s see how much it would cost each time if this crew runs at scale.
import pandas as pd

costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
print(f"Total costs: ${costs:.4f}")

# Convert UsageMetrics instance to a DataFrame
df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
df_usage_metrics

# result
result.pydantic.dict()

# Inspect further
tasks = result.pydantic.dict()['tasks']
df_tasks = pd.DataFrame(tasks)

# Display the DataFrame as an HTML table
df_tasks.style.set_table_attributes('border="1"').set_caption("Task Details").set_table_styles(
    [{'selector': 'th, td', 'props': [('font-size', '120%')]}]
)

# Inspecting Milestones

milestones = result.pydantic.dict()['milestones']
df_milestones = pd.DataFrame(milestones)

# Display the DataFrame as an HTML table
df_milestones.style.set_table_attributes('border="1"').set_caption("Task Details").set_table_styles(
    [{'selector': 'th, td', 'props': [('font-size', '120%')]}]
)
