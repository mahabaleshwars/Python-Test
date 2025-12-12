# Python-Test

A sample Python project for testing [github.com/actions/setup-python](https://github.com/actions/setup-python) scenarios.

## Overview

This project is designed to test various scenarios with the GitHub Actions `setup-python` action. It includes:

- A Python package with sample modules
- A `package.json` file for Node.js integration testing
- Standard Python project configuration files (`setup.py`, `requirements.txt`)
- Unit tests using Python's `unittest` framework

## Project Structure

```
Python-Test/
├── python_test/          # Main Python package
│   ├── __init__.py       # Package initialization
│   ├── calculator.py     # Calculator module with basic math operations
│   └── greeter.py        # Greeter module with greeting functions
├── tests/                # Test directory
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_greeter.py
├── setup.py              # Python package setup configuration
├── requirements.txt      # Python dependencies
├── package.json          # Node.js package configuration (for setup-python testing)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Installation

### Python Dependencies

Install the package in development mode:

```bash
pip install -e .
```

Or install with development dependencies:

```bash
pip install -e .[dev]
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Using npm (via package.json)

The project includes a `package.json` file with convenient scripts:

```bash
npm run install:python    # Install Python dependencies
npm run install:dev       # Install with development dependencies
npm run setup            # Run setup.py install
```

## Running Tests

### Using Python

```bash
# Run tests with unittest
python -m unittest discover tests

# Run tests with pytest (requires pytest installation)
pytest

# Run tests with coverage
pytest --cov=python_test --cov-report=html
```

### Using npm

```bash
npm test                 # Run pytest
npm run test:coverage    # Run pytest with coverage
```

## Usage Examples

### Calculator Module

```python
from python_test.calculator import add, subtract, multiply, divide

result = add(5, 3)        # Returns 8
result = subtract(10, 4)  # Returns 6
result = multiply(3, 7)   # Returns 21
result = divide(15, 3)    # Returns 5.0
```

### Greeter Module

```python
from python_test.greeter import greet, farewell

message = greet("Alice")     # Returns "Hello, Alice!"
message = farewell("Bob")    # Returns "Goodbye, Bob!"
```

## Testing with setup-python

This project is designed to test various scenarios with the `actions/setup-python` GitHub Action, including:

- Installing Python dependencies from `requirements.txt`
- Running tests with different Python versions
- Using both Python and Node.js package managers
- Testing package installation and module imports
- Validating test execution across different environments

## License

MIT
