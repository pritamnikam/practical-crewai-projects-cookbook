# CrewAI with Exception Handling

This project demonstrates how to build a multi-agent system using [CrewAI](https://docs.crewai.com/) that includes robust exception handling. The example features a crew of agents designed to research and write an article on a given topic, and it includes checks to prevent common issues like running the crew without a topic.

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
    ├── crew.py         # Crew definition, including agent and task creation
    ├── config.py       # Configuration and environment variable handling
    └── main.py         # Main application entry point with error handling
```

## Features

- **Modular Design**: Code is separated into modules for configuration, crew definition, and execution.
- **Error Handling**: The main script includes `try...except` blocks to gracefully handle missing inputs (e.g., no topic) and other potential runtime errors.
- **Dynamic Crew Creation**: The crew is assembled dynamically based on the provided topic.
- **Containerized**: The application is fully containerized with Docker for easy deployment and execution.

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

## Running the Application

To run the crew, execute the main script from the project root and provide a topic as a command-line argument:

```bash
python -m src.main "The Future of Artificial Intelligence"
```

### Handling Missing Topics

If you run the script without a topic, the application will catch the error and provide guidance:

```bash
python -m src.main
# Output: Error: The 'topic' for the crew to research and write about cannot be empty.
#         Please provide a topic to run the crew. Example: python -m src.main "Artificial Intelligence"
```

## Docker Support

You can also build and run the application using Docker:

1.  **Build the image:**
    ```bash
    docker build -t crewai-exception-handler .
    ```

2.  **Run the container with a topic:**
    ```bash
    docker run --env-file .env crewai-exception-handler "The Rise of Quantum Computing"
    ```

## References

- [CrewAI Documentation](https://docs.crewai.com/)
