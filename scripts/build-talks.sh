#!/bin/bash
set -e

mkdir -p slides

# Load exclude list only
if [ -f .github/talks-config.yml ]; then
  EXCLUDE=$(yq e '.exclude[]' .github/talks-config.yml 2>/dev/null || echo "")
  HIDDEN=$(yq e '.hidden // false' .github/talks-config.yml 2>/dev/null || echo "false")
else
  EXCLUDE=""
  HIDDEN="false"
fi

echo "Excluding: [$EXCLUDE]"
echo "Hidden mode: $HIDDEN"

declare -A DISPLAY_NAMES

# Build all talks, skip excluded, extract display names
for talk in talks/*/slides.md; do
  if [ ! -f "$talk" ]; then continue; fi
  
  talk_name=$(basename "$(dirname "$talk")")
  
  # Skip excluded
  SKIP=false
  for pattern in $EXCLUDE; do
    if [[ "$talk_name" == $pattern ]]; then
      echo "⏭️ Excluded: $talk_name"
      SKIP=true
      break
    fi
  done
  
  if [ "$SKIP" = true ]; then continue; fi
  
  # Extract display_name from YAML frontmatter
  display_name=$(sed -n '/^---/,/^---/ { /display_name:/ { s/.*display_name: *"\?//; s/" *$//p; } }' "$talk" | head -1)
  if [ -z "$display_name" ]; then
    display_name="$talk_name"
  fi
  DISPLAY_NAMES["$talk_name"]="$display_name"
  echo "$talk_name -> '$display_name'"
  
  echo "🔨 Building $talk_name..."
  mdslides "$talk" --output_dir "slides/${talk_name}"
done

# Export display names for index script
for key in "${!DISPLAY_NAMES[@]}"; do
  echo "$key: ${DISPLAY_NAMES[$key]}" >> display-names.txt
done

echo "HIDDEN_MODE=$HIDDEN" >> $GITHUB_ENV
