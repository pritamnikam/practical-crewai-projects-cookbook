# 08: Advanced Crew Execution Methods in CrewAI

This project demonstrates advanced methods for executing crews in CrewAI, showcasing how to run tasks asynchronously and how to process a batch of inputs sequentially.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running Crews Asynchronously](#running-crews-asynchronously)
  - [Running a Crew with Batch Inputs](#running-a-crew-with-batch-inputs)
- [How It Works](#how-it-works)
  - [Asynchronous Execution](#asynchronous-execution)
  - [Batch Execution](#batch-execution)

## Project Structure

The project is organized into a modular `src` directory:

```
08-agent-kickoff-crewai/
├── src/
│   ├── __init__.py
│   ├── config.py       # Handles API keys and environment variables
│   ├── crew.py         # Defines the analysis crew
│   └── main.py         # Main script to run the execution examples
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

### Installation

1.  **Clone the repository** (if you haven't already).

2.  **Navigate to the project directory**:
    ```bash
    cd 08-agent-kickoff-crewai
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
    -   Add your OpenAI API key to the `.env` file:
        ```
        OPENAI_API_KEY="your-openai-api-key"
        ```

## Usage

The `main.py` script accepts a command-line argument to specify which execution method to demonstrate.

### Running Crews Asynchronously

This example runs two crews in parallel: one using `kickoff_async` and another using a standard `kickoff` call wrapped to run concurrently.

```bash
python -m src.main async
```

### Running a Crew with Batch Inputs

This example runs a single crew sequentially for each item in a list of inputs using `kickoff_for_each`.

```bash
python -m src.main batch
```

## How It Works

### Asynchronous Execution

The `run_async_crews` function demonstrates how to leverage Python's `asyncio` library to run multiple crew operations concurrently. One crew is explicitly set to run its tasks asynchronously (`async_execution=True`) and is started with `await crew.kickoff_async()`. A second, synchronous crew is run in a separate thread using `loop.run_in_executor` to prevent it from blocking the main asynchronous event loop.

### Batch Execution

The `run_for_each_crew` function shows how to use the `kickoff_for_each` method. This method takes a list of input dictionaries and executes the crew's tasks once for each dictionary in the list, returning an aggregated list of results. This is useful for batch processing a collection of similar tasks.
