#!/usr/bin/env bash
# Pack Python Full Stack student batch: program + shared topics.
# Usage (from repo root): ./scripts/pack_student_share.sh
#
# Output layout (paths match repo root so Prev/Next links work):
#   dist/FULL_STACK_PYTHON_STUDENT/
#     FULL_STACK_PYTHON/   # stripped program
#     FRONTEND/            # HTML/CSS/JS + FRONTEND/REACT/
#     MYSQL/
#     START_HERE.md

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/dist/FULL_STACK_PYTHON_STUDENT"
PROG_SRC="$ROOT/FULL_STACK_PYTHON"
PROG_DEST="$DEST/FULL_STACK_PYTHON"

if [[ ! -d "$PROG_SRC" ]]; then
  echo "error: missing $PROG_SRC" >&2
  exit 1
fi
for dep in FRONTEND MYSQL; do
  if [[ ! -d "$ROOT/$dep" ]]; then
    echo "error: missing shared topic $ROOT/$dep" >&2
    exit 1
  fi
done
if [[ ! -d "$ROOT/FRONTEND/REACT" ]]; then
  echo "error: missing $ROOT/FRONTEND/REACT" >&2
  exit 1
fi

rm -rf "$DEST"
mkdir -p "$PROG_DEST"

rsync -a \
  --exclude '14_Trainer_Only/' \
  --exclude '**/solution/' \
  --exclude '*_KEY.md' \
  --exclude '.DS_Store' \
  --exclude '**/.DS_Store' \
  "$PROG_SRC/" "$PROG_DEST/"

for dep in FRONTEND MYSQL; do
  rsync -a \
    --exclude '**/solution/' \
    --exclude '.DS_Store' \
    --exclude '**/.DS_Store' \
    "$ROOT/$dep/" "$DEST/$dep/"
done

python3 "$ROOT/scripts/strip_trainer_sections.py" "$PROG_DEST"
python3 "$ROOT/scripts/strip_trainer_sections.py" "$DEST/FRONTEND"

cat > "$DEST/START_HERE.md" << 'EOF'
# Start here — Python Full Stack student pack

This folder mirrors the repo layout used by trainers.

| Folder | What it is |
|--------|------------|
| `FULL_STACK_PYTHON/` | Python program (calendar, Django, labs, placement) |
| `FRONTEND/` | Shared HTML / CSS / JS |
| `FRONTEND/REACT/` | Shared React |
| `MYSQL/` | Shared SQL labs (Weeks 10–11) |

1. Open [`FULL_STACK_PYTHON/00_Course_Guide/11_Session_Calendar_100.md`](FULL_STACK_PYTHON/00_Course_Guide/11_Session_Calendar_100.md).  
2. On frontend / React / SQL days, open the folder named in the calendar (`FRONTEND/`, `FRONTEND/REACT/`, `MYSQL/`).  
3. Type examples; use `labs/` or `15_Lab_Assets/` starters.  
4. Every even week, complete the matching paper in [`FULL_STACK_PYTHON/16_Assessments/`](FULL_STACK_PYTHON/16_Assessments/README.md).  
5. Submit projects with [`FULL_STACK_PYTHON/00_Course_Guide/05_Standard_Project_Deliverables.md`](FULL_STACK_PYTHON/00_Course_Guide/05_Standard_Project_Deliverables.md).  
6. Capstone MVP: [`FULL_STACK_PYTHON/00_Course_Guide/03_Capstone_CampusCart_One_Pager.md`](FULL_STACK_PYTHON/00_Course_Guide/03_Capstone_CampusCart_One_Pager.md).  

Interview **answers**, assessment **keys** (`*_KEY.md`), `14_Trainer_Only/`, and `solution/` folders are removed from this pack.
EOF

cat > "$DEST/README.md" << 'EOF'
# Python Full Stack — Student Batch Pack

**Schedule:** 20 weeks × 1h 15m — see Session Calendar inside `FULL_STACK_PYTHON/`.  
**Shared topics:** `FRONTEND/` (includes `REACT/`), `MYSQL/`.

## Start

→ [START_HERE.md](START_HERE.md)

## Program modules (Python-owned)

See [`FULL_STACK_PYTHON/README.md`](FULL_STACK_PYTHON/README.md) teaching order.  
Pointers: `FULL_STACK_PYTHON/06_Frontend/` and `10_React/` only redirect to the shared folders.
EOF

python3 - <<'PY'
from pathlib import Path
import re
root = Path("dist/FULL_STACK_PYTHON_STUDENT/FULL_STACK_PYTHON")
p = root / "00_Course_Guide/04_Required_MySQL_Labs_Checklist.md"
if p.exists():
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"\n\*\*Trainers:\*\*.*\n", "\n", t)
    p.write_text(t, encoding="utf-8")
PY

echo "Student pack ready: $DEST"
echo "Includes: FULL_STACK_PYTHON/ + FRONTEND/ (with REACT/) + MYSQL/"
