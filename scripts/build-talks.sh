#!/bin/bash
set -euo pipefail

OUTPUT_DIR="slides"
mkdir -p "${OUTPUT_DIR:?}"

if [[ -f ".github/talks-config.yml" ]]; then
  EXCLUDE=$(yq e '.exclude[]' .github/talks-config.yml 2>/dev/null || echo "")
  HIDDEN=$(yq e '.hidden // false' .github/talks-config.yml 2>/dev/null || echo "false")
else
  EXCLUDE=""
  HIDDEN="false"
fi

echo "Excluding: [${EXCLUDE}]"
echo "Hidden mode: ${HIDDEN}"

declare -A DISPLAY_NAMES

for talk in talks/*/slides.md; do
  [[ ! -f "${talk}" ]] && continue
  
  talk_name=$(basename "$(dirname "${talk}")")
  
  SKIP=false
  for pattern in ${EXCLUDE}; do
    if [[ "${talk_name}" == "${pattern}" ]]; then
      echo "Excluded: ${talk_name}"
      SKIP=true
      break
    fi
  done
  
  [[ "${SKIP}" == "true" ]] && continue
  
  display_name=$(sed -n '/^---/,/^---/ { /display_name:/ { s/.*display_name: *"\?//; s/" *$//p; } }' "${talk}" | head -1) || true

  if [[ -z "${display_name}" ]]; then
    display_name="${talk_name}"
  fi
  
  DISPLAY_NAMES["${talk_name}"]="${display_name}"
  echo "${talk_name} -> '${display_name}'"

  echo "Building ${talk_name}..."

  mdslides "${talk}" --output_dir "${OUTPUT_DIR:?}/${talk_name:?}"
done

: > "display-names.txt"
for key in "${!DISPLAY_NAMES[@]}"; do
  echo "${key}: ${DISPLAY_NAMES[${key}]}" >> "display-names.txt"
done

if [[ -n "${GITHUB_ENV:-}" ]]; then
  echo "HIDDEN_MODE=${HIDDEN}" >> "${GITHUB_ENV}"
fi
