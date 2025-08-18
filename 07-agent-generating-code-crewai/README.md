# 07: Code Generation & Debugging with CrewAI

This project demonstrates how to use CrewAI to perform two distinct software development tasks: generating new code and debugging existing code. It contains two separate crews that can be run independently.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Coding Crew](#running-the-coding-crew)
  - [Running the Debugging Crew](#running-the-debugging-crew)
- [How It Works](#how-it-works)
  - [Coding Crew](#coding-crew)
  - [Debugging Crew](#debugging-crew)

## Project Structure

The project is organized into a modular `src` directory:

```
07-agent-generating-code-crewai/
├── src/
│   ├── __init__.py
│   ├── config.py       # Handles API keys and environment variables
│   ├── crew.py         # Defines the agents and tasks for both crews
│   └── main.py         # Main script to run the crews
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
    cd 07-agent-generating-code-crewai
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

The `main.py` script accepts a command-line argument to specify which crew to run.

### Running the Coding Crew

This crew generates Python code to calculate the average of a list of numbers.

```bash
python -m src.main coding
```

### Running the Debugging Crew

This crew identifies and fixes a bug in a snippet of Python code.

```bash
python -m src.main debugging
```

## How It Works

### Coding Crew

-   **Agent**: `Python Data Analyst`
    -   **Goal**: Write and execute Python code to perform calculations.
-   **Task**: Given a list of ages, write and execute Python code to find the average and return the result in a specific format.

### Debugging Crew

-   **Agent**: `Python Debugger`
    -   **Goal**: Identify and fix issues in existing Python code.
-   **Task**: Given a buggy Python script that is supposed to square a list of numbers, identify the bug, fix it, and explain the correction.
