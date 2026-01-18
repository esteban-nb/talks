This directory contains third-party libraries managed as Git Submodules.
We use submodules to ensure the build pipeline is offline-capable and reproducible.

1. Reveal.js provides the CSS/JS engine that renders slides in the browser. We utilize the built-in markdown, notes, and math plugins provided in this repository.
2. Highlight.js CDN Release provides the syntax highlighting engine for code blocks.

to add advanced features that are not core, they shoudl be added as separate submodules here. For example:

- Chalkboard: For drawing on slides.
- Menu: For a slide-out navigation table of contents.
- Custom Code Editors: For live-running code snippets.
