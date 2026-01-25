#!/usr/bin/env bash

set -euo pipefail

PORT=8000
TARGET_OUTPUT="${TARGET_OUTPUT:-slides}"
AUTO_OPEN="${AUTO_OPEN:-false}"

if [ ! -d "$TARGET_OUTPUT" ]; then
  echo "Error: target output directory not found: $TARGET_OUTPUT" >&2
  exit 1
fi

cd "$TARGET_OUTPUT"

URL="http://localhost:${PORT}/"

echo "Serving slides from: $(pwd)"

# Auto-open browser
if [ "$AUTO_OPEN" = "true" ]; then
  if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$URL" >/dev/null 2>&1 &
  elif command -v open >/dev/null 2>&1; then
    open "$URL" >/dev/null 2>&1 &
  else
    echo "Warning: no known opener (xdg-open/open) found; cannot auto-open browser"
    echo "Open: http://localhost:${PORT}/"
  fi
else
  echo "Open: http://localhost:${PORT}/"
fi

echo "Press Ctrl+C to stop"

python3 -m http.server "$PORT"
