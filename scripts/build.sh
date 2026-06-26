#!/usr/bin/env bash
# Build PDFs from training Markdown files.
# Usage:
#   ./scripts/build.sh              # all courses
#   ./scripts/build.sh mysql        # one course
#   ./scripts/build.sh python mysql # multiple courses
#   ./scripts/build.sh --force      # rebuild everything

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! python3 -c "import markdown, pygments" 2>/dev/null; then
  echo "Installing Python dependencies..."
  python3 -m pip install -r requirements.txt
fi

ARGS=()
FORCE=false

for arg in "$@"; do
  case "$arg" in
    --force|-f)
      FORCE=true
      ;;
    python|PYTHON)
      ARGS+=(--course PYTHON)
      ;;
    mysql|MYSQL)
      ARGS+=(--course MYSQL)
      ;;
    sql|SQL)
      ARGS+=(--course SQL)
      ;;
    *)
      echo "Unknown argument: $arg"
      echo "Usage: $0 [--force] [python|mysql|sql ...]"
      exit 1
      ;;
  esac
done

if $FORCE; then
  ARGS+=(--force)
fi

python3 scripts/build_pdfs.py "${ARGS[@]}"
