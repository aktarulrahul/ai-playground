# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd Python-AIAgents

# Ensure Python 3.12 is available
python3.12 --version
```

### 2. One-Command Setup

```bash
# This will create separate virtual environments for each week and install all dependencies
make setup-venv
```

### 3. Setup Environment Files (Optional)

```bash
# Setup all weeks at once
python scripts/manage_weeks.py setup --all

# Or setup individual weeks
python scripts/manage_weeks.py setup --week 2
```

### 4. Run Any Week

```bash
# Run week 2 (Tea API with PostgreSQL)
make run-week-2

# Run week 3
make run-week-3

# Or use the management script
python scripts/manage_weeks.py run --week 2

# Each week has its own isolated virtual environment!
```

### 5. Test Any Week

```bash
# Test week 2
make test-week-2

# Test all weeks
python scripts/manage_weeks.py test --all

# Each week has its own isolated virtual environment!
```

## 📋 Available Commands

### Make Commands

```bash
make help                    # Show all available commands
make setup-venv             # Create venv and install all dependencies
make activate-venv          # Activate venv and show Python info
make install-all-weeks       # Install dependencies for all weeks
make run-week-1             # Run week 1 on port 8001
make run-week-2             # Run week 2 on port 8002
make run-week-3             # Run week 3 on port 8003
make run-week-4             # Run week 4 on port 8004
make run-week-5             # Run week 5 on port 8005
make run-week-6             # Run week 6 on port 8006
make test-week-1            # Test week 1
make test-week-2            # Test week 2
# ... etc for all weeks
```

### Management Script

```bash
python scripts/manage_weeks.py list          # List all weeks
python scripts/manage_weeks.py install --all # Install all weeks
python scripts/manage_weeks.py setup --all   # Setup env for all weeks
python scripts/manage_weeks.py run --week 2  # Run week 2
python scripts/manage_weeks.py test --week 2 # Test week 2
```

## 🌐 Access Your APIs

Each week runs on a different port:

- **Week 1**: http://localhost:8001 (Python basics)
- **Week 2**: http://localhost:8002 (FastAPI + PostgreSQL)
- **Week 3**: http://localhost:8003 (FastAPI Backend)
- **Week 4**: http://localhost:8004 (FastAPI Backend)
- **Week 5**: http://localhost:8005 (FastAPI Backend)
- **Week 6**: http://localhost:8006 (FastAPI Backend)

### API Documentation

- **Swagger UI**: http://localhost:8002/docs (for week 2)
- **ReDoc**: http://localhost:8002/redoc (for week 2)

## 🔧 Development Workflow

1. **One-time setup**: `make setup-venv`
2. **Choose a week** to work on
3. **Run the app**: `make run-week-X`
4. **Write tests**: Edit `week-X/test_main.py`
5. **Test your code**: `make test-week-X`

**That's it!** Each week has its own isolated virtual environment.

## 🐳 Docker (Optional)

```bash
# Run with Docker Compose
make docker-run

# Build Docker image
make docker-build
```

## 📚 What's in Each Week?

- **Week 1**: Python basics, async/await, CLI tools
- **Week 2**: FastAPI with PostgreSQL, Pydantic models, testing
- **Week 3**: FastAPI Backend (ready for your features)
- **Week 4**: FastAPI Backend (ready for your features)
- **Week 5**: FastAPI Backend (ready for your features)
- **Week 6**: FastAPI Backend (ready for your features)

**Each week has its own isolated virtual environment!** 🎯

## 🆘 Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Each week has its own `requirements.txt`, `env.example`, and `venv/`
- Use `make help` to see all available commands
- Use `python scripts/manage_weeks.py list` to see all weeks
- **Python 3.12** is required for all virtual environments
