# Slides Repo

## View Slides

Index of all talks: https://esteban-nb.github.io/talks/

## Local Development

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.11+**
- **yq** (YAML processor)
- **shasum** (usually pre-installed on Linux)

### Setup & Build

Run the following commands from the project root:

```bash
# Install the slide generator
pip install git+https://gitlab.com

# Make scripts executable
chmod +x scripts/*.sh

# Build talks and generate the index
./scripts/build-talks.sh
./scripts/generate-index.sh

# Open
xdg-open slides/index.html
```

The build process generates several files:

- `slides/` (complete static site, that's deployable)
- `display-names.txt` (temp mapping of talk folders to display names)
- `hash-mapping.txt` (audit log of talk-name)
- `valid-talks.txt` (built talks used by the indexer)

## Next steps

- Add pre-commits hooks (clean yaml, etc)
- Add ShellCheck (for linting) and shfmt (for formatting) workflow for scripts
- Integrate with latex "princeton beamer" template
- Move to rst instead of md?
