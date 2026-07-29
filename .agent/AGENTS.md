# Repository: New Project Template

This is a Python project template with a Dev Container configuration for VS Code.

## Structure

```
.
├── .devcontainer/
│   └── devcontainer.json    # VS Code Dev Container configuration
├── .vscode/
│   └── settings.json        # VS Code workspace settings
├── .gitignore
├── .agent/
│   └── AGENTS.md            # This file
├── app/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── hello.py         # Core hello world module
│   │   └── main.py          # Application entry point
│   └── test/
│       ├── __init__.py
│       └── test_hello.py    # Pytest test suite
├── Makefile               # Convenience commands (make run, make test)
├── requirements.txt       # Python dependencies
├── LICENSE
└── README.md
```

## Development Environment

- **Python Version**: 3.12 (via Dev Container)
- **Base Image**: `mcr.microsoft.com/devcontainers/python:3.12`
- **Package Manager**: pip
- **Dependencies**: pytest (from requirements.txt)

## Dev Container Features

- Git (via `ghcr.io/devcontainers/features/git:1`)
- GitHub CLI (via `ghcr.io/devcontainers/features/github-cli:1`)

## VS Code Extensions (auto-installed)

- `ms-python.python` - Python language support
- `ms-python.vscode-pylance` - Pylance for IntelliSense
- `charliermarsh.ruff` - Ruff linter/formatter

## Code Style & Linting

- **Formatter**: Ruff (default for Python files)
- **Linting**: Enabled via Pylance
- **Format on Save**: Enabled

## Running the Application

```bash
# Using make commands (recommended)
make run    # Run the application
make test   # Run all unit tests

# Or directly with Python
python -m app.src.hello
python -m app.src.main

# Or directly with pytest
pytest app/test/
pytest app/test/test_hello.py -v
```

## Agent Instructions

- This is a Python 3.12 project
- Use type hints where appropriate
- Follow Ruff formatting conventions
- All source code lives under `app/src/`
- All tests live under `app/test/`
- Tests use pytest
- Add new dependencies to `requirements.txt`
- The Dev Container will automatically install dependencies on build

## Ports

Commented-out in devcontainer.json (uncomment if needed):
- 8000 (typical web server)
- 5432 (PostgreSQL)
