# PFS Training Material

Structured training material for **Python Full Stack** and shared **MySQL / Frontend** topics.

---

## Python Full Stack Development (primary program — **one material**)

**Audience:** Fresh graduates, non-IT career switchers, and learners targeting entry-level Python / Django / full-stack roles in India.

**Teach:** [`FULL_STACK_PYTHON/`](FULL_STACK_PYTHON/) + shared [`FRONTEND/`](FRONTEND/) (HTML/CSS/JS + React) · [`MYSQL/`](MYSQL/).  
Legacy `PDF/PYTHON/` / `PYTHON/` were **removed**.

| Resource | Link |
|----------|------|
| Syllabus map | [COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md](COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md) |
| Course folder | [FULL_STACK_PYTHON/](FULL_STACK_PYTHON/) |
| Session calendar | [FULL_STACK_PYTHON/00_Course_Guide/11_Session_Calendar_100.md](FULL_STACK_PYTHON/00_Course_Guide/11_Session_Calendar_100.md) |
| Slim course guide | [FULL_STACK_PYTHON/00_Course_Guide/](FULL_STACK_PYTHON/00_Course_Guide/) |
| Trainer ops / sharing | [FULL_STACK_PYTHON/14_Trainer_Only/](FULL_STACK_PYTHON/14_Trainer_Only/) |
| Student pack | `./scripts/pack_student_share.sh` → `dist/FULL_STACK_PYTHON_STUDENT/` |
| Student PDFs | `./scripts/build.sh fullstack` → `PDF/FULL_STACK_PYTHON/` |

**Default schedule:** 20 weeks × **1 hour 15 minutes/day** live (100 sessions) · Stack: Python 3, MySQL 8+, Django 5.x, HTML/CSS/JS, React, Flask overview, GitHub, VS Code.

**Phases:** Foundations → Core Python → Advanced Python → Git → MySQL → Frontend → Django → Flask/REST → React → Testing/AI lite → Placement.

---

## MySQL Course (MySQL 8+)

**Audience:** Beginners with no database background and career switchers preparing for analyst, backend, or full-stack roles.

**Prerequisites:** Basic computer literacy. No prior SQL experience required.

**Setup:** Start with [MySQL Setup and Connection](MYSQL/00_MySQL_Setup_and_Connection.md) — install MySQL, connect via CLI or Workbench, and create the `training_db` database.

### Recommended Teaching Order

| Order | File | Topic | Focus |
|-------|------|-------|-------|
| 1 | [00_MySQL_Setup_and_Connection](MYSQL/00_MySQL_Setup_and_Connection.md) | Install & connect | Fresher — get MySQL running |
| 2 | [01_Introduction_to_Databases](MYSQL/01_Introduction_to_Databases.md) | DB fundamentals | Tables, rows, DBMS vs RDBMS |
| 3 | [02_Introduction_to_SQL_Basic_Concepts](MYSQL/02_Introduction_to_SQL_Basic_Concepts.md) | SQL basics | DDL, DML, DQL, constraints, CRUD |
| 4 | [03_Querying_with_SQL](MYSQL/03_Querying_with_SQL.md) | Querying | WHERE, LIKE, NULL, ORDER BY, LIMIT |
| 5 | [04_Aggregations_and_Group_By](MYSQL/04_Aggregations_and_Group_By.md) | Aggregations | COUNT, SUM, GROUP BY, HAVING |
| 6 | [05_Common_Concepts](MYSQL/05_Common_Concepts.md) | Functions & sets | CONCAT, DATE_FORMAT, ROUND, UNION |
| 7 | [06_Modeling_Databases](MYSQL/06_Modeling_Databases.md) | Data modeling | ER model, PK/FK, junction tables |
| 8 | [07_Joins](MYSQL/07_Joins.md) | Joins | INNER, LEFT, RIGHT, FULL, self-join |
| 9 | [08_Views_and_Subqueries](MYSQL/08_Views_and_Subqueries.md) | Views & subqueries | EXISTS, correlated subqueries |
| 10 | [09_Transactions_and_Indexes](MYSQL/09_Transactions_and_Indexes.md) | Transactions & indexes | ACID, GRANT/REVOKE, CREATE INDEX |
| 11 | [11_Window_Functions_and_CTEs](MYSQL/11_Window_Functions_and_CTEs.md) | Window functions & CTEs | ROW_NUMBER, RANK, recursive CTE |
| 12 | [12_Real_Time_Projects](MYSQL/12_Real_Time_Projects.md) | Capstone projects | AcmeHR, TechMart, MedCare, SecureBank |

**Homework (use throughout):** [10_Practice_Exercises](MYSQL/10_Practice_Exercises.md) — chapter-wise exercises aligned to each module above.

### Suggested Class Plan (~18 sessions)

| Sessions | Modules | Notes |
|----------|---------|-------|
| 1–2 | 00, 01 | Setup + database concepts |
| 3–4 | 02 | CRUD, constraints, data types |
| 5–6 | 03 | Filtering, sorting, pagination |
| 7–8 | 04, 05 | Aggregations + string/date functions |
| 9–10 | 06 | Schema design and relationships |
| 11–12 | 07 | Joins — spend extra time here |
| 13 | 08 | Subqueries and views |
| 14 | 09 | Transactions, indexes, permissions |
| 15 | 11 | Window functions and CTEs |
| 16–18 | 12 | Real-time project capstone |

---

## How to Use This Material

**For Full Stack trainers (recommended)**
- Teach **only** from `FULL_STACK_PYTHON/` (same files students get).
- Share: `./scripts/pack_student_share.sh` or `./scripts/build.sh fullstack`.
- Keep `14_Trainer_Only/` private.
- SQL depth: Required MySQL labs checklist → `MYSQL/` (planned dependency, not a second Python course).

**For MySQL-only batches**
- Follow numbered order in `MYSQL/`; use `10_Practice_Exercises.md` for homework.

---

## Repository Structure

```
PFS_MATERIAL_KASI/
├── README.md
├── FULL_STACK_PYTHON/        # Python program (calendar, Django, Python labs)
├── FRONTEND/                 # Shared HTML/CSS/JS + REACT/ (+ labs)
├── MYSQL/                    # Shared SQL (FS Weeks 10–11 + MySQL-only)
├── COURSE_CONTENTS/          # Syllabus / brochure maps
├── PDF/                      # Generated PDFs
├── dist/                     # Student batch packs
└── scripts/
```

---

## PDF Workflow (for trainers)

**Source of truth:** edit and commit `.md` files only.  
**For students:** generate PDFs and share the `PDF/` folder.

### One-time setup

1. Install [Google Chrome](https://www.google.com/chrome/) (used for PDF rendering).
2. Install Python dependencies:

```bash
pip3 install -r requirements.txt
```

### Build all PDFs

```bash
chmod +x scripts/build.sh   # first time only
./scripts/build.sh
```

### Build one course

```bash
./scripts/build.sh mysql
./scripts/build.sh fullstack
```

### Rebuild after editing a chapter

The script skips files that are already up to date. To force a rebuild:

```bash
./scripts/build.sh --force
```

Or build a single file:

```bash
python3 scripts/build_pdfs.py --file MYSQL/07_Joins.md
```

### Typical workflow

1. Edit a chapter in `MYSQL/` or `FULL_STACK_PYTHON/`.
2. Commit and push the `.md` change to git.
3. Run `./scripts/build.sh mysql` or `./scripts/build.sh fullstack`.
4. Upload updated PDFs from `PDF/` to Google Drive / LMS / email.

Generated PDFs mirror the source folder structure — e.g. `MYSQL/07_Joins.md` becomes `PDF/MYSQL/07_Joins.pdf`.
