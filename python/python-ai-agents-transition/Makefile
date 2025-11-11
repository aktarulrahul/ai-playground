.PHONY: help setup-venv check-venv activate-venv install install-dev test test-cov lint format type-check clean run run-dev docker-build docker-run docs setup-all-week-venvs setup-week-1-venv setup-week-2-venv setup-week-3-venv setup-week-4-venv setup-week-5-venv setup-week-6-venv

# Virtual environment configuration
PYTHON_VERSION = python3.12

# Default target
help:
	@echo "Available commands:"
	@echo "  setup-venv   - Create separate virtual environments for all weeks"
	@echo "  check-venv   - Check status of all week virtual environments"
	@echo "  activate-venv - Show how to activate each week's virtual environment"
	@echo "  install      - Install root dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  install-all-weeks - Install dependencies for all weeks"
	@echo "  test         - Run tests for week 2"
	@echo "  test-cov     - Run tests with coverage for week 2"
	@echo "  lint         - Run linting for week 2"
	@echo "  format       - Format code for week 2"
	@echo "  type-check   - Run type checking for week 2"
	@echo "  clean        - Clean up cache files"
	@echo "  run          - Run week 2 FastAPI application"
	@echo "  run-dev      - Run week 2 FastAPI application in development mode"
	@echo "  run-week-X   - Run specific week (X = 1-6) with its own venv"
	@echo "  test-week-X  - Test specific week (X = 1-6) with its own venv"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run with Docker Compose"
	@echo "  docs         - Build documentation"

# Virtual environment management
setup-venv: setup-all-week-venvs install-all-weeks
	@echo "✅ All week virtual environments setup complete!"
	@echo "Each week has its own isolated virtual environment"

setup-all-week-venvs: setup-week-1-venv setup-week-2-venv setup-week-3-venv setup-week-4-venv setup-week-5-venv setup-week-6-venv
	@echo "All week virtual environments created!"

setup-week-1-venv:
	@if [ ! -d "week-1/venv" ]; then \
		echo "Creating virtual environment for week 1..."; \
		cd week-1 && $(PYTHON_VERSION) -m venv venv; \
		echo "Week 1 virtual environment created successfully!"; \
	else \
		echo "Week 1 virtual environment already exists."; \
	fi

setup-week-2-venv:
	@if [ ! -d "week-2/venv" ]; then \
		echo "Creating virtual environment for week 2..."; \
		cd week-2 && $(PYTHON_VERSION) -m venv venv; \
		echo "Week 2 virtual environment created successfully!"; \
	else \
		echo "Week 2 virtual environment already exists."; \
	fi

setup-week-3-venv:
	@if [ ! -d "week-3/venv" ]; then \
		echo "Creating virtual environment for week 3..."; \
		cd week-3 && $(PYTHON_VERSION) -m venv venv; \
		echo "Week 3 virtual environment created successfully!"; \
	else \
		echo "Week 3 virtual environment already exists."; \
	fi

setup-week-4-venv:
	@if [ ! -d "week-4/venv" ]; then \
		echo "Creating virtual environment for week 4..."; \
		cd week-4 && $(PYTHON_VERSION) -m venv venv; \
		echo "Week 4 virtual environment created successfully!"; \
	else \
		echo "Week 4 virtual environment already exists."; \
	fi

setup-week-5-venv:
	@if [ ! -d "week-5/venv" ]; then \
		echo "Creating virtual environment for week 5..."; \
		cd week-5 && $(PYTHON_VERSION) -m venv venv; \
		echo "Week 5 virtual environment created successfully!"; \
	else \
		echo "Week 5 virtual environment already exists."; \
	fi

setup-week-6-venv:
	@if [ ! -d "week-6/venv" ]; then \
		echo "Creating virtual environment for week 6..."; \
		cd week-6 && $(PYTHON_VERSION) -m venv venv; \
		echo "Week 6 virtual environment created successfully!"; \
	else \
		echo "Week 6 virtual environment already exists."; \
	fi

check-venv:
	@echo "Checking all week virtual environments..."
	@for week in 1 2 3 4 5 6; do \
		if [ -d "week-$$week/venv" ]; then \
			echo "✅ Week $$week: venv exists"; \
		else \
			echo "❌ Week $$week: venv missing"; \
		fi; \
	done

activate-venv:
	@echo "Available virtual environments:"
	@for week in 1 2 3 4 5 6; do \
		if [ -d "week-$$week/venv" ]; then \
			echo "Week $$week: source week-$$week/venv/bin/activate"; \
		fi; \
	done

# Installation
install:
	@echo "Installing root dependencies..."
	@pip install -r requirements.txt
	@echo "Root dependencies installed successfully!"

install-dev:
	@echo "Installing development dependencies..."
	@pip install -r requirements.txt
	@pip install -e ".[dev]"
	@echo "Development dependencies installed successfully!"

# Testing
test: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && pytest

test-cov: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && pytest --cov=. --cov-report=html --cov-report=term-missing

# Code quality
lint: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && flake8 . --max-line-length=88 --extend-ignore=E203,W503

format: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && black .
	@cd week-2 && source venv/bin/activate && isort .

type-check: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && mypy .

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +

# Running the application
run: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8000

run-dev: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Week-specific commands
run-week-1: setup-week-1-venv
	@cd week-1 && source venv/bin/activate && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001

run-week-2: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8002

run-week-3:
	@cd week-3 && source venv/bin/activate && which python && pip install -r requirements.txt && uvicorn main:app --reload --host 0.0.0.0 --port 8003

run-week-4: setup-week-4-venv
	@cd week-4 && source venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8004

run-week-5: setup-week-5-venv
	@cd week-5 && source venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8005

run-week-6: setup-week-6-venv
	@cd week-6 && source venv/bin/activate && uvicorn main:app --reload --host 0.0.0.0 --port 8006

# Test specific weeks
test-week-1: setup-week-1-venv
	@cd week-1 && source venv/bin/activate && pytest

test-week-2: setup-week-2-venv
	@cd week-2 && source venv/bin/activate && pytest

test-week-3: setup-week-3-venv
	@cd week-3 && source venv/bin/activate && pytest

test-week-4: setup-week-4-venv
	@cd week-4 && source venv/bin/activate && pytest

test-week-5: setup-week-5-venv
	@cd week-5 && source venv/bin/activate && pytest

test-week-6: setup-week-6-venv
	@cd week-6 && source venv/bin/activate && pytest

# Install dependencies for specific weeks
install-week-1: setup-week-1-venv
	@echo "Installing week 1 dependencies..."
	@cd week-1 && source venv/bin/activate && pip install -r requirements.txt

install-week-2: setup-week-2-venv
	@echo "Installing week 2 dependencies..."
	@cd week-2 && source venv/bin/activate && pip install -r requirements.txt

install-week-3: setup-week-3-venv
	@echo "Installing week 3 dependencies..."
	@cd week-3 && source venv/bin/activate && pip install -r requirements.txt

install-week-4: setup-week-4-venv
	@echo "Installing week 4 dependencies..."
	@cd week-4 && source venv/bin/activate && pip install -r requirements.txt

install-week-5: setup-week-5-venv
	@echo "Installing week 5 dependencies..."
	@cd week-5 && source venv/bin/activate && pip install -r requirements.txt

install-week-6: setup-week-6-venv
	@echo "Installing week 6 dependencies..."
	@cd week-6 && source venv/bin/activate && pip install -r requirements.txt

# Install all weeks
install-all-weeks: install-week-1 install-week-2 install-week-3 install-week-4 install-week-5 install-week-6

# Docker
docker-build:
	docker build -t python-ai-agents .

docker-run:
	docker-compose up --build

# Documentation
docs:
	mkdocs build

# Pre-commit
pre-commit-install:
	pre-commit install

pre-commit-run:
	pre-commit run --all-files

# Database
db-migrate:
	# Add database migration commands here
	@echo "Database migration commands to be implemented"

db-seed:
	# Add database seeding commands here
	@echo "Database seeding commands to be implemented"

# Security
security-check:
	bandit -r week-2/
	safety check

# All checks
check: format lint type-check test
	@echo "All checks passed! ✅" 