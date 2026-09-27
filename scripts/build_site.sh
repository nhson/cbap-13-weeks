#!/usr/bin/env bash
# Build the static site into ./public (Quartz v4, pinned).
set -euo pipefail
cd "$(dirname "$0")/.."
QUARTZ_REF="v4.5.2"
if [ ! -d .quartz ]; then
  git clone --depth 1 --branch v4 https://github.com/jackyzha0/quartz.git .quartz
fi
(cd .quartz && [ -d node_modules ] || npm ci --no-audit --no-fund)
cp site/quartz.config.ts site/quartz.layout.ts .quartz/
python3 site/build_content.py .quartz/content
(cd .quartz && npx quartz build -o ../public)
touch public/.nojekyll
echo "Built site in ./public"
