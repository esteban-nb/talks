#!/bin/bash
set -euo pipefail
set -o pipefail

declare -A DISPLAY_NAMES
declare -A COMMIT_DATES
declare -A HASH_MAP

main() {
  load_display_names
  process_talks
  generate_index
  report
}

load_display_names() {
  if [[ -f display-names.txt ]]; then
    while IFS=: read -r original_name display_name; do
      [[ -z "${original_name// }" ]] && continue
      DISPLAY_NAMES["$original_name"]="$display_name"
    done < display-names.txt
  fi
}

process_talks() {
  : > hash-mapping.txt
  : > valid-talks.txt

  for dir in slides/*/index.html; do
    [[ ! -f "$dir" ]] && continue

    local talk_name
    talk_name=$(basename "$(dirname "$dir")")

    if [[ ! -f "talks/$talk_name/slides.md" ]]; then
      printf 'Skipping %s (no slides.md)\n' "$talk_name" >&2
      rm -rf "slides/$talk_name"
      continue
    fi

    local hash
    if ! hash=$(printf '%s' "$talk_name-$(git rev-parse HEAD)" | shasum -a 256 | cut -c1-8); then
      printf 'Hash generation failed for %s\n' "$talk_name" >&2
      continue
    fi

    HASH_MAP["$talk_name"]="$hash"
    mv "slides/$talk_name" "slides/$hash"
    printf '%s %s\n' "$hash" "$talk_name" >> hash-mapping.txt
    printf '%s -> %s\n' "$talk_name" "$hash"

    local commit_date
    if ! commit_date=$(git log -1 --format=%cI -- "talks/$talk_name/" 2>/dev/null); then
      commit_date="1970-01-01T00:00:00Z"
    fi

    COMMIT_DATES["$talk_name"]="$commit_date"
    printf '%s\n' "$talk_name" >> valid-talks.txt
  done
}

generate_index() {
  cat > slides/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
  <title>All Talks</title>
  <meta charset="utf-8">
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      line-height: 1.6;
      color: #333;
    }
    h1 {
      font-size: 2em;
      font-weight: 600;
      color: #1a1a1a;
      border-bottom: 2px solid #e5e5e5;
      padding-bottom: 15px;
      margin-bottom: 30px;
    }
    .talk-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .talk-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 12px 0;
    }
    .talk-title {
      white-space: nowrap;
    }
    .talk-link {
      font-size: 1.1em;
      color: #0366d6;
      text-decoration: none;
      font-weight: 500;
    }
    .talk-link:hover { color: #0969da; }
    .talk-divider {
      flex: 1;
      height: 1px;
      background: #e0e0e0;
      margin-top: 0.2em;
    }
    .talk-date {
      white-space: nowrap;
      font-size: 0.95em;
      color: #666;
      font-weight: 500;
    }
    .hash {
      font-family: 'SF Mono', Monaco, monospace;
      font-size: 0.8em;
      color: #999;
      margin-left: 8px;
    }
    .hidden .hash { display: none; }
    .hidden .talk-item:hover .hash { display: inline; }
  </style>
</head>
<body>
  <h1>All Talks</h1>
  <ul class="talk-list">
EOF

  local hidden
  hidden="${HIDDEN_MODE:-false}"

  if [[ -s valid-talks.txt ]]; then
    {
      while read -r talk_name; do
        local commit_date hash display_name month_year
        commit_date="${COMMIT_DATES[$talk_name]}"
        hash="${HASH_MAP[$talk_name]}"
        display_name="${DISPLAY_NAMES[$talk_name]:-$talk_name}"

        if ! month_year=$(date -d "$commit_date" +"%b %Y" 2>/dev/null); then
          month_year="Unknown"
        fi

        printf '%s\t%s\t%s\t%s\n' "$commit_date" "$hash" "$display_name" "$month_year"
      done < valid-talks.txt
    } | sort -r | while IFS=$'\t' read -r _ hash display_name month_year; do
      local hidden_class=""
      [[ "$hidden" == "true" ]] && hidden_class="hidden"

      cat >> slides/index.html << EOF
    <li class="talk-item $hidden_class">
      <div class="talk-title">
        <a href="$hash/" class="talk-link">$display_name</a><span class="hash">$hash/</span>
      </div>
      <div class="talk-divider"></div>
      <div class="talk-date">$month_year</div>
    </li>
EOF
    done
  fi

  cat >> slides/index.html << 'EOF'
  </ul>
</body>
</html>
EOF
}

report() {
  local talk_count
  if ! talk_count=$(wc -l < hash-mapping.txt 2>/dev/null); then
    talk_count=0
  fi
  printf 'Index generated with %s talks\n' "$talk_count"
}

main
