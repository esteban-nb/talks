import shutil
from pathlib import Path
from preprocess import process_markdown_blocks

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
TALKS_DIR = PROJECT_ROOT / "talks"
OUTPUT_DIR = PROJECT_ROOT / "slides"
VENDOR_DIR = PROJECT_ROOT / "vendor"

def setup_vendor_assets(target_dir: Path):
    """
    Copies required assets from Git submodules into the specific talk directory.
    """
    # Define source paths
    reveal_src = VENDOR_DIR / "reveal.js"
    
    # Define destination paths in the hashed talk folder
    target_path = Path(target_dir)
    
    # Copy Reveal.js Core (dist and plugin folders)
    try:
        shutil.copytree(reveal_src / "dist", target_path / "dist", dirs_exist_ok=True)
        shutil.copytree(reveal_src / "plugin", target_path / "plugin", dirs_exist_ok=True)
        print(f"Core Reveal.js assets copied to {target_dir}")
    except FileNotFoundError:
        print(f"Error: Submodule not found at {reveal_src}. Did you run 'git submodule update --init'?")

def build_talk(talk_path: Path):
    """Full workflow for a single talk."""
    ...
    # 1. hashed target directory (same as generate-index.sh)
    #    check, since it seems that revealjs already gives the option to hash
    # 2. setup Reveal.js assets
    # 3. process content: merge markdown + templates
    #    i.e. handle the {{CONTENT}} replacement in index-template.html

if __name__ == "__main__":
    for talk_folder in TALKS_DIR.iterdir():
        if talk_folder.is_dir() and (talk_folder / "slides.md").exists():
            print(f"Processing talk: {talk_folder.name}")
            build_talk(talk_folder)
