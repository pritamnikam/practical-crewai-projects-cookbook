# 09: Conditional Task Execution in CrewAI

This project demonstrates how to implement conditional tasks in CrewAI. The crew is designed to search for events, check if enough events were found, and perform another search if the condition is not met before summarizing the results.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)

## Project Structure

The project is organized into a modular `src` directory:

```
09-agent-conditional-tasks-cewai/
├── src/
│   ├── __init__.py
│   ├── config.py       # Handles API keys and environment variables
│   ├── crew.py         # Defines the agents, tasks, and conditional logic
│   └── main.py         # Main script to run the crew
├── .env.example        # Example environment file
├── .gitignore          # Git ignore file
├── Dockerfile          # Docker configuration
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- A [Serper API key](https://serper.dev/)

### Installation

1.  **Clone the repository** (if you haven't already).

2.  **Navigate to the project directory**:
    ```bash
    cd 09-agent-conditional-tasks-cewai
    ```

3.  **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
    ```

4.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your environment variables**:
    -   Create a `.env` file by copying the `.env.example` file:
        ```bash
        cp .env.example .env
        ```
    -   Add your OpenAI and Serper API keys to the `.env` file:
        ```
        OPENAI_API_KEY="your-openai-api-key"
        SERPER_API_KEY="your-serper-api-key"
        ```

## Usage

To run the crew, execute the `main.py` script from the project's root directory:

```bash
python -m src.main
```

## How It Works

This crew uses a `ConditionalTask` to create a dynamic workflow:

1.  **`fetch_task`**: The `Data Collector` agent searches for events in New York City.
2.  **`verify_data_task`**: This is a `ConditionalTask`. The `Data Analyzer` agent checks the output of the `fetch_task`.
    -   **Condition**: The `should_fetch_more_data` function checks if fewer than 8 events were found.
    -   **If True**: The condition is met, and the `ConditionalTask` re-triggers the `fetch_task` to find more events.
    -   **If False**: The condition is not met, and the workflow proceeds to the next step.
3.  **`summary_task`**: The `Summary Creator` agent takes the final list of events (from either the first or second fetch) and creates a concise summary.
