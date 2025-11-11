# Python FastAPI Monorepo

A professional FastAPI monorepo with PostgreSQL, testing, and modern development practices.

## 🚀 Features

- **FastAPI** - Modern, fast web framework
- **PostgreSQL** - Production-ready database
- **Async/Await** - High-performance async operations
- **Pydantic** - Data validation and serialization
- **Dependency Injection** - Clean architecture patterns
- **Testing** - Comprehensive test suite with pytest
- **OpenAPI** - Auto-generated API documentation
- **Environment Management** - Secure configuration with .env

## 📁 Project Structure

```
Python-AIAgents/
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── requirements.txt          # Root dependencies
├── pyproject.toml           # Project configuration
├── docker-compose.yml       # Docker setup
├── Makefile                 # Development commands
├── week-1/                  # Week 1: Python basics
│   ├── async_await_asyncio.py
│   ├── cli_app_aiohttp.py
│   ├── requirements.txt     # Week 1 dependencies
│   ├── venv/                # Week 1 virtual environment
│   └── ...
├── week-2/                  # Week 2: FastAPI & Databases
│   ├── main.py              # FastAPI application
│   ├── db.py                # Database configuration
│   ├── schemas.py           # Pydantic models
│   ├── deps.py              # Dependency injection
│   ├── test_main.py         # Test suite
│   ├── test_db.py           # Test database config
│   ├── requirements.txt     # Week 2 dependencies
│   ├── env.example          # Environment template
│   ├── venv/                # Week 2 virtual environment
│   └── .env                 # Environment variables
├── week-3/                  # Week 3: FastAPI Backend
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Week 3 dependencies
│   ├── env.example          # Environment template
│   ├── test_main.py         # Test suite
│   ├── venv/                # Week 3 virtual environment
│   └── .env                 # Environment variables
├── week-4/                  # Week 4: FastAPI Backend
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Week 4 dependencies
│   ├── env.example          # Environment template
│   ├── test_main.py         # Test suite
│   ├── venv/                # Week 4 virtual environment
│   └── .env                 # Environment variables
├── week-5/                  # Week 5: FastAPI Backend
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Week 5 dependencies
│   ├── env.example          # Environment template
│   ├── test_main.py         # Test suite
│   ├── venv/                # Week 5 virtual environment
│   └── .env                 # Environment variables
├── week-6/                  # Week 6: FastAPI Backend
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Week 6 dependencies
│   ├── env.example          # Environment template
│   ├── test_main.py         # Test suite
│   ├── venv/                # Week 6 virtual environment
│   └── .env                 # Environment variables
└── docs/                    # Documentation
    ├── api.md
    └── deployment.md
```

## 🛠️ Setup

### Prerequisites

- Python 3.12
- PostgreSQL
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd Python-AIAgents

   # Ensure Python 3.12 is available
   python3.12 --version
   ```

2. **One-command setup**

   ```bash
   # This creates separate virtual environments for each week and installs all dependencies
   make setup-venv
   ```

3. **Set up environment variables**

   ```bash
   # For each week, copy the environment template
   cd week-2 && cp env.example .env
   cd week-3 && cp env.example .env
   cd week-4 && cp env.example .env
   cd week-5 && cp env.example .env
   cd week-6 && cp env.example .env

   # Edit each .env file with your specific configuration
   ```

4. **Run the application**

   ```bash
   # Run specific week
   make run-week-2  # Runs week-2 on port 8002
   make run-week-3  # Runs week-3 on port 8003
   # ... etc

   # Or run directly
   uvicorn week-2.main:app --reload --port 8002
   ```

**Note:** Each week has its own isolated virtual environment!

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific week tests
make test-week-1  # Test week 1
make test-week-2  # Test week 2
make test-week-3  # Test week 3
make test-week-4  # Test week 4
make test-week-5  # Test week 5
make test-week-6  # Test week 6

# Run with coverage
pytest --cov=week-2
```

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🐳 Docker Support

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in development mode
docker-compose -f docker-compose.dev.yml up
```

## 📝 Development

### Code Style

This project uses:

- **Black** - Code formatting
- **isort** - Import sorting
- **flake8** - Linting
- **mypy** - Type checking

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## 🚀 Deployment

See [docs/deployment.md](docs/deployment.md) for deployment instructions.

## 📄 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📞 Support

For questions and support, please open an issue on GitHub.
