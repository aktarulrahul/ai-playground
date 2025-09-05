# AI Workspace

This repository contains various AI, Machine Learning, and Deep Learning projects including NLP, Computer Vision, and deployment examples.

## 🚀 Quick Start with UV

This project uses [UV](https://github.com/astral-sh/uv) for fast Python package and project management. UV is a drop-in replacement for pip, pip-tools, and virtualenv, offering significantly faster performance.

### Prerequisites

Install UV first:

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

## 📋 UV Workflow Guide

### 1. Creating a Virtual Environment

UV makes it incredibly simple to create a virtual environment. Navigate to your project directory and run:

```bash
uv venv
```

This creates a `.venv` directory in your project folder, containing an isolated Python environment.

If you want to specify a Python version:

```bash
uv venv --python 3.11
```

### 2. Activating the Virtual Environment

To activate the virtual environment, use:

```bash
# For Linux/Mac
source .venv/bin/activate

# For Windows
.venv\Scripts\activate
```

### 3. Installing Dependencies

Once the environment is active, you can install packages using UV's pip interface:

```bash
uv pip install requests
```

To add dependencies to your `pyproject.toml` file for better reproducibility:

```bash
uv add requests
```

To generate `pyproject.toml` file you need to use the below command - it will create several files:

```bash
uv init
```

### 4. Freezing Dependencies

To generate a list of installed dependencies:

```bash
uv pip freeze > requirements.txt
```

For projects using `pyproject.toml`, UV automatically manages dependencies and creates a `uv.lock` file to lock versions.

### 5. Deactivating and Removing Environments

Deactivate the virtual environment:

```bash
uv deactivate
```

Remove the virtual environment:

```bash
uv remove
```

## 🔄 Migrating Existing Projects to UV

If you have an existing project with a virtualenv setup, you can easily migrate it to UV:

1. Navigate to your project directory
2. Initialize UV:
   ```bash
   uv init
   ```
3. Convert dependencies:
   ```bash
   uv add -r requirements.txt
   ```

This creates a `pyproject.toml` and `uv.lock` file, making your project UV-compatible.

## ⚡ Advanced Features of UV

### 1. Managing Python Versions

UV can manage multiple Python versions seamlessly. To install a specific version:

```bash
uv python install 3.10
```

To switch between versions:

```bash
uv python use 3.10
```

### 2. Reproducible Environments

UV ensures reproducibility by locking dependencies in a `uv.lock` file. This guarantees that all team members and deployment environments use the same package versions.

To lock dependencies declared in a `pyproject.toml`:

```bash
uv pip compile pyproject.toml -o requirements.txt
```

> **Note:** By default, the `uv pip compile` output is just displayed and the `--output-file` / `-o` argument is needed to write to a file.

To lock dependencies declared in a `requirements.in`:

```bash
uv pip compile requirements.in -o requirements.txt
```

To lock dependencies declared in multiple files:

```bash
uv pip compile pyproject.toml requirements-dev.in -o requirements-dev.txt
```

### 3. Global Tools

Install global tools like `black` or `ruff` without polluting your project environment:

```bash
uv tool install black
```

## 🎯 Why Choose UV?

UV stands out for its speed, simplicity, and versatility. Here's why you should consider switching to UV for virtual environment management:

- **Speed**: UV is significantly faster than traditional tools, saving you time during development
- **Unified Workflow**: No need to juggle multiple tools; UV handles everything
- **Reproducibility**: Ensures consistent environments across machines and deployments
- **Ease of Use**: Intuitive commands make it beginner-friendly

## 📁 Project Structure

```
ai/
├── Generative-AI-Masters--NLP-Transformers -Gen-AI/
│   ├── Codes/                    # NLP and ML code examples
│   ├── Deep Learning - Resources/ # Deep learning projects
│   ├── Deployment/               # Model deployment examples
│   └── Presentations/            # Course presentations
├── NLP/                          # Natural Language Processing projects
├── n8n/                          # n8n workflow automation
├── python-refresher/             # Python fundamentals
└── test/                         # Test files
```

## 🛠️ Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aktarulrahul/ai-playground.git
   cd ai-playground
   ```

2. **Set up the environment:**

   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   uv init  # Initialize project with pyproject.toml
   uv add jupyter pandas numpy scikit-learn tensorflow torch
   ```

4. **Start exploring:**
   ```bash
   jupyter notebook
   ```

## 📚 Contents

### NLP Projects

- Text preprocessing and tokenization
- Bag of Words and TF-IDF implementations
- Named Entity Recognition (NER)
- Word2Vec and pre-trained models
- LSTM and GRU practical implementations

### Deep Learning

- Convolutional Neural Networks (CNN)
- Autoencoders for X-ray image analysis
- Pre-trained model implementations
- Image classification and augmentation
- Stock prediction using LSTM

### Deployment

- Streamlit applications
- Model deployment examples
- Breast cancer prediction system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Useful Links

- [UV Documentation](https://github.com/astral-sh/uv)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)

---

**Happy Coding! 🚀**
