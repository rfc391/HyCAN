```markdown
## Description
Please include a summary of the changes.

## Checklist
- [ ] Code compiles correctly
- [ ] Tests added for new features
- [ ] All tests passing
- [ ] Code reviewed and approved
```

### 4. Issue Template for Bugs (`.github/ISSUE_TEMPLATE/bug_report.md`)
```markdown
---
name: Bug Report
about: Create a report to help us improve
labels: bug
---

**Describe the bug:**
A clear and concise description of what the bug is.

**To Reproduce:**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior:**
A clear and concise description of what you expected to happen.

**Screenshots:**
If applicable, add screenshots to help explain your problem.

**Environment:**
- OS: [e.g., Windows, MacOS]
- Browser [e.g., Chrome, Firefox]
- Version [e.g., 22]

**Additional context:**
Add any other context about the problem here.
```

### 5. Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### 6. Example Test File (`tests/test_example.py`)
```python
# tests/test_example.py

def test_sample():
    assert 1 + 1 == 2
```

### 7. Linter and Formatter Configuration
#### `.pylintrc` for Pylint:
```ini
[MASTER]
ignore=tests

[MESSAGES CONTROL]
disable=missing-docstring,invalid-name
```
#### Black Configuration:
Add the following to `pyproject.toml`:
```toml
[tool.black]
line-length = 88
