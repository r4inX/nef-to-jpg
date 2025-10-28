# Contributing to NEF to JPG Converter

We love your input! We want to make contributing to the NEF to JPG Converter as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. **Fork the repo** and create your branch from `main`
2. **Install development dependencies**: `pip install -e ".[dev]"`
3. **Make your changes**
4. **Add tests** for your changes
5. **Run the test suite**: `pytest`
6. **Ensure code quality**: `black src tests && isort src tests && flake8 src tests`
7. **Commit your changes** with a clear commit message
8. **Push to your fork** and submit a pull request

## Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/nef-to-jpg.git
cd nef-to-jpg

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev,docs,security]"

# Install pre-commit hooks (optional but recommended)
pre-commit install
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_converter.py

# Run with verbose output
pytest -v

# Run tests in parallel
pytest -n auto
```

## Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Lint code
flake8 src tests

# Type checking
mypy src

# Run all quality checks
black src tests && isort src tests && flake8 src tests && mypy src
```

## Testing Guidelines

- Write tests for all new functionality
- Ensure existing tests still pass
- Include edge cases and error conditions
- Test with different Python versions locally if possible
- Mock external dependencies (like actual NEF files) in unit tests

### Test Structure

```python
def test_function_name():
    """Test description of what is being tested."""
    # Arrange
    setup_data = "test_data"
    
    # Act
    result = function_to_test(setup_data)
    
    # Assert
    assert result == expected_result
```

## Pull Request Process

1. **Update documentation** if you're changing functionality
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass** locally
4. **Update the README.md** if needed
5. **Write a clear PR description** explaining your changes
6. **Link to any related issues**
7. **Request review** from maintainers

### PR Title Format

Use conventional commit format:
- `feat: add new conversion option`
- `fix: resolve memory leak in batch processing`
- `docs: update installation instructions`
- `test: add tests for CLI module`
- `refactor: improve error handling`

## Bug Reports

When filing an issue, please include:

- **Python version** and operating system
- **Complete error message** and stack trace
- **Steps to reproduce** the issue
- **Sample input file** (if possible, without sensitive data)
- **Expected vs actual behavior**
- **Screenshots** if relevant

### Bug Report Template

```markdown
**Bug Description**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
A clear and concise description of what you expected to happen.

**Environment**
- OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g. 3.9.7]
- Package Version: [e.g. 2.0.0]

**Additional Context**
Add any other context about the problem here.
```

## Feature Requests

We welcome feature requests! Please:

- **Check existing issues** to avoid duplicates
- **Clearly describe the use case** and problem you're solving
- **Provide examples** of how the feature would be used
- **Consider backwards compatibility**
- **Think about the API design** if proposing new functionality

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions.

**Use Cases**
Describe specific use cases where this feature would be helpful.

**Additional Context**
Add any other context or screenshots about the feature request here.
```

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code.

## Recognition

Contributors will be recognized in:
- The project's README.md
- Release notes for significant contributions
- GitHub's contributor graph

## Questions?

Feel free to open an issue with the "question" label if you need help or clarification on anything!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to NEF to JPG Converter!** 🎉