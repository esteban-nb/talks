Here we implement the main logic:
1. Markdown parsing. We read the `.md` file(s) line-by-line
   * Starting with the YAML front matter, that contains the information for the index of all talks, but also the different options for the slides.
     ```
     ---
     title: "A Long and Great Title (Month Year)"
     display_name: "A Short Title"
     date: "YYYY-MM-DD"
     template: "templates/slides-template.html"

     # Reveal.js Integration Options
     controls: true
     progress: true
     center: true
     hash: true
     transition: "slide"
     zoom: true
     fragments: true
     ---
      
     # Slide 1
     Some novel contents...
     ```
   * In the actual markdown body, we converts text blocks, fragments, etc.
3. Template injection. We replace the different anchors in `slides-template.html` (TITLE, CONTENT, CONFIG) with the generated HTML string.
4. Vendoring. We physically copy the `reveal.js` folder (once for all slide decks) to the target path, and delete everything except "critical paths" (dist, plugin).

## User Guide

1. Install Python libraries.
2. Run orchestrator. The function `build_talks.py` will directly load the Markdown files, get the processed HTML from `preprocess_slides.py`, and use a simple string replace to generate the final `index.html` in a hashed folder.
