"""Pytest configuration and fixtures."""

import pytest
from unittest.mock import MagicMock, patch

# This makes the test directory a Python package
# and allows for relative imports in test files

@pytest.fixture(autouse=True)
def mock_environment_vars():
    """Mock environment variables for testing."""
    with patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test_openai_key',
        'GOOGLE_API_KEY': 'test_google_key',
        'SERPER_API_KEY': 'test_serper_key',
        'LOG_LEVEL': 'ERROR'  # Suppress logging during tests
    }):
        yield

@pytest.fixture
def mock_crew():
    """Create a mock Crew instance for testing."""
    with patch('src.main.Crew') as mock_crew_class:
        mock_instance = MagicMock()
        mock_instance.kickoff.return_value = MagicMock(raw='Test result')
        mock_crew_class.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def mock_llms():
    """Mock the LLM classes."""
    with patch('src.main.ChatGoogleGenerativeAI') as mock_gemini, \
         patch('src.main.ChatOpenAI') as mock_openai:
        yield {
            'gemini': mock_gemini.return_value,
            'openai': mock_openai.return_value
        }

@pytest.fixture
def mock_tools():
    """Mock the tool classes."""
    with patch('src.main.SerperDevTool') as mock_search, \
         patch('src.main.ScrapeWebsiteTool') as mock_scrape:
        yield {
            'search': mock_search.return_value,
            'scrape': mock_scrape.return_value
        }
