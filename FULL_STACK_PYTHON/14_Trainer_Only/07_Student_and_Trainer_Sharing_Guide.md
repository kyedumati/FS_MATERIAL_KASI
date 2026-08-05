# One Material Policy — Teach and Share the Same Notes

**Rule:** Use **only** `FULL_STACK_PYTHON/` for teaching **and** for student sharing.

Do **not** revive a parallel Python-only pack.  
Teach the **Python program** from `FULL_STACK_PYTHON/` and open shared topics from repo root: `FRONTEND/` (includes React), `MYSQL/`.

---

## What you open every day

| Role | Open this | Do not open for class |
|------|-----------|------------------------|
| **Trainer (live class)** | Same week’s module `.md` in `FULL_STACK_PYTHON/` | Any old Python-only PDF pack |
| **Student (notes + homework)** | Same module file / PDF built from it | Legacy Python PDF set |
| **Trainer (private)** | Plus `14_Trainer_Only/` | Never share answer keys |

**MySQL depth** stays in `MYSQL/` because the Full Stack course already points there via the [Required MySQL labs checklist](../00_Course_Guide/04_Required_MySQL_Labs_Checklist.md). That is one planned dependency, not a second Python curriculum. See also [09_External_Dependencies.md](09_External_Dependencies.md).

**Schedule authority:** [11_Session_Calendar_100.md](../00_Course_Guide/11_Session_Calendar_100.md) — **20 weeks / 100 sessions** (1h 15m each).

---

## How to share with students (pick one)

### Option A — Markdown (recommended if students use GitHub / Cursor / VS Code)

Share a **student pack** (everything except trainer-only):

```bash
# From repo root
./scripts/pack_student_share.sh
```

Output: `dist/FULL_STACK_PYTHON_STUDENT/` — upload to Drive/LMS or push to a student repo.  
The pack already includes nested `FRONTEND/` (with React) and `MYSQL/` beside `FULL_STACK_PYTHON/`.

### Option B — PDFs from the **same** markdown (same content as you teach)

```bash
# From repo root
./scripts/build.sh fullstack
```

PDFs appear under `PDF/FULL_STACK_PYTHON/` mirroring the folder structure.  
Share **those** PDFs — not any old Python-only PDF folder.

### Week-by-week habit (less overload)

1. Teach from this week’s module file.  
2. Share **only that week’s** file or PDF + assignment.  
3. Keep the full pack available as view-only reference on Drive/LMS.

---

## What students should do in every module

- Read outcomes + beginner explanation.  
- Type the code.  
- Basic → Intermediate → Interview exercises.  
- Mini-project with [standard deliverables](../00_Course_Guide/05_Standard_Project_Deliverables.md).  
- GitHub push.  

## What trainers use beyond the shared pack

- **Session Calendar** + module **Classroom Ticket** / lab kit for live class.
- Optional blank: [Daily Lesson Plan Template](04_Daily_Lesson_Plan_Template.md).
- **Student pack / Full Stack PDFs:** assessment answer lines removed automatically.
- This folder (`14_Trainer_Only/`) only on your machine / private Drive.

## What is excluded from the student pack

Automatically removed or not copied:

- Entire folder `14_Trainer_Only/` (sharing guide, lesson plan, writing standard, master guide, keys, …)
- Lab `**/solution/` folders under `15_Lab_Assets/`
- Practice assessment `**Answer:**` / `**Model answer:**` lines (and inline answer keys)
- Trainer-only phrasing cleaned by `scripts/strip_trainer_sections.py`

Rebuild after edits (repo root): `./scripts/pack_student_share.sh`

## Graded tests

Module assessments in the **trainer** tree may keep answers for prep. The **student pack strips those answers**. For scored tests, use [Trainer answer-key index](01_Sample_Answer_Keys_Index.md) / [Assessment Answer Policy](03_Assessment_Answer_Policy.md) and issue a fresh sheet without answers.

---

## Legacy Python pack (removed)

`PDF/PYTHON/` and `PYTHON/` were deleted from this repo. Topic map: [08_PDF_Python_Enrichment_Map.md](08_PDF_Python_Enrichment_Map.md).

---

## Trainer delivery reminder

Notes are a reference, not a script. Each **1h 15m** session: short theory → type-along demo → mini-lab → homework assign → one Git commit expectation.
