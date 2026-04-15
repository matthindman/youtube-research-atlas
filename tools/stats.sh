#!/usr/bin/env bash
# stats.sh — one-shot quantitative snapshot of the atlas.
#
# Prints:
#   - page counts by directory
#   - verification marker counts across all wiki pages
#   - source registry size and status breakdown
#   - claim registry size
#
# Useful as a weekly progress check during Phase 1.

set -euo pipefail

cd "$(dirname "$0")/.."

count_files() {
  find "$1" -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' '
}

echo "# Atlas stats — $(date +%Y-%m-%d)"
echo

echo "## Page counts"
printf "  %-30s %s\n" "wiki/sources"  "$(count_files wiki/sources)"
printf "  %-30s %s\n" "wiki/themes"   "$(count_files wiki/themes)"
printf "  %-30s %s\n" "wiki/methods"  "$(count_files wiki/methods)"
printf "  %-30s %s\n" "wiki/debates"  "$(count_files wiki/debates)"
printf "  %-30s %s\n" "wiki/papers"   "$(count_files wiki/papers)"
echo

echo "## Verification markers (wiki-wide)"
for marker in "🤖" "✓✓" "✓" "NEEDS CITATION"; do
  count=$(rg -o "\[$marker\]" wiki 2>/dev/null | wc -l | tr -d ' ')
  printf "  %-20s %s\n" "[$marker]" "$count"
done
echo

echo "## Source registry"
if [[ -f data/source-registry.yaml ]]; then
  total=$(rg -c "^  - id: " data/source-registry.yaml 2>/dev/null || echo 0)
  ingested=$(rg -c "status: ingested" data/source-registry.yaml 2>/dev/null || echo 0)
  pending=$(rg -c "status: pending" data/source-registry.yaml 2>/dev/null || echo 0)
  needs_upd=$(rg -c "status: needs_update" data/source-registry.yaml 2>/dev/null || echo 0)
  printf "  %-20s %s\n" "total"        "$total"
  printf "  %-20s %s\n" "ingested"     "$ingested"
  printf "  %-20s %s\n" "pending"      "$pending"
  printf "  %-20s %s\n" "needs_update" "$needs_upd"
fi
echo

echo "## Claim registry"
if [[ -f data/claim-registry.yaml ]]; then
  total=$(rg -c "^  - id: " data/claim-registry.yaml 2>/dev/null || echo 0)
  printf "  %-20s %s\n" "total" "$total"
fi
echo
