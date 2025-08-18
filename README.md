# Comprehensive CrewAI Examples

This repository contains a collection of hands-on examples demonstrating various features and best practices for building multi-agent systems with [CrewAI](https://docs.crewai.com/). The projects range from basic agent setups to advanced hierarchical structures, all with a focus on clean, modular, and production-ready code.

Each project is self-contained, fully containerized with Docker, and includes detailed documentation.

## Projects

Here is a summary of the examples included in this repository:

1.  **[01-agent-with-langchain](./01-agent-with-langchain/)**
    -   **Description**: A foundational example demonstrating how to build a simple agent using the core components of LangChain.
    -   **Concepts**: LangChain basics, Agent-Tool interaction.

2.  **[02-agent-with-crewai](./02-agent-with-crewai/)**
    -   **Description**: An introduction to CrewAI, showcasing how to create a simple multi-agent crew to accomplish a task.
    -   **Concepts**: CrewAI Agents, Tasks, and Crews.

3.  **[03-agent-with-different-models-and-tools-crewai](./03-agent-with-different-models-and-tools-crewai/)**
    -   **Description**: An advanced example that demonstrates how to integrate different LLMs (e.g., Groq) and custom tools within a single crew.
    -   **Concepts**: Multi-LLM configurations, custom tool integration.

4.  **[04-agent-with-exception-handling-crewai](./04-agent-with-exception-handling-crewai/)**
    -   **Description**: A practical example focused on building robust crews with proper error and exception handling.
    -   **Concepts**: Graceful error handling, input validation.

5.  **[05-hirarchical-agent-structure-crewai](./05-hirarchical-agent-structure-crewai/)**
    -   **Description**: A sophisticated example that implements a hierarchical crew structure, where a manager agent delegates tasks to subordinate agents.
    -   **Concepts**: Hierarchical process, manager LLM, delegation.

6.  **[06-agent-human-feedback-crewai](./06-agent-human-feedback-crewai/)**
    -   **Description**: An interactive example that shows how to pause a crew to ask for human feedback before continuing a task.
    -   **Concepts**: Human-in-the-loop, interactive workflows.

7.  **[07-agent-generating-code-crewai](./07-agent-generating-code-crewai/)**
    -   **Description**: A dual-purpose example demonstrating how agents can both generate new code and debug existing code.
    -   **Concepts**: Code generation, debugging, dynamic crew selection.

8.  **[08-agent-kickoff-crewai](./08-agent-kickoff-crewai/)**
    -   **Description**: A project showcasing advanced crew execution methods, including asynchronous and batch processing.
    -   **Concepts**: Asynchronous execution, batch processing, `kickoff_async`, `kickoff_for_each`.

## Getting Started

Each project directory contains its own `README.md` with specific instructions for setup and execution. In general, all projects follow a similar structure:

1.  **Navigate to a project directory:**
    ```bash
    cd <project-directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    -   Copy `.env.example` to `.env`.
    -   Add your API keys to the `.env` file.

4.  **Run the application:**
    -   Execution instructions are provided in each project's `README.md`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
