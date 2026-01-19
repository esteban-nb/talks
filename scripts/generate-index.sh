#!/bin/bash
set -euo pipefail

declare -A DISPLAY_NAMES
declare -A COMMIT_DATES
declare -A HASH_MAP

# Configuration
TEMPLATE_FILE="templates/index-template.html"
ASSETS_SRC="templates/assets"
OUTPUT_DIR="${OUTPUT_DIR:-slides}"
ASSETS_DEST="${OUTPUT_DIR}/assets"

main() {
  load_display_names
  process_talks
  setup_assets
  generate_index
  report
}

load_display_names() {
  if [[ -f "display-names.txt" ]]; then
    while IFS=: read -r original_name display_name; do
      [[ -z "${original_name// }" ]] && continue
      DISPLAY_NAMES["${original_name}"]="${display_name}"
    done < "display-names.txt"
  fi
}

process_talks() {
  : > "hash-mapping.txt"
  : > "valid-talks.txt"

  # Ensure the directory exists before iteration
  mkdir -p "${OUTPUT_DIR:?}"

  for dir in "${OUTPUT_DIR}"/*/index.html; do
    [[ ! -f "${dir}" ]] && continue

    local talk_name
    talk_name=$(basename "$(dirname "${dir}")")

    if [[ ! -f "talks/${talk_name}/slides.md" ]]; then
      printf 'Skipping %s (no slides.md)\n' "${talk_name}" >&2
      # Safety: ensure OUTPUT_DIR and talk_name are not empty/unset
      rm -rf "${OUTPUT_DIR:?}/${talk_name:?}"
      continue
    fi

    local hash
    local hasher="shasum -a 256"
    command -v shasum >/dev/null 2>&1 || hasher="sha256sum"

    hash=$(printf '%s' "${talk_name}-$(git rev-parse HEAD)" | ${hasher} | cut -c1-8)

    HASH_MAP["${talk_name}"]="${hash}"
    mv "${OUTPUT_DIR:?}/${talk_name:?}" "${OUTPUT_DIR:?}/${hash:?}"
    printf '%s %s\n' "${hash}" "${talk_name}" >> "hash-mapping.txt"
    printf '%s -> %s\n' "${talk_name}" "${hash}"

    local commit_date
    if ! commit_date=$(git log -1 --format=%cI -- "talks/${talk_name}/" 2>/dev/null); then
      commit_date="1970-01-01T00:00:00Z"
    fi

    COMMIT_DATES["${talk_name}"]="${commit_date}"
    printf '%s\n' "${talk_name}" >> "valid-talks.txt"
  done
}

setup_assets() {
  printf 'Setting up assets...\n'
  mkdir -p "${ASSETS_DEST:?}"
  if [[ -d "${ASSETS_SRC}" ]]; then
    cp -r "${ASSETS_SRC}"/* "${ASSETS_DEST}/"
  else
    printf 'Warning: %s not found. CSS/JS will be missing.\n' "${ASSETS_SRC}" >&2
  fi
}

generate_index() {
  local list_items=""
  local hidden="${HIDDEN_MODE:-false}"

  if [[ -s "valid-talks.txt" ]]; then
    list_items=$(
      {
        while read -r talk_name; do
          local commit_date hash display_name month_year

          commit_date="${COMMIT_DATES[${talk_name}]}"
          hash="${HASH_MAP[${talk_name}]}"
          display_name="${DISPLAY_NAMES[${talk_name}]:-${talk_name}}"
          month_year=$(date -d "${commit_date}" +"%b %Y" 2>/dev/null || echo "Unknown")

          printf '%s\t%s\t%s\t%s\n' "${commit_date}" "${hash}" "${display_name}" "${month_year}"
        done < "valid-talks.txt"
      } | sort -r | while IFS=$'\t' read -r _ hash display_name month_year; do
        local hidden_class=""
        [[ "${hidden}" == "true" ]] && hidden_class="hidden"

        printf '<li class="talk-item %s">
          <div class="talk-title">
            <a href="%s/" class="talk-link">%s</a><span class="hash">%s/</span>
          </div>
          <div class="talk-divider"></div>
          <div class="talk-date">%s</div>
        </li>' "${hidden_class}" "${hash}" "${display_name}" "${hash}" "${month_year}"
      done
    )
  fi

  if [[ -f "${TEMPLATE_FILE}" ]]; then
    export LIST_ITEMS="${list_items}"
    perl -pe 's|\{\{CONTENT\}\}|$ENV{LIST_ITEMS}|g' "${TEMPLATE_FILE}" > "${OUTPUT_DIR}/index.html"
    printf 'Generated %s/index.html from template\n' "${OUTPUT_DIR}"
  else
    printf 'Error: Template %s not found!\n' "${TEMPLATE_FILE}" >&2
    exit 1
  fi
}

report() {
  local talk_count=0
  [[ -f "hash-mapping.txt" ]] && talk_count=$(wc -l < "hash-mapping.txt")
  printf 'Index generated with %s talks\n' "${talk_count}"
}

main
