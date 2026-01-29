# TODO
# - add footers
# - check attr inheritance / handing for vertical wrappers
# - write a test such as:
#       DEFAULT_ATTRIBUTES = 'data-transition="fade" data-background="black"'
#       comment = 'data-background="red" data-state="intro"'
#       normalize_attrs(DEFAULT_ATTRIBUTES, comment)

import re
import json
from pathlib import Path
from typing import List, Callable

import frontmatter

# -------------------------------------------------
# Configuration
# -------------------------------------------------

ALLOW_DASH_DELIM = False
DEFAULT_ATTRIBUTES = ""

SECTION_RAW = """<section {attrs}>
{content}
</section>"""

SECTION_MD = """<section data-markdown {attrs}>
<script type="text/template">
{content}
</script>
</section>"""

DIVISION_MD = """<div data-markdown class="tight-block" {attrs}>
<textarea text/template">
{content}
</textarea>
</div>"""

COMMENT_TEMPLATES = [
    r"<!-- {content} -->",
    r"\[comment\]: # \({content}\)",
    r"\[comment\]: <> \({content}\)",
    r"\[comment\]: # \"{content}\"",
    r"\[//\]: # \({content}\)",
    r"\[//\]: # \"{content}\""
]

blocks = ["donot", "alert", "zoom", "info", "example", "note"]

BLOCK_PATTERN = rf":::\s*({'|'.join(blocks)})\s*\|\s*(.*?)\n(.*?)\n\s*:::"
MD_PATTERN = rf"<md(?:\\s+(.*))?>\\s*(.*?)\\s*</md>"
COMMENT_PATTERN = "|".join(
    t.format(content=r"\s*(.*?)\s*") for t in COMMENT_TEMPLATES
)
FRAGMENT_PATTERN = r"<f:([\d, ]+)>"

comment_re = re.compile(COMMENT_PATTERN, re.DOTALL | re.MULTILINE)
block_re = re.compile(BLOCK_PATTERN, re.DOTALL | re.MULTILINE)  
mdiv_re = re.compile(MD_PATTERN, re.DOTALL | re.MULTILINE)
frag_re = re.compile(FRAGMENT_PATTERN, re.DOTALL | re.MULTILINE)

# -------------------------------------------------
# Helpers
# -------------------------------------------------

def get_comment(line: str) -> str | None:
    match = comment_re.search(line)
    if not match:
        return None
    content = next((g for g in match.groups() if g), "")
    return content.strip()


def normalize_attrs(*parts: str) -> str:
    """
    Merge attribute fragments into a unique, ordered attribute string.
    Order: keyed attrs first (last-wins), then booleans.
    """
    kv_attrs: dict[str, str] = {}
    bool_attrs: set[str] = set()

    for part in parts:
        if not part:
            continue

        tokens = part.strip().split()
        for tok in tokens:
            if "=" in tok:
                key, value = tok.split("=", 1)
                kv_attrs[key] = f"{key}={value}"
            else:
                bool_attrs.add(tok)

    # Preserve deterministic order:
    # keyed attributes first, then booleans
    merged = list(kv_attrs.values()) + sorted(bool_attrs)
    return " ".join(merged)


def fmt_section_attrs(attr: str) -> str:
    """
    Format attributes for a markdown slide.
    Ensures:
      - data-markdown is always present
      - default attributes come foirst, so they get
        overriden by local attributes (in case of conflict)
    """
    sattr = attr.strip()
    raw_bool = False

    if sattr.startswith("raw:"):
        raw_bool = True
        parts = sattr.removeprefix("raw:").strip()
        merged = normalize_attrs(parts)
    elif sattr.startswith("only:"):
        parts = sattr.removeprefix("only:").strip()
        merged = normalize_attrs(parts)
    else:
        merged = normalize_attrs(DEFAULT_ATTRIBUTES, sattr)

    return raw_bool, merged


# -------------------------------------------------
# Inner pipeline
# -------------------------------------------------

def transform_blocks(text: str) -> str:
    """
    Converts ::: block | Title syntax into HTML blocks.
    """
    def replacer(match):
        b_type = match.group(1).lower()
        title = match.group(2).strip()
        body = match.group(3).strip()

        css_map = {
            "donot": "donot",
            "alert": "alert",
            "zoom": "zoom",
            "info": "info",
            "example": "note",
            "note": "pin",
        }
        cls = css_map.get(b_type, "std")

        return (
            f'<div class="block block-{cls}">\n'
            f'  <div class="block-title">{title}</div>\n'
            f'  <div class="block-body">\n\n'
            f'{body}\n\n'
            f'  </div>\n'
            f'</div>'
        )

    return block_re.sub(replacer, text)


def handle_fragments(text: str) -> str:
    """
    Converts <f> shorthand into Reveal.js fragment comments.
    """
    text.replace(
        " <f>",
        ' <!-- .element: class="fragment" -->'
    )

    def format_fragment(match):
        indices = match.group(1)
        clean_indices = ",".join(i.strip() for i in indices.split(','))

        return f'<!-- .element: class="fragment" data-fragment-index="{clean_indices}" -->'

    return frag_re.sub(format_fragment, text)


def replace_md_divisions(text: str) -> str:
    """
    Replace <md attrs>content</md> blocks with markdown div template.
    """
    def md_replacement(match):
        attrs = match.group(1) or ""
        content = match.group(2).strip()
        return DIVISION_MD.format(attrs=attrs, content=content)
    
    return mdiv_re.sub(md_replacement, text)


def inner_pipeline(content: str) -> str:
    content = transform_blocks(content)
    content = handle_fragments(content)
    content = replace_md_divisions(content)
    return content


# -------------------------------------------------
# Outer pipeline (slide segmentation)
# -------------------------------------------------

def outer_pipeline(
    presentation_markdown: List[str],
    inner_pipeline: Callable[[str], str],
) -> List[str]:
    slides: List[str] = []

    h_stack: List[str] = []     # vertical slides in current horizontal
    buffer: List[str] = []      # markdown buffer
    pending_attrs: str = ""     # attrs for *next* slide only

    def flush_buffer_into_vertical():
        nonlocal buffer, h_stack, pending_attrs
        if not buffer:
            return

        processed = inner_pipeline("\n".join(buffer))
        raw, attrs = fmt_section_attrs(pending_attrs)

        if raw:
            h_stack.append(
                SECTION_RAW.format(
                    attrs=attrs,
                    content=processed
                )
            )
        else:
            h_stack.append(
                SECTION_MD.format(
                    attrs=attrs,
                    content=processed
                )
            )
        buffer = []
        pending_attrs = ""

    def flush_horizontal():
        nonlocal h_stack
        if not h_stack:
            return

        if len(h_stack) == 1:
            slides.append(h_stack[0])
        else:
            slides.append(
                SECTION_RAW.format(
                    attrs="",
                    content="\n".join(h_stack)
                )
            )
        h_stack = []

    for line in presentation_markdown:
        comment = get_comment(line)

        if comment is not None:
            # Horizontal break
            if "!!!" in comment or (ALLOW_DASH_DELIM and "---" in comment):
                flush_buffer_into_vertical()
                flush_horizontal()
                pending_attrs = comment.replace("!!!", "").strip()
                continue

            # Vertical break
            if "|||" in comment or (ALLOW_DASH_DELIM and "--" in comment):
                flush_buffer_into_vertical()
                pending_attrs = comment.replace("|||", "").strip()
                continue

        buffer.append(line)

    # Final flush
    flush_buffer_into_vertical()
    flush_horizontal()

    return slides


# -------------------------------------------------
# Full pipeline (HTML-injection)
# -------------------------------------------------

def process_markdown_to_html(md_path: str, template_path: str) -> str:
    post = frontmatter.load(md_path)
    metadata = post.metadata
    content_lines = post.content.splitlines()

    slides_html = outer_pipeline(content_lines, inner_pipeline)
    content_html = "\n".join(slides_html) + "\n"

    # Reveal config
    exclude_keys = {
        "title", "display_name", "date", "template"
    }

    reveal_config = {
        k: v for k, v in metadata.items()
        if k not in exclude_keys
    }

    defaults = {
        "hash": True,
        "center": True,
        "controls": False,
        "progress": True,
        "transition": "slide",
        "slideNumber": "c/t",
        "pdfMaxPagesPerSlide": 1,
        "markdown": {"smartypants": True},
    }

    for k, v in defaults.items():
        reveal_config.setdefault(k, v)

    template = Path(template_path).read_text()

    template = template.replace(
        "{{TITLE}}",
        metadata.get("title", "Presentation")
    )

    template = template.replace("{{CONTENT}}", content_html)
    template = template.replace(
        "{{CONFIG}}",
        json.dumps(reveal_config, indent=2)
    )

    return template
