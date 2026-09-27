#!/usr/bin/env bash
# Build and push the site to the gh-pages branch (served by GitHub Pages).
set -euo pipefail
cd "$(dirname "$0")/.."
./scripts/build_site.sh
REMOTE=$(git remote get-url origin)
TMP=$(mktemp -d)
cp -R public/. "$TMP/"
cd "$TMP"
git init -q -b gh-pages
git add -A
git commit -q -m "Deploy site $(date -u +%Y-%m-%dT%H:%MZ)"
git push -q -f "$REMOTE" gh-pages
echo "Published to gh-pages"
