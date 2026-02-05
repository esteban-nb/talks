Here we implement the main logic:

1. Markdown parsing. We read the `.md` file(s) line-by-line
   - Starting with the YAML front matter, that contains the information for the index of all talks, but also the different options for the slides.

     ```
     ---
     title: "A Long and Great Title (Month Year)"
     display_name: "A Short Title"
     date: "YYYY-MM-DD"
     template: "templates/slides-template.html"

     # Reveal.js Integration Options
     controls: true
     progress: true
     hash: true
     transition: "slide"
     ---

     # Slide 1
     Some novel contents...
     ```

     Where `templates/slides-template.html` is the full deck template: we fill the `{{CONTENT}}` anchor with a long string of many `<section>` tags (one for each slide).
     Next we should create a specific title/cover page, TOC page and closing page template.

   - In the actual markdown body, we converts text blocks, fragments, slide segments, etc.

2. Template injection. We replace the different anchors in `slides-template.html` (TITLE, CONTENT, CONFIG) with the generated HTML string.
3. Vendoring. We physically copy the `reveal.js` folder (once for all slide decks) to the target path, and delete everything except "critical paths" (dist, plugin).

Note that `build-talks.sh` is just a first version that calls `mdslides` on each slide deck.
The file `build.py` on the other hand contains the function that gathers all slides and builds with a single copy of `reveal.js` (WIP).

## Build Structure

The layout is:

```bash
TARGET_OUTPUT/assets/...
TARGET_OUTPUT/dist/...
TARGET_OUTPUT/highlightjs/highlight.js
TARGET_OUTPUT/media/...
TARGET_OUTPUT/plugin/...
TARGET_OUTPUT/<talk_name>/index.html
TARGET_OUTPUT/index.html
```

This has to be kept in mind when referencing to a specific asset (inside a talk index, or inside the home index).
For example writing in a specific `slides.md` `![FP on sphere](media/images/fokker-plank-wuerzburg.jpg)` emits this verbatim into HTML: `<img src="media/images/fokker-plank-wuerzburg.jpg">
`. However that path is interpreted as `<location of slide index.html>/media/images/...`. Therefore, one should use `../media/images/fokker-plank-wuerzburg.jpg`, or prepend that adjustement.

When

## User Guide

1. Install Python libraries.
2. Run orchestrator. The function `build_talks.py` will directly load the Markdown files, get the processed HTML from `preprocess_slides.py`, and use a simple string replace to generate the final `index.html` in a hashed folder.

## [CommonMark Spec](https://spec.commonmark.org/current/)

- Block vs. inline parsing
  - Block HTML: If a tag like `<div>` starts on its own line, CommonMark stops parsing Markdown until it finds a blank line or a closing tag.
  - Inline HTML: Tags like `<span>`, `<b>`, or `<i>` can be used inside a paragraph without breaking Markdown parsing
- Markdown parsers require a blank line between a block-level HTML tag (like `div`) and the Markdown content to correctly switch back from HTML parsing to Markdown parsing.
- Lines starting with `<!--`, `<?`, `<!`, or `<![CDATA[` also stop Markdown parsing.
- CommonMark uses a 4-space or 1-tab rule for code blocks.
  Thus always keep Markdown content flush-left even when inside nested HTML.
  Otherwise the parser will see the `<div>` and switch to HTML mode, see the indented text and wrap it in `<pre><code>` instead of rendering it as part of the block.

To see these rules in action, test snippets in the [CommonMark Dingus](https://spec.commonmark.org/dingus/).
