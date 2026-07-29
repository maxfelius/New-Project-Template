# New-Project-Template

This is a repository template for starting new Python projects. It contains the minimum building blocks needed for a new application or data processing flow.

## Prerequisites

- Python 3.12+
- pip
- make (optional, for convenience commands)

## Quick Start

### Using Dev Container (Recommended)

1. Open this repository in VS Code
2. When prompted, click "Reopen in Container" to build and enter the Dev Container
3. The environment will be automatically set up with all dependencies

### Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Application

```bash
# Using make (recommended)
make run

# Or directly with Python
python -m app.src.main
python -m app.src.hello
```

### Run Tests

```bash
# Using make (recommended)
make test

# Or directly with pytest
python -m pytest app/test/ -v

# Run a specific test file
python -m pytest app/test/test_hello.py -v
```

## Project Structure

```
.
├── .devcontainer/          # VS Code Dev Container configuration
├── .vscode/               # VS Code workspace settings
├── .agent/                # AI agent instructions
├── app/
│   ├── src/               # Application source code
│   │   ├── __init__.py
│   │   ├── hello.py       # Hello world module
│   │   └── main.py        # Application entry point
│   └── test/              # Unit tests
│       ├── __init__.py
│       └── test_hello.py  # Test suite
├── Makefile               # Convenience commands
├── requirements.txt        # Python dependencies
├── LICENSE
└── README.md
```

## Development Environment

- **Python Version**: 3.12
- **Formatter**: Ruff
- **Linting**: Ruff, Pylance
- **Testing**: pytest
- **Pre-commit Hooks**: Code formatting and linting run on commit, tests run on push

## Pre-commit Setup

This project uses pre-commit hooks for code quality:

- **On `git commit`**: Ruff lint and format run automatically
- **On `git push`**: Tests run automatically (blocks push if tests fail)

To install the hooks:

```bash
# Install pre-commit hook (runs on git commit)
pre-commit install

# Install pre-push hook (runs on git push)
pre-commit install --hook-type pre-push
```

## Adding New Features

1. Add source files to `app/src/`
2. Add corresponding tests to `app/test/`
3. Add new dependencies to `requirements.txt`
4. Update the `Makefile` with any new convenience commands

# test
