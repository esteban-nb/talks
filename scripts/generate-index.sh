#!/bin/bash
set -e

declare -A DISPLAY_NAMES

# Load extracted display names
if [ -f display-names.txt ]; then
  while IFS=: read -r original_name display_name; do
    DISPLAY_NAMES["$original_name"]="$display_name"
  done < display-names.txt
fi

# Hash all generated directories
declare -A HASH_MAP
> hash-mapping.txt

for dir in slides/*/index.html; do
  if [ -f "$dir" ]; then
    talk_name=$(basename "$(dirname "$dir")")
    hash=$(echo -n "$talk_name-$(git rev-parse HEAD)" | shasum -a 256 | cut -c1-8)
    HASH_MAP["$talk_name"]="$hash"
    mv "slides/$talk_name" "slides/$hash"
    echo "$hash $talk_name" >> hash-mapping.txt
    echo "$talk_name -> $hash"
  fi
done

# Create index page
cat > slides/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
  <title>All Talks</title>
  <meta charset="utf-8">
  <style>
    body { font-family: Arial, sans-serif; max-width: 900px; margin: 50px auto; padding: 20px; line-height: 1.6; }
    h1 { color: #0366d6; border-bottom: 2px solid #0366d6; padding-bottom: 10px; }
    .talk { margin: 25px 0; padding: 25px; border: 1px solid #ddd; border-radius: 12px; background: #fafbfc; }
    .talk h2 { margin: 0 0 10px 0; }
    .talk h2 a { color: #0366d6; text-decoration: none; font-size: 1.4em; }
    .talk h2 a:hover { text-decoration: underline; }
    .hash { font-family: monospace; font-size: 0.8em; color: #666; margin-top: 5px; }
    .hidden .hash { display: none; }
    .hidden .talk:hover .hash { display: block; }
  </style>
</head>
<body>
  <h1>📽️ All Talks</h1>
EOF

HIDDEN=${HIDDEN_MODE:-false}

# Add talks to index
for talk_dir in slides/*/index.html; do
  if [ -f "$talk_dir" ]; then
    hash=$(basename "$(dirname "$talk_dir")")
    original_name=$(grep "^$hash " hash-mapping.txt | cut -d' ' -f2)
    display_name="${DISPLAY_NAMES[$original_name]:-$original_name}"
    
    HIDDEN_CLASS=""
    if [ "$HIDDEN" = "true" ]; then
      HIDDEN_CLASS="hidden"
    fi
    
    cat >> slides/index.html << EOF
<div class="talk $HIDDEN_CLASS">
  <h2><a href="$hash/">$display_name</a></h2>
  <div class="hash">$hash/</div>
</div>
EOF
  fi
done

cat >> slides/index.html << 'EOF'
</body>
</html>
EOF
