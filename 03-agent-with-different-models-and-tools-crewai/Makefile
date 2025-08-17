.PHONY: install test lint format clean run docker-build docker-run

# Variables
PYTHON = python3
PIP = pip3
DOCKER = docker

# Install dependencies
install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

# Install development dependencies
dev-install:
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e ".[dev]"

# Run tests
test:
	pytest tests/ -v --cov=src --cov-report=term-missing

# Run linter
lint:
	flake8 src/ tests/
	black --check src/ tests/
	isort --check-only src/ tests/
	mypy src/ tests/

# Format code
format:
	black src/ tests/
	isort src/ tests/

# Clean up
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '*.pyc' -delete
	find . -type d -name '*.pyo' -delete
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .coverage .mypy_cache .pytest_cache htmlcov

# Run the application
run:
	$(PYTHON) -m src.main

# Build Docker image
docker-build:
	$(DOCKER) build -t multi-model-crew .

# Run Docker container
docker-run:
	$(DOCKER) run --env-file .env multi-model-crew

# Run the application with a specific topic
run-topic:
	$(PYTHON) -m src.main "$(topic)"
