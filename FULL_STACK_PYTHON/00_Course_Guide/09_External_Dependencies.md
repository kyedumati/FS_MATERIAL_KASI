# External Dependencies (Versioned)

`FULL_STACK_PYTHON/` is the **Python program** (calendar, Python/Django/Flask/DRF notes, Python lab kits).  
Shared, non-Python topics live at **repo root** so Java FS can reuse them later.

| Dependency | Path (repo root) | Role | Version / pin |
|------------|------------------|------|----------------|
| **MySQL** | [`MYSQL/`](../../MYSQL/) | Shared SQL depth (FS Weeks 10–11 / S46–55; also MySQL-only batches) | Same git commit as this release |
| **Frontend** | [`FRONTEND/`](../../FRONTEND/) | Shared HTML / CSS / JS (+ `FRONTEND/labs/`) and **React** under [`FRONTEND/REACT/`](../../FRONTEND/REACT/) | Same commit |
| **Syllabus map** | `COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md` | Brochure alignment | Calendar wins on order |
| **Legacy Python notes** | ~~`PDF/PYTHON/`~~ / ~~`PYTHON/`~~ | **Removed** | Do not restore |

## Contract

1. **Schedule** for the Python batch stays in [11_Session_Calendar_100.md](11_Session_Calendar_100.md) — including days that open `FRONTEND/`, `FRONTEND/REACT/`, `MYSQL/`.  
2. **Edit shared topics once** in `MYSQL/` / `FRONTEND/` — do not copy into `FULL_STACK_PYTHON/`.  
3. Student packs must include those siblings (see pack script).  
4. Pointers only: `FULL_STACK_PYTHON/06_Frontend/README.md` and `10_React/README.md`.

## Student distribution

| Option | What to zip |
|--------|-------------|
| A (recommended) | `dist/FULL_STACK_PYTHON_STUDENT/` (nests program + FRONTEND + MYSQL) |
| B (USB offline) | Same + `COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md` |

## Change control

When renaming a shared file, update the Session Calendar module column and any Prev/Next links in the Python program.
