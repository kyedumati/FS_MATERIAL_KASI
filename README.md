# PFS Training Material

Structured training material for **Python Full Stack**, **Java Full Stack**, and shared **MySQL / Frontend** topics.

---

## Python Full Stack Development (**one material**)

**Audience:** Fresh graduates, non-IT career switchers, and learners targeting entry-level Python / Django / full-stack roles in India.

**Teach:** [`PYTHON/`](PYTHON/) + shared [`FRONTEND/`](FRONTEND/) (HTML/CSS/JS + React) · [`MYSQL/`](MYSQL/).

| Resource | Link |
|----------|------|
| Syllabus map | [COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md](COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md) |
| Course folder | [PYTHON/](PYTHON/) |
| Session calendar | [PYTHON/Session_Calendar_100.md](PYTHON/Session_Calendar_100.md) |
| Toolchain / deliverables / capstone | [Tested_Toolchain.md](PYTHON/Tested_Toolchain.md) · [Standard_Project_Deliverables.md](PYTHON/Standard_Project_Deliverables.md) · [Capstone_CampusCart_One_Pager.md](PYTHON/Capstone_CampusCart_One_Pager.md) |
| Trainer ops (private) | [PYTHON/14_Trainer_Only/](PYTHON/14_Trainer_Only/) |
| Student pack | `./scripts/pack_student_share.sh` → `dist/PYTHON_STUDENT/` |
| Student PDFs | `./scripts/build.sh python` → `PDF/PYTHON/` · `./scripts/build.sh frontend` → `PDF/FRONTEND/` |

**Default schedule:** 20 weeks × **1 hour 15 minutes/day** live (100 sessions) · Stack: Python 3, MySQL 8+, Django 5.x, HTML/CSS/JS, React, Flask overview, GitHub, VS Code.

**Phases:** Foundations → Core Python → Advanced Python → Git → MySQL → Frontend → Django → Flask/REST → React → Testing/AI lite → Placement.

---

## Java Full Stack Development (**one material**)

**Audience:** Learners targeting entry-level Java / Spring Boot / full-stack roles in India (one unified learner voice).

**Teach:** [`JAVA/`](JAVA/) + the **same** shared [`FRONTEND/`](FRONTEND/) and [`MYSQL/`](MYSQL/) — do not copy those topics into the Java folder.

| Resource | Link |
|----------|------|
| Syllabus map | [COURSE_CONTENTS/Full_Stack_Java_Course_Contents.md](COURSE_CONTENTS/Full_Stack_Java_Course_Contents.md) |
| Course folder | [JAVA/](JAVA/) |
| Session calendar | [JAVA/Session_Calendar_100.md](JAVA/Session_Calendar_100.md) |
| Toolchain / deliverables / capstone | [Tested_Toolchain.md](JAVA/Tested_Toolchain.md) · [Standard_Project_Deliverables.md](JAVA/Standard_Project_Deliverables.md) · [Capstone_CampusCart_One_Pager.md](JAVA/Capstone_CampusCart_One_Pager.md) |
| Trainer ops (private) | [JAVA/14_Trainer_Only/](JAVA/14_Trainer_Only/) |
| Student pack | `./scripts/pack_student_share.sh java` → `dist/JAVA_STUDENT/` |
| Student PDFs | `./scripts/build.sh java` → `PDF/JAVA/` · `./scripts/build.sh frontend` → `PDF/FRONTEND/` |

**Default schedule:** 20 weeks × **1 hour 15 minutes/day** live (100 sessions) · Stack: JDK 17, Maven 3.9+, MySQL 8+, Spring Boot 3.x (Jakarta), HTML/CSS/JS, React, GitHub, VS Code or IntelliJ Community, Postman, JUnit 5.

**Phases:** Foundations → Core Java → OOP → Collections/Exceptions/IO → Git → MySQL → JDBC → Frontend → Spring Boot (REST + JPA + labs) → React → Testing → Placement. AI lite is optional stretch after a deployed MVP.

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

**Python Full Stack path**
- Start at [`PYTHON/`](PYTHON/) → [Session Calendar](PYTHON/Session_Calendar_100.md).
- Open the linked modules and lab kits in calendar order (same files for class and homework).
- Shared topics: [`FRONTEND/`](FRONTEND/) (HTML/CSS/JS + React) · [`MYSQL/`](MYSQL/) (labs listed from the MySQL bridge module).

**Java Full Stack path**
- Start at [`JAVA/`](JAVA/) → [Session Calendar](JAVA/Session_Calendar_100.md).
- Same shared `FRONTEND/` and `MYSQL/` files (pointers only inside the Java folder).
- JDBC then JPA; REST-first Spring Boot; Servlets/JSP are one interview-map session only.

**MySQL-only path**
- Follow numbered order in `MYSQL/`; use `10_Practice_Exercises.md` for homework.

**Maintainers (pack / PDF)**
- Student pack: `./scripts/pack_student_share.sh` (Python) or `./scripts/pack_student_share.sh java`.
- PDFs: `./scripts/build.sh python` or `./scripts/build.sh java` (also `frontend`, `mysql`).
- Private ops: `14_Trainer_Only/` inside each program folder — never share. Share each module PDF after teaching (one material).

---

## Repository Structure

```
PFS_MATERIAL_KASI/
├── README.md
├── PYTHON/                   # Python program (calendar, Django, Python labs)
├── JAVA/                     # Java program (calendar, Spring Boot, Java labs)
├── FRONTEND/                 # Shared HTML/CSS/JS + REACT/ (+ labs)
├── MYSQL/                    # Shared SQL (FS Weeks 10–11 + MySQL-only)
├── COURSE_CONTENTS/          # Syllabus / brochure maps
├── PDF/                      # Generated PDFs
├── dist/                     # Student batch packs
└── scripts/
```

---

## PDF Workflow

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
./scripts/build.sh python
./scripts/build.sh java
./scripts/build.sh frontend
```

(`fullstack` is an alias for `python`; `fullstack-java` is an alias for `java`.)

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

1. Edit a chapter in `MYSQL/`, `PYTHON/`, `JAVA/`, or `FRONTEND/`.
2. Commit and push the `.md` change to git.
3. Run `./scripts/build.sh mysql`, `./scripts/build.sh python`, `./scripts/build.sh java`, or `./scripts/build.sh frontend`.
4. Upload updated PDFs from `PDF/` to Google Drive / LMS / email.

Generated PDFs mirror the source folder structure — e.g. `MYSQL/07_Joins.md` becomes `PDF/MYSQL/07_Joins.pdf`.
