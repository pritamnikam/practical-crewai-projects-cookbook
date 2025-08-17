# ReAct Agent Example with LangChain

This project demonstrates how to use the ReAct (Reason + Act) agent architecture with the [LangChain](https://python.langchain.com/) framework and OpenAI. It includes a practical example that leverages external tools and prompts from LangChain Hub.

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
    ├── agent.py        # Agent definition and logic
    ├── config.py       # Configuration and environment handling
    └── main.py         # Main application entry point
```

## Features

- Modular code structure with separation of concerns.
- Integration with LangChain Hub for dynamic prompts.
- Use of Tavily for real-time search results.
- Containerized deployment with Docker.

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- API keys for:
  - OpenAI
  - Tavily
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
    TAVILY_API_KEY=your_tavily_api_key
    # Optional, for LangSmith tracing
    # LANGCHAIN_API_KEY=your_langchain_api_key
    # LANGCHAIN_PROJECT=your_project_name
    ```

4.  **Run the application:**
    ```bash
    python -m src.main "Your question here"
    ```

## Docker Support

You can also build and run the application using Docker:

1.  **Build the image:**
    ```bash
    docker build -t react-langchain-agent .
    ```

2.  **Run the container:**
    ```bash
    docker run --env-file .env react-langchain-agent "Your question here"
    ```

## References

- [LangChain Documentation](https://python.langchain.com/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
