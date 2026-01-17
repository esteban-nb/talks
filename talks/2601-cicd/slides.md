---
title: "CI/CD with GitHub Actions (Jan 2026)"
display_name: "CI/CD Workshop"  
date: "2026-01-15"
---

[comment]: # (This presentation was made with markdown-slides)
[comment]: # (Can be found here: https://gitlab.com/da_doomer/markdown-slides)
[comment]: # (Compile this presentation with: mdslides slides.md)

[comment]: # (THEME = white)
[comment]: # (CODE_THEME = github)
[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })

## Continuous Integration and Continuous Delivery (CI/CD)

### Esteban NOCET-BINOIS
**Personal Notes, from Andres Rios Tascon's talk, Princeton Winter Training 2026**

[comment]: # (!!!)

## CI Services Landscape

- **GitHub Actions** 🥇 *Most popular, integrated*
  - Native GitHub integration
  - Massive marketplace of actions
  - Free minutes for public repos
  
- **GitLab CI** 🥈 *Enterprise favorite*
  - `.gitlab-ci.yml` syntax
  - Built-in container registry
  - Self-hosted runners
  
- **CircleCI** 🥉 *Speed focused*
  - Fast parallel execution
  - Optimized Docker images

[comment]: # (||| data-auto-animate)

## Main CI Services - Minutes/Month

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        Minutes/Month         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ GitHub:   2000 (Public ∞)    │
│ GitLab:   400 (Public ∞)     │
│ CircleCI: 6000 paid          │
│ Travis:   10k (Declining)    │
└──────────────────────────────┘
```

[comment]: # (!!!)

## Real-World CI/CD Examples

**Scikit-HEP/Awkward** [🔗](https://github.com/scikit-hep/awkward/tree/main/.github)
```
13 workflows: test, docs, release, conda, wheels
50+ jobs across Python/NumPy versions
```

**SegmentLinking/cmssw** [🔗](https://github.com/SegmentLinking/cmssw/tree/CI_branch/.github)
```
CMS physics experiment pipeline
Matrix testing across compilers
```

**scientific-python/repo-review** [🔗](https://github.com/scientific-python/repo-review/tree/main/.github)
```
Automated repository health checks
Cookiecutter template validation
```

[comment]: # (!!!)

## YAML Crash Course - Scalars & Lists

```yaml
# Scalars
key: "string value"
number: 42
flag: true
null: null

# Lists
fruits:
  - apple
  - banana
  - cherry
inline: [apple, banana, cherry]
```

[comment]: # (||| data-auto-animate)

## YAML Crash Course - Dictionaries & Multi-line

```yaml
# Dictionaries
person:
  name: "John Doe"
  age: 30
  tags: [devops, python]

# Multi-line strings
script: |
  echo "Line 1"
  echo "Line 2"
message: >
  This gets folded into
  a single line
```

[comment]: # (!!!)

## Writing Actions - Basic Structure

**Every workflow file starts like this:**

```yaml
name: "CI Pipeline"
on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: pytest
```

**Key concepts:**
- `on:` = triggers
- `jobs.test` = parallel execution units
- `steps` = sequential commands

[comment]: # (||| data-auto-animate)

## Writing Actions - Job Matrix

**Test across multiple environments:**

```yaml
jobs:
  test:
    strategy:
      matrix:
        python: [3.9, 3.10, 3.11, 3.12]
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python }}
```

[comment]: # (!!!)

## Handmade Scripts as Actions

**Create `.github/scripts/test.sh`:**
```bash
#!/bin/bash
set -e
pytest tests/ --cov=./ --cov-report=xml
coverage-badge -fo coverage.svg
```

**Use in workflow:**
```yaml
- name: Run tests
  run: .github/scripts/test.sh
```

**Annotations for GitHub UI:**
```bash
echo "::warning::Low test coverage (45%)"
echo "::error::Tests failed on Windows"
exit 1
```

[comment]: # (||| data-auto-animate)

## Handmade Scripts - Caching

**`.github/scripts/setup.sh`:**
```bash
#!/bin/bash
pip install -r requirements.txt
pre-commit install
black --check .
mypy src/
```

**Smart caching in workflow:**
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

[comment]: # (!!!)

## Third-Party Actions - Official

**Microsoft's official actions (always safe):**
```yaml
- uses: actions/checkout@v4
- uses: actions/setup-python@v4
- uses: actions/cache@v3
- uses: actions/upload-artifact@v3
```

**Version pinning is critical:**
```
✅ v4, v4.1.0, ==4.1.0
❌ latest, main, @v4
```

[comment]: # (||| data-auto-animate)

## Third-Party Actions - Community

**Popular vetted community actions:**
```yaml
- uses: pre-commit/action@v3
- uses: dorny/paths-filter@v2
- uses: codecov/codecov-action@v3
```

**Security checklist:**
```
1. Check stars/forks (1000+/100+)
2. Last update <6 months
3. Pin exact version
4. Read action.yml
```

[comment]: # (!!!)

## Finding Third-Party Actions

**GitHub Marketplace** [🔗](https://github.com/marketplace?type=actions)

```
⭐ Most Popular Categories
├── Testing: pytest, coverage (500+)
├── Linting: ruff, black, eslint (300+)
├── Deployment: pages, releases (400+)
├── Python: pypa, poetry (200+)
```

**Sort by "Recently updated" to avoid dead projects**

[comment]: # (||| data-auto-animate)

## Action Discovery Workflow

```
1. Need coverage? → codecov/codecov-action@v3
2. Conditional steps? → dorny/paths-filter@v2
3. Complex caching? → actions/cache@v3
4. Python packaging? → pypa/gh-action-pypa@v1
```

**Copy-paste patterns:**
```yaml
# Coverage + badge
- uses: codecov/codecov-action@v3
- run: coverage-badge -fo coverage.svg

# Pre-commit
- uses: pre-commit/action@v3
```

[comment]: # (!!!)
