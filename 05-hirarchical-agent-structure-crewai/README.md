# CrewAI with Hierarchical Process

This project demonstrates how to build a multi-agent system using a hierarchical process in [CrewAI](https://docs.crewai.com/). The example features a crew of agents managed by a master agent, designed to research a topic and produce a comprehensive report.

## Project Structure

```
.
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore file
├── Dockerfile          # Container configuration
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── src/
    ├── __init__.py     # Makes src a Python package
    ├── crew.py         # Crew definition, including agents, tasks, and manager LLM
    ├── config.py       # Configuration and environment variable handling
    └── main.py         # Main application entry point
```

## Features

- **Hierarchical Process**: The crew is managed by a higher-level LLM that delegates tasks to specialized agents.
- **Modular Design**: Code is separated into modules for configuration, crew definition, and execution.
- **Dynamic Task Creation**: Tasks are created dynamically based on a command-line topic.
- **Containerized**: The application is fully containerized with Docker for easy deployment.

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- API keys for:
  - OpenAI
  - Serper
  - Groq
  - LangChain (optional, for tracing)

## Setup

1.  **Clone the repository**

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**

    Create a `.env` file in the project root and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    SERPER_API_KEY=your_serper_api_key
    GROQ_API_KEY=your_groq_api_key
    # Optional, for LangSmith tracing
    # LANGCHAIN_API_KEY=your_langchain_api_key
    # LANGCHAIN_PROJECT=your_project_name
    ```

## Running the Application

To run the crew, execute the main script from the project root and provide a topic as a command-line argument:

```bash
python -m src.main "The impact of AI on modern healthcare systems"
```

### Handling Missing Topics

If you run the script without a topic, the application will catch the error and provide guidance:

```bash
python -m src.main
# Output: Error: The 'topic' for the crew to research and write about cannot be empty. Please provide a topic.
#         Example: python -m src.main "Artificial Intelligence"
```

## Docker Support

You can also build and run the application using Docker:

1.  **Build the image:**
    ```bash
    docker build -t crewai-hierarchical-crew .
    ```

2.  **Run the container with a topic:**
    ```bash
    docker run --env-file .env crewai-hierarchical-crew "The Rise of Quantum Computing"
    ```

## References

- [CrewAI Documentation](https://docs.crewai.com/)
