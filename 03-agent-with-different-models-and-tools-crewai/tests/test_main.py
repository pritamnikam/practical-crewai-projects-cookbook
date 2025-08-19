"""Tests for the refactored multi-model application."""

import pytest
from unittest.mock import patch, MagicMock

# --- Fixtures ---

@pytest.fixture
def mock_environment_vars():
    with patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test_openai_key',
        'GOOGLE_API_KEY': 'test_google_key',
        'SERPER_API_KEY': 'test_serper_key'
    }):
        yield

@pytest.fixture
def mock_llms():
    with patch('src.llms.LLM') as mock_llm_class:
        mock_llm_instance = MagicMock()
        mock_llm_class.return_value = mock_llm_instance
        yield mock_llm_instance

@pytest.fixture
def mock_tools():
    with patch('src.tools.Tool') as mock_tool_class:
        mock_tool_instance = MagicMock()
        mock_tool_class.return_value = mock_tool_instance
        yield mock_tool_instance

@pytest.fixture
def mock_crew():
    with patch('src.crew.Crew') as mock_crew_class:
        mock_crew_instance = MagicMock()
        mock_crew_class.return_value = mock_crew_instance
        yield mock_crew_instance

# --- Test Config Module ---

def test_config_loading(mock_environment_vars):
    """Test that the configuration loads correctly."""
    from src.config import app_config
    assert app_config['OPENAI_API_KEY'] == 'test_openai_key'
    assert app_config['GOOGLE_API_KEY'] == 'test_google_key'
    assert app_config['SERPER_API_KEY'] == 'test_serper_key'

@patch.dict('os.environ', {}, clear=True)
def test_missing_env_vars():
    """Test that missing environment variables raise a ValueError."""
    with pytest.raises(ValueError) as excinfo:
        # We need to re-import the module to trigger the config load again
        import importlib
        from src import config
        importlib.reload(config)
    assert 'Missing required environment variables' in str(excinfo.value)

# --- Test Crew Module ---

def test_create_multi_model_crew(mock_llms, mock_tools):
    """Test the creation of the multi-model crew."""
    from src.crew import create_multi_model_crew
    agents, tasks = create_multi_model_crew()
    
    assert len(agents) == 2
    assert len(tasks) == 2
    assert agents[0].role == 'Senior Researcher'
    assert agents[1].role == 'Writer'

def test_run_crew(mock_crew):
    """Test the run_crew function."""
    from src.crew import run_crew
    topic = "test topic"
    result = run_crew(topic)
    
    assert result['topic'] == topic
    assert result['result'] == 'Test result'
    mock_crew.kickoff.assert_called_once_with(inputs={'topic': topic})

# --- Test Main Module ---

@patch('src.main.run_crew')
def test_main_success(mock_run_crew):
    """Test the main function's successful execution path."""
    from src.main import main
    mock_run_crew.return_value = {'result': 'Final article'}
    
    with patch('builtins.print') as mock_print:
        main()
        # Verify that run_crew was called
        mock_run_crew.assert_called_once()
        # Verify that the result was printed
        mock_print.assert_any_call("\n" + "="*80)
        mock_print.assert_any_call('Final article')

@patch('src.main.run_crew', side_effect=Exception("Test error"))
def test_main_exception(mock_run_crew):
    """Test the main function's exception handling."""
    from src.main import main
    with pytest.raises(Exception) as excinfo:
        main()
    assert "Test error" in str(excinfo.value)
