# Contributing to Dash UI Kit

Thank you for your interest in contributing to Dash UI Kit! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)
- Code samples or screenshots if applicable

### Suggesting Features

Feature requests are welcome! Please provide:
- A clear description of the feature
- Use cases and benefits
- Potential implementation approach (optional)

### Pull Requests

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/dash-ui-kit.git
   cd dash-ui-kit
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set Up Development Environment**
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

4. **Make Your Changes**
   - Write clear, concise code
   - Follow existing code style
   - Add/update tests
   - Update documentation

5. **Run Tests and Linters**
   ```bash
   # Format code
   black .

   # Lint code
   ruff check .

   # Type check
   mypy dash_ui_kit

   # Run tests
   pytest
   ```

6. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `style:` Code style changes (formatting, etc.)
   - `refactor:` Code refactoring
   - `test:` Test changes
   - `chore:` Build process or auxiliary tool changes

7. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

   Then open a pull request on GitHub.

## Development Guidelines

### Code Style

- Follow PEP 8
- Use Black for formatting (line length: 88)
- Use type hints for all functions
- Write docstrings for public APIs

### Testing

- Write tests for all new features
- Maintain >90% code coverage
- Include unit and integration tests
- Test on multiple Python versions

### Documentation

- Update README.md if needed
- Add docstrings to new functions/classes
- Update relevant documentation pages
- Include usage examples

### Component Development

When adding a new component:

1. Create component file in `dash_ui_kit/components/`
2. Add CSS styles in `dash_ui_kit/assets/components/`
3. Write comprehensive tests
4. Add documentation page
5. Include usage examples
6. Update exports in `__init__.py`

### CSS Development

When adding utilities or styles:

1. Update generator script if needed
2. Follow naming conventions
3. Test in multiple browsers
4. Ensure accessibility
5. Keep bundle size minimal

## Project Structure

```
dash-ui-kit/
├── dash_ui_kit/          # Main package
│   ├── components/       # Component modules
│   ├── assets/          # CSS and static files
│   ├── utils/           # Utility functions
│   └── themes/          # Theme definitions
├── tests/               # Test files
├── docs/                # Documentation
├── examples/            # Example applications
└── scripts/             # Build scripts
```

## Getting Help

- Check existing issues and documentation
- Ask questions in GitHub Discussions
- Join our community chat (if available)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- CHANGELOG.md
- GitHub contributors page
- Release notes

Thank you for contributing to Dash UI Kit! 🎉
