# Separate Virtual Environments for Each Week

## 🎯 Overview

Your **6-week FastAPI monorepo** now uses **separate virtual environments** for each week, providing complete isolation and independence.

## 📁 Structure

```
Python-AIAgents/
├── week-1/
│   ├── venv/                 # Week 1's isolated environment
│   ├── requirements.txt      # Week 1's dependencies
│   └── ...
├── week-2/
│   ├── venv/                 # Week 2's isolated environment
│   ├── requirements.txt      # Week 2's dependencies
│   └── ...
├── week-3/
│   ├── venv/                 # Week 3's isolated environment
│   ├── requirements.txt      # Week 3's dependencies
│   └── ...
└── ... (weeks 4-6)
```

## 🚀 Benefits

### ✅ **Complete Isolation**

- Each week has its own Python environment
- No dependency conflicts between weeks
- Independent package management

### ✅ **Flexibility**

- Different Python versions per week (if needed)
- Different dependency versions per week
- Easy to experiment with new packages

### ✅ **Maintenance**

- Easy to recreate individual week environments
- Clear separation of concerns
- No shared state between weeks

## 🔧 Commands

### Setup

```bash
# Create all week virtual environments
make setup-venv

# Create specific week virtual environment
make setup-week-2-venv
make setup-week-3-venv
# ... etc
```

### Check Status

```bash
# Check all virtual environments
make check-venv

# Show activation commands
make activate-venv
```

### Run & Test

```bash
# Run specific week (uses its own venv)
make run-week-2
make run-week-3
# ... etc

# Test specific week (uses its own venv)
make test-week-2
make test-week-3
# ... etc
```

## 🔍 Manual Activation

To manually work with a specific week:

```bash
# Activate week 2's virtual environment
cd week-2
source venv/bin/activate

# Check Python info
which python
python --version

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

## 📋 What Each Command Does

### `make setup-venv`

1. Creates `week-1/venv/` with `python3.12`
2. Creates `week-2/venv/` with `python3.12`
3. Creates `week-3/venv/` with `python3.12`
4. ... continues for all weeks
5. Installs dependencies in each week's environment

### `make run-week-X`

1. Ensures `week-X/venv/` exists
2. Activates `week-X/venv/bin/activate`
3. Runs the FastAPI app from `week-X/`
4. Uses the week's isolated environment

### `make test-week-X`

1. Ensures `week-X/venv/` exists
2. Activates `week-X/venv/bin/activate`
3. Runs tests from `week-X/`
4. Uses the week's isolated environment

## 🎯 Use Cases

### **Learning Path**

- Week 1: Basic Python with minimal dependencies
- Week 2: FastAPI with PostgreSQL dependencies
- Week 3: Advanced FastAPI features
- Each week builds on the previous without conflicts

### **Experimentation**

- Try different package versions per week
- Test new libraries without affecting other weeks
- Easy rollback by recreating individual venv

### **Team Development**

- Different developers can work on different weeks
- No shared dependency conflicts
- Clear boundaries between week features

## 🔧 Configuration

### Python Version

Edit `Makefile`:

```makefile
PYTHON_VERSION = python3.12
```

### Custom Dependencies

Each week can have completely different `requirements.txt`:

```bash
# Week 2 might need PostgreSQL
week-2/requirements.txt:
  fastapi
  uvicorn
  asyncpg
  databases

# Week 3 might need Redis
week-3/requirements.txt:
  fastapi
  uvicorn
  redis
  aioredis
```

## 🐛 Troubleshooting

### Recreate Specific Week Environment

```bash
# Remove week 2's venv
rm -rf week-2/venv

# Recreate it
make setup-week-2-venv
```

### Check Dependencies

```bash
# Check what's installed in week 2
cd week-2
source venv/bin/activate
pip list
```

### Debug Environment Issues

```bash
# Check Python path
cd week-2
source venv/bin/activate
which python
python --version
```

## 🎉 Success!

Your **6-week FastAPI monorepo** now provides:

- ✅ **Complete isolation** between weeks
- ✅ **Independent dependency management**
- ✅ **Easy setup and maintenance**
- ✅ **Flexible development workflow**

Each week is now a **self-contained, independent project** within the monorepo! 🚀
