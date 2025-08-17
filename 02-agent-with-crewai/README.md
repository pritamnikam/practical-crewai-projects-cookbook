# Multi-Agent CrewAI Example

This project demonstrates how to use [CrewAI](https://docs.crewai.com/) to coordinate multiple agents for a real-world event planning scenario.

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
    ├── crew.py         # Crew definition and logic
    ├── config.py       # Configuration and environment handling
    └── main.py         # Main application entry point
```

## Features

- Modular code structure with separation of concerns.
- Multi-agent collaboration for a practical use case.
- Use of Serper for real-time search results.
- Containerized deployment with Docker.

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- API keys for:
  - OpenAI
  - Serper
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
    # Optional, for LangSmith tracing
    # LANGCHAIN_API_KEY=your_langchain_api_key
    # LANGCHAIN_PROJECT=your_project_name
    ```

4.  **Run the application:**
    ```bash
    python -m src.main --conference_name "Tech Conference 2024" --requirements "Capacity for 1000 people"
    ```

## Docker Support

You can also build and run the application using Docker:

1.  **Build the image:**
    ```bash
    docker build -t crewai-event-planner .
    ```

2.  **Run the container:**
    ```bash
    docker run --env-file .env crewai-event-planner --conference_name "Tech Conference 2024" --requirements "Capacity for 1000 people"
    ```

## References

- [CrewAI Documentation](https://docs.crewai.com/)
