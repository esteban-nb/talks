# TODO
# - add footers

import re
import json
import frontmatter
from pathlib import Path

def transform_blocks(text):
    """
    Converts ::: type | Title syntax into HTML.
    Uses double newlines to ensure Reveal.js parses Markdown inside the block body.
    """
    pattern = r":::\s*(block|alert|example)\s*\|\s*(.*?)\n(.*?)\n:::"

    def replacer(match):
        b_type = match.group(1).lower()
        title = match.group(2).strip()
        body = match.group(3).strip()

        # Mapping to the CSS classes defined in slides-style.css
        css_map = {"block": "std", "alert": "alert", "example": "example"}
        cls = css_map.get(b_type, "std")

        return (f'<div class="block block-{cls}">\n'
                f'  <div class="block-title">{title}</div>\n'
                f'  <div class="block-body">\n\n'
                f'{body}\n\n'
                f'  </div>\n'
                f'</div>')

    return re.sub(pattern, replacer, text, flags=re.DOTALL)

def handle_fragments(text):
    """
    Converts [f] shorthand into Reveal.js fragment comments.
    """
    return text.replace(" [f]", ' <!-- .element: class="fragment" -->')

def wrap_slide(content, attributes=""):
    """
    Wraps content in Reveal.js section with attribute support.
    """
    attr_str = f" {attributes}" if attributes else ""
    return f'<section data-markdown{attr_str}><textarea data-template>\n{content.strip()}\n</textarea></section>'

def process_markdown_to_html(md_path, template_path):
    """
    Reads MD, handles YAML, replaces template anchors.
    """
    # 1. Load markdown and frontmatter
    post = frontmatter.load(md_path)
    metadata = post.metadata
    content = post.content

    # 2. Pre-process content
    content = transform_blocks(content)
    content = handle_fragments(content)

    # 3. Segmentation (horizontal !!! and vertical |||)
    presentation_html = []

    # Split by horizontal delimiter
    h_slides = re.split(r'\n!!!\s*\n', content)

    for h_slide in h_slides:
        # Check if this horizontal section contains vertical slides
        if "|||" in h_slide:
            v_slides = re.split(r'\n\|\|\|\s*\n', h_slide)
            v_html = [wrap_slide(v) for v in v_slides if v.strip()]
            # Wrap all vertical slides in a parent section
            presentation_html.append(f"<section>\n" + "\n".join(v_html) + "\n</section>")
        else:
            if h_slide.strip():
                presentation_html.append(wrap_slide(h_slide))

    content_html = "\n".join(presentation_html)

    # 4. Prepare Reveal.js Config (Injecting YAML options)
    # Filter out project-level keys, keep Reveal.js keys
    exclude_keys = ['title', 'display_name', 'date', 'template', 'code_theme']
    reveal_config = {k: v for k, v in metadata.items() if k not in exclude_keys}

    # Defaults for the frontmatter
    defaults = {
        "hash": True,
        "center": True,
        "controls": False,
        "progress": True,
        "transition": "slide",
        "slideNumber": "c/t",
        "pdfMaxPagesPerSlide": 1,
        "markdown": {"smartypants": True},
        "display": "flex",
    }
    for key, value in defaults.items():
        reveal_config.setdefault(key, value)

    # 5. Load Template and Perform Replacements
    template_text = Path(template_path).read_text()

    # Title
    final_html = template_text.replace("{{TITLE}}", metadata.get("title", "Presentation"))

    # Code highlight
    # Default to zenburn if not specified in YAML
    h_theme = metadata.get("code_theme", "base16/zenburn")
    final_html = final_html.replace("{{HIGHLIGHT_THEME}}", h_theme)

    # Content
    final_html = final_html.replace("{{CONTENT}}", content_html)

    # Config (JSON injection)
    final_html = final_html.replace("{{CONFIG}}", json.dumps(reveal_config, indent=2))

    return final_html
