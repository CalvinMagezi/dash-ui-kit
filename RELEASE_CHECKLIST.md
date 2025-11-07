# Release Checklist for Dash UI Kit

Comprehensive checklist for preparing and publishing a new release.

## Pre-Release Checklist

### Code Quality

- [ ] All tests passing: `pytest`
- [ ] Code coverage ≥90%: `pytest --cov=dash_ui_kit`
- [ ] No linting errors: `ruff check .`
- [ ] Code formatted: `black .`
- [ ] Type checking passes: `mypy dash_ui_kit`
- [ ] No security vulnerabilities
- [ ] All examples working

### Documentation

- [ ] README.md updated
- [ ] CHANGELOG.md updated with release notes
- [ ] All component docs complete
- [ ] API reference accurate
- [ ] Examples tested and working
- [ ] Screenshots/GIFs updated (if applicable)
- [ ] Migration guide updated (for breaking changes)

### Package Structure

- [ ] Version bumped in `__version__.py`
- [ ] Version bumped in `pyproject.toml`
- [ ] Dependencies up to date
- [ ] License file present
- [ ] MANIFEST.in includes all assets
- [ ] All CSS files generated: `python scripts/build_css.py`
- [ ] Package builds successfully: `python -m build`
- [ ] Package validates: `twine check dist/*`

### Git & GitHub

- [ ] All changes committed
- [ ] Branch up to date with main
- [ ] No uncommitted changes: `git status`
- [ ] Git tags pushed
- [ ] Release branch created (if using git-flow)

## Release Steps

### 1. Version Bump

Update version in these files:
```python
# dash_ui_kit/__version__.py
__version__ = "0.2.0"  # Update this
```

```toml
# pyproject.toml
[project]
version = "0.2.0"  # Update this
```

### 2. Update CHANGELOG

```markdown
# CHANGELOG.md

## [0.2.0] - 2025-XX-XX

### Added
- Feature 1
- Feature 2

### Changed
- Change 1

### Fixed
- Bug fix 1

### Breaking Changes
- Breaking change 1 (if any)
```

### 3. Clean Previous Builds

```bash
rm -rf dist/ build/ *.egg-info
```

### 4. Build Package

```bash
python -m build
```

Expected output:
- `dist/dash_ui_kit-X.X.X.tar.gz` (source distribution)
- `dist/dash_ui_kit-X.X.X-py3-none-any.whl` (wheel)

### 5. Verify Package

```bash
# Check package
twine check dist/*

# List contents
tar -tzf dist/dash_ui_kit-*.tar.gz

# Verify wheel
unzip -l dist/dash_ui_kit-*-py3-none-any.whl
```

### 6. Test Installation Locally

```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from local wheel
pip install dist/dash_ui_kit-X.X.X-py3-none-any.whl

# Test import
python -c "import dash_ui_kit; print(dash_ui_kit.__version__)"

# Test example
python examples/basic_usage.py

# Cleanup
deactivate
rm -rf test_env
```

### 7. Upload to TestPyPI (Optional but Recommended)

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ dash-ui-kit

# Verify
python -c "import dash_ui_kit; print(dash_ui_kit.__version__)"
```

### 8. Create Git Tag

```bash
git tag -a v0.X.X -m "Release version 0.X.X"
git push origin v0.X.X
```

### 9. Create GitHub Release

1. Go to https://github.com/CalvinMagezi/dash-ui-kit/releases/new
2. Select the tag (v0.X.X)
3. Set release title: "v0.X.X - Release Name"
4. Copy CHANGELOG entries to release notes
5. Attach built packages (optional)
6. Publish release

### 10. Upload to PyPI

```bash
twine upload dist/*
```

You'll need PyPI credentials or API token.

### 11. Verify PyPI Release

```bash
# Wait a few minutes, then install from PyPI
pip install --upgrade dash-ui-kit

# Verify version
python -c "import dash_ui_kit; print(dash_ui_kit.__version__)"

# Check PyPI page
# https://pypi.org/project/dash-ui-kit/
```

## Post-Release

### Documentation

- [ ] Documentation deployed: https://dash-ui-kit.readthedocs.io/
- [ ] GitHub Pages updated (if applicable)
- [ ] Announcement blog post (if applicable)

### Communication

- [ ] Announce on internal Slack/Teams
- [ ] Tweet/social media (if public)
- [ ] Email to stakeholders
- [ ] Update project board/roadmap

### Monitoring

- [ ] Monitor PyPI download stats
- [ ] Watch for bug reports
- [ ] Monitor GitHub issues
- [ ] Check CI/CD pipelines

### Next Steps

- [ ] Create milestone for next release
- [ ] Triage open issues
- [ ] Plan next features
- [ ] Update roadmap

## Rollback Procedure

If issues are discovered after release:

### Option 1: Yank Release (PyPI)

```bash
# Mark release as yanked (not deleted, but discouraged)
pip install twine
twine upload --skip-existing dist/*
# Then manually yank on PyPI web interface
```

### Option 2: Hot Fix Release

1. Create hotfix branch
2. Fix the issue
3. Version bump (patch version)
4. Follow release steps for patch release
5. Communicate the hotfix

### Option 3: Major Rollback

1. Delete GitHub release
2. Remove git tag
3. Yank PyPI release
4. Communicate rollback to users

## Version Numbering Guide

Following [Semantic Versioning](https://semver.org/):

- **Major (X.0.0)**: Breaking changes
  - API changes
  - Removed features
  - Major refactoring

- **Minor (0.X.0)**: New features (backward compatible)
  - New components
  - New utilities
  - Enhanced features

- **Patch (0.0.X)**: Bug fixes
  - Bug fixes
  - Documentation updates
  - Minor tweaks

## Troubleshooting

### Build Fails

```bash
# Clean everything
rm -rf dist/ build/ *.egg-info dash_ui_kit.egg-info
pip install --upgrade build wheel setuptools

# Rebuild
python -m build
```

### Upload Fails

```bash
# Check credentials
twine check dist/*

# Ensure you have API token set
# Create token at: https://pypi.org/manage/account/token/
```

### Assets Missing

```bash
# Verify MANIFEST.in includes assets
cat MANIFEST.in

# Check assets in source dist
tar -tzf dist/dash_ui_kit-*.tar.gz | grep assets
```

## Automation (Future)

Consider automating with GitHub Actions:

```yaml
# .github/workflows/release.yml
on:
  release:
    types: [published]
jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build and publish
        run: |
          python -m build
          twine upload dist/*
```

## Security

- [ ] API tokens stored securely (not in code)
- [ ] Use PyPI trusted publishers (if available)
- [ ] Enable 2FA on PyPI account
- [ ] Review all dependencies for vulnerabilities
- [ ] Sign releases with GPG (optional)

## Resources

- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [GitHub Release Guide](https://docs.github.com/en/repositories/releasing-projects-on-github)

---

**Last Updated**: November 7, 2025
**Maintained By**: Calvin Magezi
