"""Tests for the main application."""

import pytest
import os
from unittest.mock import MagicMock, patch
from src.main import MultiModelCrew


class TestMultiModelCrew:
    """Test cases for MultiModelCrew class."""

    @patch('src.main.ChatGoogleGenerativeAI')
    @patch('src.main.ChatOpenAI')
    @patch('src.main.SerperDevTool')
    @patch('src.main.ScrapeWebsiteTool')
    @patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test_openai_key',
        'GOOGLE_API_KEY': 'test_google_key',
        'SERPER_API_KEY': 'test_serper_key'
    })
    def test_initialization(self, mock_scrape_tool, mock_search_tool, 
                          mock_openai, mock_gemini):
        """Test that the crew initializes with all required components."""
        # Setup mocks
        mock_search_tool.return_value = 'search_tool'
        mock_scrape_tool.return_value = 'scrape_tool'
        
        # Initialize the crew
        crew = MultiModelCrew()
        
        # Assert tools and models were initialized
        assert hasattr(crew, 'search_tool')
        assert hasattr(crew, 'scrape_tool')
        assert hasattr(crew, 'gemini')
        assert hasattr(crew, 'gpt')
        assert hasattr(crew, 'article_researcher')
        assert hasattr(crew, 'article_writer')
        assert hasattr(crew, 'research_task')
        assert hasattr(crew, 'writing_task')

    @patch('src.main.Crew')
    @patch.dict('os.environ', {
        'OPENAI_API_KEY': 'test_openai_key',
        'GOOGLE_API_KEY': 'test_google_key',
        'SERPER_API_KEY': 'test_serper_key'
    })
    def test_run_method(self, mock_crew_class):
        """Test the run method with a test topic."""
        # Setup mock
        mock_crew_instance = MagicMock()
        mock_crew_instance.kickoff.return_value = MagicMock(raw='Test result')
        mock_crew_class.return_value = mock_crew_instance
        
        # Initialize and run
        crew = MultiModelCrew()
        result = crew.run('test topic')
        
        # Assertions
        assert result['topic'] == 'test topic'
        assert result['result'] == 'Test result'
        mock_crew_instance.kickoff.assert_called_once()

    @patch.dict('os.environ', {}, clear=True)
    def test_missing_environment_variables(self):
        """Test that missing environment variables raise an error."""
        with pytest.raises(ValueError) as excinfo:
            MultiModelCrew()
        assert 'Missing required environment variables' in str(excinfo.value)

    @patch('src.main.load_dotenv')
    @patch('src.main.Path')
    def test_env_file_loading(self, mock_path, mock_load_dotenv):
        """Test that .env file is loaded if it exists."""
        # Setup mock
        mock_path.return_value.exists.return_value = True
        
        # Initialize
        MultiModelCrew()
        
        # Assert load_dotenv was called
        mock_load_dotenv.assert_called_once()

    def test_main_function(self):
        """Test the main function execution."""
        with patch('src.main.MultiModelCrew') as mock_crew_class:
            # Setup mock
            mock_instance = MagicMock()
            mock_instance.run.return_value = {
                'topic': 'test topic',
                'result': 'test result',
                'markdown': 'test markdown'
            }
            mock_crew_class.return_value = mock_instance
            
            # Import and run main
            from src.main import main
            
            # Test successful execution
            with patch('builtins.print') as mock_print:
                main()
                mock_print.assert_called()
            
            # Test exception handling
            mock_instance.run.side_effect = Exception('Test error')
            with patch('src.main.logger') as mock_logger:
                with pytest.raises(Exception):
                    main()
                mock_logger.error.assert_called_once()
