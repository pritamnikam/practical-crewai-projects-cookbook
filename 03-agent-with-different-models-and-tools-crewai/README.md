# Multi-Model Agent Crew with CrewAI

This project demonstrates how to use [CrewAI](https://docs.crewai.com/) to coordinate multiple AI agents, each powered by different LLM providers (Gemini, GPT-4o), for collaborative content creation.

## Project Structure

```
.
├── .env.example                 # Example environment variables
├── .gitignore                  # Git ignore file
├── Dockerfile                  # Container configuration
├── README.md                   # This file
├── requirements.txt            # Python dependencies
└── src/
    └── main.py                 # Main application code
```

## Features

- Integration of multiple LLM providers (Gemini, GPT-4o)
- Task delegation between specialized AI agents
- Web search and content scraping capabilities
- Clean, modular code structure
- Containerized deployment

## Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)
- API keys for:
  - OpenAI
  - Google AI (Gemini)
  - Serper (for web search)

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your API keys
4. Run the application:
   ```bash
   python -m src.main
   ```

## Docker Support

Build and run with Docker:

```bash
docker build -t multi-model-crew .
docker run --env-file .env multi-model-crew
```

## Environment Variables

Create a `.env` file with the following variables:

```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_serper_api_key
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT
