# Virtual Environment Setup Guide

## 🎯 Separate Virtual Environments for Each Week

Your 6-week FastAPI monorepo now has **separate virtual environments for each week**!

### Quick Start (3 steps)

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd Python-AIAgents

# 2. One command setup
make setup-venv

# 3. Run any week
make run-week-2
```

**That's it!** Each week has its own isolated environment.

## 🔧 How It Works

### Virtual Environment Management

The Makefile now automatically:

1. **Creates separate venv for each week** - `week-X/venv/`
2. **Activates the specific week's venv** - For each command
3. **Installs dependencies** - In the week's own environment
4. **Runs commands** - With the week's isolated Python environment

### Key Commands

```bash
# Setup everything
make setup-venv

# Check venv status
make check-venv

# Activate and show info
make activate-venv

# Run any week (uses its own venv)
make run-week-2
make run-week-3
# ... etc

# Test any week (uses its own venv)
make test-week-2
make test-week-3
# ... etc
```

## 📋 What `make setup-venv` Does

1. **Creates separate virtual environments** for each week with `python3.12`
2. **Installs dependencies** in each week's own environment
3. **Sets up isolated environments** for immediate use
4. **Each week is completely independent**

## 🔍 Manual Commands (if needed)

If you prefer manual control:

```bash
# Create venv for specific week manually
cd week-2
python3.12 -m venv venv

# Activate manually
source venv/bin/activate

# Check Python
which python
python --version

# Install manually
pip install -r requirements.txt
```

## 🚀 Benefits

- **Complete isolation** between weeks
- **Independent dependency management** for each week
- **No conflicts** between different week requirements
- **One-command setup** for new developers
- **Automatic dependency installation** for each week
- **Cross-platform compatibility** (macOS, Linux, Windows)

## 🔧 Configuration

You can customize the setup in the Makefile:

```makefile
# Virtual environment configuration
PYTHON_VERSION = python3.12
```

Each week gets its own `venv/` directory inside the week folder.

## 🐛 Troubleshooting

### If venv creation fails:

```bash
# Check Python version
python3.12 --version

# Try different Python version
# Edit Makefile: PYTHON_VERSION = python3.11
```

### If dependencies fail to install:

```bash
# Check pip
source venv/bin/activate && pip --version

# Upgrade pip
source venv/bin/activate && pip install --upgrade pip
```

### If commands don't work:

```bash
# Check venv exists for specific week
ls -la week-2/venv/

# Recreate venv for specific week
rm -rf week-2/venv
make setup-week-2-venv
```

## 📚 Next Steps

After setup:

1. **Set up environment files** (optional):

   ```bash
   python scripts/manage_weeks.py setup --all
   ```

2. **Run any week**:

   ```bash
   make run-week-2  # Tea API with PostgreSQL
   make run-week-3  # Basic FastAPI
   ```

3. **Test any week**:

   ```bash
   make test-week-2
   make test-week-3
   ```

4. **Access APIs**:
   - Week 2: http://localhost:8002/docs
   - Week 3: http://localhost:8003
   - etc.

## 🎉 Success!

Your 6-week FastAPI monorepo now has **complete isolation** with separate virtual environments for each week!
