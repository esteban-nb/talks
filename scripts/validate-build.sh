#!/bin/bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <target_dir>" >&2
    echo "Example: $0 slides" >&2
    exit 1
fi

TARGET_DIR="${1%/}"
shopt -s nullglob dotglob

# 0. Check output of build.py
if [[ ! -f "display-names.txt" ]]; then
    echo "Missing display-names.txt" >&2
    exit 1
fi

echo "display-names.txt found ($(wc -l < "display-names.txt") entries)"

# 1. Check TARGET_DIR exists
if [[ ! -d "${TARGET_DIR}" ]]; then
    echo "Directory not found: ${TARGET_DIR}" >&2
    exit 1
fi

# 2. Check shared assets exist
REQUIRED_SHARED=(
    "dist/reveal.js"
    "dist/reveal.css"
    "dist/reset.css"
    "plugin/notes/notes.js"
    "plugin/markdown/markdown.js"
    "plugin/highlight/highlight.js"
    "plugin/math/math.js"
    "plugin/zoom/zoom.js"
    "highlightjs/highlight.js"
    "assets/slides-style.css"
)

MISSING_ASSETS=()
for asset in "${REQUIRED_SHARED[@]}"; do
    if [[ ! -f "${TARGET_DIR}/${asset}" ]]; then
        MISSING_ASSETS+=("${asset}")
    fi
done

if [[ ${#MISSING_ASSETS[@]} -ne 0 ]]; then
    echo "Missing required assets:" >&2
    printf '  %s\n' "${MISSING_ASSETS[@]}" >&2
    exit 1
fi
echo "All ${#REQUIRED_SHARED[@]} shared assets present"

# 3. Validate each talk directory
talk_dirs=("${TARGET_DIR}"/*/index.html)
if [[ ${#talk_dirs[@]} -eq 0 ]] || [[ "${talk_dirs[0]}" == "${TARGET_DIR}/*/index.html" ]]; then
    echo "No index.html files found in ${TARGET_DIR}/*/" >&2
    ls -la "${TARGET_DIR}/" >&2 || true
    exit 1
fi

TALK_COUNT=${#talk_dirs[@]}
echo "Found ${TALK_COUNT} talk directories with index.html files"

for talk_dir in "${talk_dirs[@]}"; do
    echo "here 1"
    talk_name=$(basename "$(dirname "${talk_dir}")")
    echo "here 2"

    # Check index.html has Reveal.js structure
    if ! grep -q 'class="reveal"' "${talk_dir}"; then
        echo "  [${talk_name}] Missing .reveal container" >&2
        exit 1
    fi

    echo "here 3"

    # Check critical shared asset paths
    if ! grep -q '../dist/reveal.js' "${talk_dir}"; then
        echo "  [${talk_name}] Missing ../dist/reveal.js path reference" >&2
        exit 1
    fi

    echo "here 4"

    if ! grep -q 'Reveal\.initialize' "${talk_dir}"; then
        echo "  [${talk_name}] Missing Reveal.initialize() call" >&2
        exit 1
    fi

    echo "here 5"

    # Check display name exists in mapping
    if ! grep -q "^${talk_name}:" "${TARGET_DIR}/display-names.txt"; then
        echo "  [${talk_name}] Not in display-names.txt" >&2
    fi
    echo "here 6"
done

echo "last"

echo "${TALK_COUNT} talks validated"
