# One Material Policy — Teach and Share the Same Notes

**Rule:** One version of module notes. Teach from `FULL_STACK_PYTHON/` (and shared `FRONTEND/`, `MYSQL/`). Share **that same** content with students — usually the **module PDF after that module is taught**.

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

## How to share (recommended)

1. Teach from the module markdown.  
2. Build PDFs when needed: `./scripts/build.sh fullstack` → `PDF/FULL_STACK_PYTHON/`.  
3. After the module (or that day’s Focus) is done, share **only that module’s PDF** on Drive/LMS/WhatsApp.  
4. Homework = **Mini-Project (Assignment)** in the same PDF/notes.

Optional full zip (same notes, still no private folders):

```bash
./scripts/pack_student_share.sh
# → dist/FULL_STACK_PYTHON_STUDENT/
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

## Legacy

`PDF/PYTHON/` was removed. Topic map: [08_PDF_Python_Enrichment_Map.md](08_PDF_Python_Enrichment_Map.md).

---

## Trainer delivery reminder

Each **1h 15m** session: short theory → type-along demo → mini-lab → assign **Mini-Project (Assignment)** → one Git commit expectation.
