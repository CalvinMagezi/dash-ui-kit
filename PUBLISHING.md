# Publishing Guide

Quick reference for publishing Dash UI Kit to PyPI.

## Quick Publish (For Maintainers)

```bash
# 1. Update version
# Edit dash_ui_kit/__version__.py and pyproject.toml

# 2. Update changelog
# Edit CHANGELOG.md

# 3. Clean and build
rm -rf dist/ build/ *.egg-info
python -m build

# 4. Check package
twine check dist/*

# 5. Test locally (optional but recommended)
pip install dist/dash_ui_kit-*.whl

# 6. Upload to TestPyPI (optional)
twine upload --repository testpypi dist/*

# 7. Upload to PyPI
twine upload dist/*

# 8. Tag and push
git tag v0.X.X
git push origin v0.X.X
```

## Prerequisites

### Install Build Tools

```bash
pip install build twine
```

### PyPI Account Setup

1. Create account at https://pypi.org/account/register/
2. Verify email
3. Enable 2FA (recommended)
4. Generate API token at https://pypi.org/manage/account/token/
5. Save token securely

### Configure Credentials

**Option 1: .pypirc file** (Recommended)

Create `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR-TOKEN-HERE

[testpypi]
username = __token__
password = pypi-YOUR-TESTPYPI-TOKEN-HERE
```

Set permissions:
```bash
chmod 600 ~/.pypirc
```

**Option 2: Environment Variables**

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR-TOKEN-HERE
```

## First Time Setup

### 1. Register Package Name

The package name `dash-ui-kit` must be available on PyPI.

Check availability:
```bash
pip search dash-ui-kit  # Or check https://pypi.org/project/dash-ui-kit/
```

### 2. Test Upload

First publish to TestPyPI:

```bash
twine upload --repository testpypi dist/*
```

View at: https://test.pypi.org/project/dash-ui-kit/

### 3. Test Install from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ dash-ui-kit
```

### 4. Publish to Production PyPI

```bash
twine upload dist/*
```

View at: https://pypi.org/project/dash-ui-kit/

## Version Management

### Semantic Versioning

- **0.1.0** → **0.2.0**: New features (minor)
- **0.2.0** → **0.2.1**: Bug fixes (patch)
- **0.9.0** → **1.0.0**: Stable release (major)
- **1.0.0** → **2.0.0**: Breaking changes (major)

### Update Version

Edit two files:

**1. dash_ui_kit/__version__.py**
```python
__version__ = "0.2.0"
```

**2. pyproject.toml**
```toml
[project]
version = "0.2.0"
```

## Build Process

### Generate CSS

Before building, ensure CSS is generated:

```bash
python scripts/generate_utilities.py
python scripts/build_css.py
```

### Build Package

```bash
python -m build
```

This creates:
- `dist/dash_ui_kit-0.X.X.tar.gz` (source)
- `dist/dash_ui_kit-0.X.X-py3-none-any.whl` (wheel)

### Verify Package

```bash
twine check dist/*
```

## Uploading

### To TestPyPI

```bash
twine upload --repository testpypi dist/*
```

### To PyPI

```bash
twine upload dist/*
```

### With Specific Credentials

```bash
twine upload -u __token__ -p pypi-YOUR-TOKEN dist/*
```

## Post-Release

### Create Git Tag

```bash
git tag -a v0.X.X -m "Release v0.X.X"
git push origin v0.X.X
```

### Create GitHub Release

1. Go to https://github.com/CalvinMagezi/dash-ui-kit/releases/new
2. Choose tag v0.X.X
3. Title: "v0.X.X - Release Name"
4. Description: Copy from CHANGELOG.md
5. Publish

### Verify Installation

```bash
# Wait 1-2 minutes for PyPI to update
pip install --upgrade dash-ui-kit==0.X.X

# Test
python -c "import dash_ui_kit; print(dash_ui_kit.__version__)"
```

## Troubleshooting

### "Package already exists"

You cannot overwrite a version. Must bump version number.

### "Invalid authentication"

Check your API token:
- Token must start with `pypi-`
- Username must be `__token__`
- Check `.pypirc` formatting

### "Missing files in distribution"

Check `MANIFEST.in`:
```bash
cat MANIFEST.in
```

Verify files in package:
```bash
tar -tzf dist/dash_ui_kit-*.tar.gz
```

### "README rendering failed"

PyPI requires valid reStructuredText or Markdown:
```bash
twine check dist/*
```

## Security Best Practices

1. **Never commit tokens** to git
2. **Use API tokens** instead of passwords
3. **Enable 2FA** on PyPI account
4. **Rotate tokens** regularly
5. **Use separate tokens** for TestPyPI and PyPI
6. **Restrict token scope** to specific projects

## Automation

### GitHub Actions (Future)

Create `.github/workflows/publish.yml`:

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
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      - name: Build package
        run: python -m build
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

Add `PYPI_API_TOKEN` to repository secrets.

## Resources

- [PyPI](https://pypi.org/)
- [TestPyPI](https://test.pypi.org/)
- [Packaging Guide](https://packaging.python.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)

## Support

For publishing issues:
- Check [PyPI Status](https://status.python.org/)
- PyPI Help: https://pypi.org/help/
- GitHub Issues: https://github.com/CalvinMagezi/dash-ui-kit/issues

---

**Maintained By**: Calvin Magezi
**Last Updated**: November 7, 2025
