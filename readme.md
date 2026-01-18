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
pip install git+https://gitlab.com/da_doomer/markdown-slides.git

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

## The [mdslides](https://gitlab.com/da_doomer/markdown-slides) Utility

So far we use `mdslides` as a Python-based wrapper for the Reveal.js framework.
It automates the transition from markdown text to a browser-based presentation, with math rendering and syntax highlighting (on top of Reveal.js core features).

1. **Asset bundling:** The tool carries a full, pre-configured version of Reveal.js internally. When executed, it creates an output directory (e.g., slides/) and copies all necessary CSS, JavaScript, and Plugin files into it.
2. **Template injection:** It utilizes an internal `index.html` template. It injects the presentation metadata (title, theme, etc.) and Markdown contents into this skeleton.
3. **Markdown strategy:** Instead of converting Markdown to HTML at build-time, it configures Reveal.js to use its Markdown Plugin. It wraps contents in a `<section data-markdown>` tag, allowing the browser to parse the Markdown at runtime.

The resulting folder is entirely self-contained and can be opened locally, or deployed directly to platforms like GitHub Pages.

## Next steps

- CI / SQA
  - Add pre-commits hooks (clean yaml, etc)
  - Add ShellCheck (for linting) and shfmt (for formatting) workflow for scripts
- Allow subfolder structure before `slides.md` (e.g. to gather all meeting slides in one)
- Integrate with latex [princeton-beamer](https://github.com/cisgroup/princeton-beamer) template
  - Change color scheme
  - Change title/sections/etc fonts
  - Implement dedicated text-blocks, allowing writing something like
    ```md
    ::: alert | Important Title
    This is the content of the alert block.
    :::
    ```
  - Write tailored title, TOC and final frames
  - Add footers:
    - footline with logo, name, short title, location, last compiled and frame number
    - extra footline for citations and image sources
- Add dark / light mode for the slides. Probably define a monochromatic palette for the dark mode. Exception on slides with background images/videos.
- Leave the `mdslides`-per-talk approach, which creates a copy of Reveal.js for each talk. Instead, we refactor around our suite of slide decks as follows:
  ```bash
  slides/
  ├── lib/ (One copy of Reveal.js CSS/JS)
  ├── assets/ (Shared theme-toggle.js and style.css)
  ├── talk-1/ (Only the index.html and slides.md)
  └── talk-2/ (Only the index.html and slides.md)
  ```
  At this point we rewrite everything (since we use different template and html injection), instead of forking `mdslides`.
- Move to rst instead of md? Of course the issue is that there is no such [plugin](https://github.com/hakimel/reveal.js/tree/master/plugin). However, instead of using the browser-side Markdown plugin, we could use a tool like Pandoc or Hugo to convert reStructuredText (reST) to HTML during the CI build.
