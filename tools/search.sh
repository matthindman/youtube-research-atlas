#!/usr/bin/env bash
# search.sh — ripgrep-based search across the atlas
#
# Usage:
#   tools/search.sh "pattern"                    # all wiki + data
#   tools/search.sh -s "pattern"                 # source cards only
#   tools/search.sh -t "pattern"                 # themes only
#   tools/search.sh -p "pattern"                 # paper dossiers only
#   tools/search.sh -r "pattern"                 # registries only
#
# Returns file:line:match for easy editor-jump.

set -euo pipefail

# Move to repo root (script lives in tools/).
cd "$(dirname "$0")/.."

SCOPE="wiki data"
while getopts "stprh" opt; do
  case "$opt" in
    s) SCOPE="wiki/sources" ;;
    t) SCOPE="wiki/themes" ;;
    p) SCOPE="wiki/papers" ;;
    r) SCOPE="data" ;;
    h)
      sed -n '2,12p' "$0"
      exit 0
      ;;
    *) exit 2 ;;
  esac
done
shift $((OPTIND - 1))

if [[ $# -lt 1 ]]; then
  echo "Usage: tools/search.sh [-s|-t|-p|-r] pattern" >&2
  exit 2
fi

PATTERN="$1"

if ! command -v rg >/dev/null 2>&1; then
  echo "error: ripgrep (rg) is required" >&2
  exit 1
fi

# shellcheck disable=SC2086
rg --line-number --color=auto --smart-case "$PATTERN" $SCOPE
