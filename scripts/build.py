import os
import shutil
import hashlib
import yaml
from pathlib import Path
from preprocess import process_markdown_to_html

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
TALKS_DIR = PROJECT_ROOT / "talks"
TARGET_OUTPUT = os.getenv("OUTPUT_DIR", "slides")
OUTPUT_DIR = PROJECT_ROOT / TARGET_OUTPUT
VENDOR_DIR = PROJECT_ROOT / "vendor"
TEMPLATE_PATH = PROJECT_ROOT / "templates/slides-template.html"
CONFIG_PATH = PROJECT_ROOT / ".github/talks-config.yml"

def setup_shared_vendor_assets():
    """
    Copies required assets from Git submodules into the root of the slides directory.
    Retains your defensive logic to ensure submodules exist.
    """
    reveal_src = VENDOR_DIR / "reveal.js"
    highlight_src = VENDOR_DIR / "highlightjs-cdn-release"

    # Define Destinations
    shared_dist = OUTPUT_DIR / "dist"
    shared_plugin = OUTPUT_DIR / "plugin"
    shared_highlight = OUTPUT_DIR / "highlightjs"

    try:
        # Core Reveal.js
        shutil.copytree(reveal_src / "dist", shared_dist, dirs_exist_ok=True)
        shutil.copytree(reveal_src / "plugin", shared_plugin, dirs_exist_ok=True)

        # Highlight.js engine and styles
        shared_highlight.mkdir(parents=True, exist_ok=True)
        shutil.copy(highlight_src / "build/highlight.min.js", shared_highlight / "highlight.js")
        shutil.copytree(highlight_src / "build/styles", shared_highlight / "styles", dirs_exist_ok=True)

        # Custom shared assets (Pyramid, CSS)
        shutil.copytree(PROJECT_ROOT / "templates/assets", OUTPUT_DIR / "assets", dirs_exist_ok=True)

        print(f"Shared assets successfully deployed to {OUTPUT_DIR}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Did you run 'git submodule update --init --recursive'?")
        exit(1)

def build_all_talks():
    """
    Build unhashed directories (slides/talk_name/index.html).
    Hashing/indexing done by generate-index.sh.
    """
    # Load CI config
    config = {"exclude": [], "hidden": False}
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            config.update(yaml.safe_load(f) or {})

    # Reset and setup
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    setup_shared_vendor_assets()

    display_names = {}

    for talk_path in TALKS_DIR.iterdir():
        if not talk_path.is_dir():
            continue

        talk_name = talk_path.name
        md_file = talk_path / "slides.md"

        # Skip if no slides.md or explicitly excluded
        if not md_file.exists() or talk_name in config["exclude"]:
            print(f"Skipping: {talk_name} (no slides.md or excluded)")
            continue

        # Output dir (unhashed)
        target_dir = OUTPUT_DIR / talk_name
        target_dir.mkdir(parents=True, exist_ok=True)

        print(f"Building: {talk_name} -> slides/{talk_name}/")

        # Preprocessing (blocks, yaml, delimiters)
        html_content = process_markdown_to_html(md_file, TEMPLATE_PATH)
        (target_dir / "index.html").write_text(html_content)

        # Extract display name from YAML frontmatter for generate-index.sh
        try:
            with open(md_file) as f:
                # Read YAML frontmatter
                content = f.read()
                meta = yaml.safe_load(content.split('---', 2)[1]) if '---' in content else {}
                display_names[talk_name] = meta.get("display_name", talk_name)
        except Exception as e:
            print(f"Warning: Could not parse frontmatter for {talk_name}: {e}")
            display_names[talk_name] = talk_name

    # Save display-names.txt for generate-index.sh
    with open(PROJECT_ROOT / "display-names.txt", "w") as f:
        for name, display in display_names.items():
            f.write(f"{name}: {display}\n")

    print(f"Built {len(display_names)} talks; display-names.txt written")
    print("Ready for generate-index.sh (hashing + index generation)")

if __name__ == "__main__":
    build_all_talks()
