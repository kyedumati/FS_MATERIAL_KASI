# One Material Policy — Teach and Share the Same Notes

**Rule:** One version of module notes. Teach from `PYTHON/` (and shared `GIT/`, `FRONTEND/`, `MYSQL/`). Share **that same** content with students — usually the **module PDF after that module is taught**.

Do **not** maintain a second “student-only” rewrite of the syllabus, and do **not** strip Practice **Model answer** blocks for sharing.

---

## What you open every day

| Role | Open this | Do not open for class |
|------|-----------|------------------------|
| **Trainer (live class)** | Same week’s module `.md` | Legacy parallel packs |
| **Student (after the module)** | Same module’s PDF (or `.md`) | Assessment `*_KEY.md`, lab `solution/` |
| **Trainer (private)** | `14_Trainer_Only/` + `*_KEY.md` | Never share these |

**Schedule authority:** [Session_Calendar_100.md](../Session_Calendar_100.md).

---

## Three places (do not merge them)

The module markdown is the **script**. Live class still happens on the board and in the batch repo.

| Place | What it is | After class |
|-------|------------|-------------|
| **Material** `PFS_MATERIAL_KASI` | Curriculum: Try these, one assemble, lab kit, mini-project, Interview Q&A | Commit only when the *curriculum* changes |
| **OpenBoard** | Running notes: diagrams, traps, student questions | Photo / export if you want; not a second syllabus |
| **Batch workspace** e.g. `WORKSPACE/KSR-YK-PFS-MAY2026` | Running **code copy** — type Try these and the assemble here (`input()`, names, comments, false starts) | **Commit here after every class** |

Students type along with you in **their** repos. You commit the trainer running copy in the **batch** workspace, not into `PYTHON/` notes.

Do **not** paste that day’s `.py` files back into the module. Do **not** turn the module into a class diary. OpenBoard + batch repo keep the live feeling; the notes stay reusable for the next batch.

---

## How to share (recommended)

1. Teach from the module markdown.  
2. Build PDFs when needed: `./scripts/build.sh python` → `PDF/PYTHON/`; Git days `./scripts/build.sh git` → `PDF/GIT/`. Commit and push those PDFs with the notes.  
3. After the module (or that day’s Focus) is done, share **only that module’s PDF** from GitHub `PDF/` (or Drive/LMS/WhatsApp).  
4. Homework = **Mini-Project (Assignment)** in the same PDF/notes.

Optional full zip (same notes, still no private folders):

```bash
./scripts/pack_student_share.sh
# → dist/PYTHON_STUDENT/
```

That pack copies teaching files **without** stripping Model answers. It still excludes `14_Trainer_Only/`, `**/solution/`, and `*_KEY.md`.

---

## What stays private

| Keep private | Why |
|--------------|-----|
| `14_Trainer_Only/` | Ops, rubrics, writing standards |
| `16_Assessments/*_KEY.md` | Graded answer keys |
| `15_Lab_Assets/**/solution/` | Full lab solutions |

Practice **Model answer** / Interview Q&A stay in the shared module — students get them with the notes when you share that PDF.

---

## Graded tests

Issue biweekly papers from `16_Assessments/BW##_….md` (no `_KEY`). Mark with the matching `*_KEY.md` on the trainer machine only.

---

## Topic map

See [08_PDF_Python_Enrichment_Map.md](08_PDF_Python_Enrichment_Map.md) if you need the old-topic → current-file list.

---

## Trainer delivery reminder

Each **1h 15m** session: short theory → type-along in the **batch workspace** (OpenBoard for notes) → mini-lab → assign **Mini-Project (Assignment)** → commit the batch repo after class.
