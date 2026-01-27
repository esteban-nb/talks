## Reveal.js and HTML Crash Course

Add HTML attributes (like classes, IDs, or fragments) directly to Markdown elements using a special trailing syntax: 

```
<!-- .element: class="fragment" data-fragment-index="1" -->
```

Apply attributes to the parent slide (the <section>) from within the Markdown:

```
<!-- .slide: data-background="#ff0000" -->
```

Use HTML line breaks:

- The simplest way to add small increments of vertical space is by inserting the `<br>` tag directly into your Markdown.
- To force a blank line, insert a paragraph containing a non-breaking space entity `&nbsp;`.
- For precise control, use an HTML element like a `<div>` or `<span>` with inline styles to define a specific height: `<div style="height:100px"></div>`.
- To automatically push other content apart by filling all available remaining space on the slide, use the .r-stretch class: `<!-- .element: class="r-stretch" -->`.

Indeed, Reveal.js provides built-in CSS classes to handle common layout challenges: 

- `.r-stretch`: Automatically resizes an element (like an image or iframe) to fill the remaining vertical space on the slide.
- `.r-stack`: Centers multiple elements on top of one another, which is ideal for showing images or text sequentially using fragments.
- `.r-fit-text`: Scales text to be as large as possible without overflowing the slide. 

Use HTML tables, links, figures, etc.

Use `data-trim` and `data-noescape` to remove surrounding whitespace or allow HTML tags inside your code blocks.

## Animations

Animation types:

- Use classes like `fade-up`, `fade-out`, `highlight-red`, or `grow` to change how the fragment appears.
- Use the `data-line-numbers` attribute for step-by-step highlighting. E.g. `[3, 8-10]` highlights line 3 and lines 8 through 10.
- Override global animations for a single slide with `data-transition="zoom"`, `fade`, `slide`, or `none`.
