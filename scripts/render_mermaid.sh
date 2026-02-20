#!/usr/bin/env bash
# Try to render the Mermaid diagram using mermaid-cli (npx).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IN="$ROOT/docs/diagrams/mappings_diagram.mmd"
OUT_PNG="$ROOT/docs/diagrams/mappings_diagram.png"

if ! command -v npx >/dev/null 2>&1; then
  echo "npx not found. Install Node.js and try: npm install -g @mermaid-js/mermaid-cli"
  exit 2
fi

echo "Rendering $IN -> $OUT_PNG using mermaid-cli..."
npx -y @mermaid-js/mermaid-cli -i "$IN" -o "$OUT_PNG"
echo "Rendered: $OUT_PNG"
