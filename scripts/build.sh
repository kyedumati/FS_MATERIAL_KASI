#!/usr/bin/env bash
# Build PDFs from training Markdown files.
# Usage:
#   ./scripts/build.sh                    # MYSQL (default)
#   ./scripts/build.sh fullstack          # FULL_STACK_PYTHON (teach + share same notes)
#   ./scripts/build.sh java               # FULL_STACK_JAVA
#   ./scripts/build.sh frontend           # shared FRONTEND/ (HTML/CSS/JS + React)
#   ./scripts/build.sh mysql
#   ./scripts/build.sh --force fullstack

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! python3 -c "import markdown, pygments" 2>/dev/null; then
  echo "Installing Python dependencies..."
  python3 -m pip install -r requirements.txt
fi

# Mermaid diagrams in PDF need Node (npx) + Chrome (already required for print).
if ! command -v npx >/dev/null 2>&1; then
  echo "warning: npx not found — Mermaid blocks will appear as code in PDFs." >&2
  echo "         Install Node.js to render diagrams: https://nodejs.org/" >&2
fi

ARGS=()
FORCE=false

for arg in "$@"; do
  case "$arg" in
    --force|-f)
      FORCE=true
      ;;
    python|PYTHON)
      echo "error: legacy PYTHON / PDF/PYTHON was removed. Use: $0 fullstack" >&2
      exit 1
      ;;
    mysql|MYSQL)
      ARGS+=(--course MYSQL)
      ;;
    sql|SQL)
      ARGS+=(--course SQL)
      ;;
    fullstack|FULL_STACK_PYTHON|full-stack|fs)
      ARGS+=(--course FULL_STACK_PYTHON)
      ;;
    java|JAVA|fullstack-java|full-stack-java|fs-java|FULL_STACK_JAVA)
      ARGS+=(--course FULL_STACK_JAVA)
      ;;
    frontend|FRONTEND|fe)
      ARGS+=(--course FRONTEND)
      ;;
    *)
      echo "Unknown argument: $arg"
      echo "Usage: $0 [--force] [fullstack|java|frontend|mysql|sql ...]"
      exit 1
      ;;
  esac
done

if $FORCE; then
  ARGS+=(--force)
fi

if ((${#ARGS[@]} > 0)); then
  python3 scripts/build_pdfs.py "${ARGS[@]}"
else
  python3 scripts/build_pdfs.py
fi
