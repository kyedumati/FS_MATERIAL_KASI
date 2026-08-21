#!/usr/bin/env bash
# Optional mirror of teaching notes (same content as class — one material policy).
# Preferred share habit: after each module, send that module’s PDF from PDF/FULL_STACK_PYTHON/.
#
# Usage (from repo root): ./scripts/pack_student_share.sh
#
# Output layout (paths match repo root so Prev/Next links work):
#   dist/FULL_STACK_PYTHON_STUDENT/
#     FULL_STACK_PYTHON/   # same notes as trainers (no answer stripping)
#     FRONTEND/            # HTML/CSS/JS + FRONTEND/REACT/
#     MYSQL/
#     START_HERE.md
#
# Still excluded (private): 14_Trainer_Only/, **/solution/, *_KEY.md

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

# One material policy: do NOT strip Practice Model answers — same notes as class PDFs.

cat > "$DEST/START_HERE.md" << 'EOF'
# Start here — Python Full Stack notes

**One material:** these files match what trainers teach. Practice **Model answer** blocks are included.

| Folder | What it is |
|--------|------------|
| `FULL_STACK_PYTHON/` | Python program (calendar, Django, labs, placement) |
| `FRONTEND/` | Shared HTML / CSS / JS |
| `FRONTEND/REACT/` | Shared React |
| `MYSQL/` | Shared SQL labs (Weeks 10–11) |

## How you usually receive material

Trainers share **one module PDF at a time** after that module is taught (from `PDF/FULL_STACK_PYTHON/…`).  
This full folder is optional reference if your batch also gets a Drive/LMS zip.

1. Open [`FULL_STACK_PYTHON/Session_Calendar_100.md`](FULL_STACK_PYTHON/Session_Calendar_100.md).  
2. On frontend / React / SQL days, open the folder named in the calendar.  
3. Type examples; use `labs/` or `15_Lab_Assets/` starters (not `solution/`).  
4. Every even week, complete the matching paper in [`FULL_STACK_PYTHON/16_Assessments/`](FULL_STACK_PYTHON/16_Assessments/README.md) (student papers only — no `*_KEY`).  
5. Capstone: [`FULL_STACK_PYTHON/Capstone_CampusCart_One_Pager.md`](FULL_STACK_PYTHON/Capstone_CampusCart_One_Pager.md).  

**Not included:** `14_Trainer_Only/`, lab `solution/` folders, assessment `*_KEY.md` files.
EOF

cat > "$DEST/README.md" << 'EOF'
# Python Full Stack — Shared Notes (same as class)

**Schedule:** 20 weeks × 1h 15m — see Session Calendar inside `FULL_STACK_PYTHON/`.  
**Shared topics:** `FRONTEND/` (includes `REACT/`), `MYSQL/`.

## Start

→ [START_HERE.md](START_HERE.md)

Preferred delivery: module PDF after each teach day. See program README for teaching order.
EOF

echo "Share mirror ready: $DEST"
echo "Same content as class (Model answers kept). Excludes: 14_Trainer_Only/, solution/, *_KEY.md"
echo "Preferred: share individual PDFs from PDF/FULL_STACK_PYTHON/ after each module."
