# CrewAI with Human-in-the-Loop Feedback

This project demonstrates how to incorporate human feedback into a multi-agent system using [CrewAI](https://docs.crewai.com/). The example features a crew that researches a YouTube video and writes an article, pausing to allow a human to review and provide input before finalizing the output.

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
    ├── crew.py         # Crew definition, including agents, tasks, and human feedback
    ├── config.py       # Configuration and environment variable handling
    └── main.py         # Main application entry point
```

## Features

- **Human-in-the-Loop**: The writing task is configured with `human_input=True`, pausing the crew to wait for user feedback.
- **Modular Design**: Code is separated into modules for configuration, crew definition, and execution.
- **Dynamic Inputs**: The YouTube URL and research topic are provided as command-line arguments.
- **Containerized**: The application is fully containerized with Docker for easy deployment.

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- An OpenAI API key.

## Setup

1.  **Clone the repository**

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**

    Create a `.env` file in the project root and add your API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    # Optional, for LangSmith tracing
    # LANGCHAIN_API_KEY=your_langchain_api_key
    # LANGCHAIN_PROJECT=your_project_name
    ```

## Running the Application

To run the crew, execute the main script from the project root and provide a YouTube URL and a topic as command-line arguments:

```bash
python -m src.main "<YOUTUBE_URL>" "<TOPIC>"
```

**Example:**
```bash
python -m src.main "https://www.youtube.com/watch?v=R0ds4Mwhy-8" "A summary of Educative's offerings"
```

When the process reaches the writing task, it will prompt for your feedback in the console. Provide your input to continue.

## Docker Support

You can also build and run the application using Docker:

1.  **Build the image:**
    ```bash
    docker build -t crewai-human-feedback .
    ```

2.  **Run the container:**
    ```bash
    docker run --env-file .env -it crewai-human-feedback "<YOUTUBE_URL>" "<TOPIC>"
    ```
    *Note: The `-it` flags are required to interact with the application for human feedback.*

## References

- [CrewAI Documentation on Human Input](https://docs.crewai.com/core-concepts/Tasks/#human-input)
