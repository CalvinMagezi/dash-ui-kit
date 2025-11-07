# GitHub Actions Workflows

Due to GitHub App permissions, workflow files need to be added manually to the repository.
Below are the workflow configurations that should be placed in `.github/workflows/`.

## Setup Instructions

1. Manually create the `.github/workflows/` directory in your repository
2. Create the three workflow files below
3. Commit and push them directly through GitHub's web interface or with appropriate permissions

---

## test.yml

Path: `.github/workflows/test.yml`

```yaml
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[dev]"

    - name: Run linters
      run: |
        black --check .
        ruff check .
        mypy dash_ui_kit

    - name: Run tests
      run: |
        pytest --cov=dash_ui_kit --cov-report=xml --cov-report=term-missing

    - name: Upload coverage to Codecov
      if: matrix.os == 'ubuntu-latest' && matrix.python-version == '3.11'
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
        fail_ci_if_error: false
```

---

## docs.yml

Path: `.github/workflows/docs.yml`

```yaml
name: Documentation

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e ".[docs]"

    - name: Build documentation
      run: |
        mkdocs build --strict

    - name: Deploy to GitHub Pages
      if: github.event_name == 'push' && github.ref == 'refs/heads/main'
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./site
```

---

## publish.yml

Path: `.github/workflows/publish.yml`

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine

    - name: Build package
      run: python -m build

    - name: Check package
      run: twine check dist/*

    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

---

## Required Secrets

For the workflows to function properly, add these secrets to your repository:

1. **PYPI_API_TOKEN**: Token from PyPI for package publishing
   - Generate at: https://pypi.org/manage/account/token/
   - Add to: Repository Settings → Secrets and variables → Actions

2. **GITHUB_TOKEN**: Automatically provided by GitHub (no setup needed)

## Enabling GitHub Pages

For documentation deployment:

1. Go to Repository Settings → Pages
2. Set Source to "Deploy from a branch"
3. Select the `gh-pages` branch
4. Save

Your documentation will be available at: `https://your-username.github.io/dash-ui-kit/`
