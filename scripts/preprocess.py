# TODO
# - add footers
# - Maybe define the choise of md patterns as global vars so we can change them

import re
from pathlib import Path
import json
import frontmatter
from typing import List, Callable

ALLOW_DASH_DELIM = False

# Basic HTML templates
SECTION_TEMPLATE = '<section data-markdown {}><textarea data-template>\n{}\n</textarea></section>'
VERTICAL_SECTION_TEMPLATE = "<section>\n{}\n</section>"
DEFAULT_ATTRIBUTES = ""

# All comment templates supported
ALL_TEMPLATES = [
    r"<!-- {content} -->",
    r"\[comment\]: # \({content}\)",
    r"\[comment\]: <> \({content}\)",
    r"\[comment\]: # \"{content}\"",
    r"\[//\]: # \({content}\)"
]

# General regex pattern
general_filler = r"\s*(.*?)\s*"
MASTER_PATTERN = "|".join([t.format(content=general_filler) for t in ALL_TEMPLATES])
comment_re = re.compile(MASTER_PATTERN, re.DOTALL | re.MULTILINE)

# Separator strings
H_SEPARATORS = [t.format(content="!!!") for t in ALL_TEMPLATES]
V_SEPARATORS = [t.format(content="|||") for t in ALL_TEMPLATES]
if ALLOW_DASH_DELIM:
    H_SEPARATORS.append("^\n---\n$")
    V_SEPARATORS.append("^\n--\n$")

def get_comment(line: str) -> str | None:
    match = comment_re.search(line)
    if match:
        content = next((g for g in match.groups() if g is not None), None)
        return content.strip() if content else ""
    return None

def outer_pipeline(
    presentation_markdown: List[str],
    inner_pipeline: Callable[[str], str]
) -> List[str]:
    """
    Slide segmentation: split by !!!/|||, apply inner_pipeline to slide content.
    """
    presentation: List[str] = []
    slide: List[str] = []
    vertical_slide: List[str] = []
    attributes = DEFAULT_ATTRIBUTES

    for line in presentation_markdown:
        content = get_comment(line)
        
        # Case 1: This line is a comment
        if content is not None:
            # Process comment content
            if "!!!" in content or (ALLOW_DASH_DELIM and "---" in content):
                # Horizontal slide break
                attributes = DEFAULT_ATTRIBUTES + " " + content.replace("!!!", "").strip()
                slide_content = "\n".join(slide)
                processed_content = inner_pipeline(slide_content)
                
                if vertical_slide:
                    vertical_slide.append(SECTION_TEMPLATE.format(attributes, processed_content))
                    presentation.append(VERTICAL_SECTION_TEMPLATE.format("\n".join(vertical_slide)))
                    vertical_slide = []
                else:
                    presentation.append(SECTION_TEMPLATE.format(attributes, processed_content))
                slide = []
                continue
            
            elif "|||" in content or (ALLOW_DASH_DELIM and "--" in content):
                # Vertical slide break
                attributes = DEFAULT_ATTRIBUTES + " " + content.replace("|||", "").strip()
                slide_content = "\n".join(slide)
                processed_content = inner_pipeline(slide_content)
                vertical_slide.append(SECTION_TEMPLATE.format(attributes, processed_content))
                slide = []
                continue
            
            # Non-delimiter comment - keep as-is
            slide.append(line)
            continue
        
        # Case 2: Regular markdown content
        slide.append(line)
    
    # Handle final slides
    if vertical_slide:
        slide_content = "\n".join(slide)
        processed_content = inner_pipeline(slide_content)
        vertical_slide.append(SECTION_TEMPLATE.format(attributes, processed_content))
        presentation.append(VERTICAL_SECTION_TEMPLATE.format("\n".join(vertical_slide)))
    elif slide:
        slide_content = "\n".join(slide)
        processed_content = inner_pipeline(slide_content)
        presentation.append(SECTION_TEMPLATE.format(DEFAULT_ATTRIBUTES, processed_content))
    
    return presentation

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

def inner_pipeline(content: str) -> str:
    content = transform_blocks(content)
    content = handle_fragments(content)

    return content

def process_markdown_to_html(md_path, template_path):
    """
    Reads MD, handles YAML, replaces template anchors.
    """
    # 1. Load markdown and frontmatter
    post = frontmatter.load(md_path)
    metadata = post.metadata
    content_lines = post.content.splitlines()

    # 2. Process content
    presentation_html = outer_pipeline(content_lines, inner_pipeline)
    content_html = "\n".join(presentation_html + [""])

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
