# Full Stack Training Material

Structured training material for **Python Full Stack**, **Java Full Stack**, and shared **Git / MySQL / Frontend** topics.

---

## Python Full Stack Development (**one material**)

**Audience:** Fresh graduates, non-IT career switchers, and learners targeting entry-level Python / Django / full-stack roles in India.

**Teach:** [`PYTHON/`](PYTHON/) + shared [`GIT/`](GIT/) · [`FRONTEND/`](FRONTEND/) (HTML/CSS/JS + React) · [`MYSQL/`](MYSQL/).

| Resource | Link |
|----------|------|
| Syllabus map | [PYTHON/Course_Contents.md](PYTHON/Course_Contents.md) |
| Course folder | [PYTHON/](PYTHON/) |
| Session calendar | [PYTHON/Session_Calendar_100.md](PYTHON/Session_Calendar_100.md) |
| Toolchain / deliverables / capstone | [Tested_Toolchain.md](PYTHON/Tested_Toolchain.md) · [Standard_Project_Deliverables.md](PYTHON/Standard_Project_Deliverables.md) · [Capstone_CampusCart_One_Pager.md](PYTHON/Capstone_CampusCart_One_Pager.md) |
| Trainer ops (private) | [PYTHON/14_Trainer_Only/](PYTHON/14_Trainer_Only/) |
| Student pack | `./scripts/pack_student_share.sh` → `dist/PYTHON_STUDENT/` |
| Student PDFs | `./scripts/build.sh python` → `PDF/PYTHON/` · `./scripts/build.sh git` → `PDF/GIT/` · `./scripts/build.sh frontend` → `PDF/FRONTEND/` |

**Default schedule:** 20 weeks × **1 hour 15 minutes/day** live (100 sessions) · Stack: Python 3, MySQL 8+, Django 5.x, HTML/CSS/JS, React, Flask overview, GitHub, VS Code.

**Phases:** Foundations → Core Python → Advanced Python → Git → MySQL → Frontend → Django → Flask/REST → React → Testing/AI lite → Placement.

---

## Java Full Stack Development (**one material**)

**Audience:** Learners targeting entry-level Java / Spring Boot / full-stack roles in India (one unified learner voice).

**Teach:** [`JAVA/`](JAVA/) + the **same** shared [`GIT/`](GIT/), [`FRONTEND/`](FRONTEND/), and [`MYSQL/`](MYSQL/) — do not copy those topics into the Java folder.

| Resource | Link |
|----------|------|
| Syllabus map | [JAVA/Course_Contents.md](JAVA/Course_Contents.md) |
| Course folder | [JAVA/](JAVA/) |
| Session calendar | [JAVA/Session_Calendar_100.md](JAVA/Session_Calendar_100.md) |
| Toolchain / deliverables / capstone | [Tested_Toolchain.md](JAVA/Tested_Toolchain.md) · [Standard_Project_Deliverables.md](JAVA/Standard_Project_Deliverables.md) · [Capstone_CampusCart_One_Pager.md](JAVA/Capstone_CampusCart_One_Pager.md) |
| Trainer ops (private) | [JAVA/14_Trainer_Only/](JAVA/14_Trainer_Only/) |
| Student pack | `./scripts/pack_student_share.sh java` → `dist/JAVA_STUDENT/` |
| Student PDFs | `./scripts/build.sh java` → `PDF/JAVA/` · `./scripts/build.sh git` → `PDF/GIT/` · `./scripts/build.sh frontend` → `PDF/FRONTEND/` |

**Default schedule:** 20 weeks × **1 hour 15 minutes/day** live (100 sessions) · Stack: JDK 17, Maven 3.9+, MySQL 8+, Spring Boot 3.x (Jakarta), HTML/CSS/JS, React, GitHub, VS Code or IntelliJ Community, Postman, JUnit 5.

**Phases:** Foundations → Core Java → OOP → Collections/Exceptions/IO → Git → MySQL → JDBC → Frontend → Spring Boot (REST + JPA + labs) → React → Testing → Placement. AI lite is optional stretch after a deployed MVP.

---

## MySQL Course (MySQL 8+)

**Audience:** Beginners with no database background and career switchers preparing for analyst, backend, or full-stack roles.

**Start:** [`MYSQL/README.md`](MYSQL/README.md) — two tracks (full stack Weeks 10–11 vs MySQL-only), homework, and the `training_db` seed.  
**Syllabus map:** [`MYSQL/Course_Contents.md`](MYSQL/Course_Contents.md).

**Setup:** [MySQL Setup and Connection](MYSQL/00_MySQL_Setup_and_Connection.md) — install MySQL, connect via CLI or Workbench, create `training_db`.

---

## How to Use This Material

**Python Full Stack path**
- Start at [`PYTHON/`](PYTHON/) → [Session Calendar](PYTHON/Session_Calendar_100.md).
- Open the linked modules and lab kits in calendar order (same files for class and homework).
- Shared topics: [`GIT/`](GIT/) (Git and GitHub) · [`FRONTEND/`](FRONTEND/) (HTML/CSS/JS + React) · [`MYSQL/`](MYSQL/) (labs listed from the MySQL bridge module).

**Java Full Stack path**
- Start at [`JAVA/`](JAVA/) → [Session Calendar](JAVA/Session_Calendar_100.md).
- Same shared `GIT/`, `FRONTEND/`, and `MYSQL/` files (pointers only inside the Java folder).
- JDBC then JPA; REST-first Spring Boot; Servlets/JSP are one interview-map session only.

**MySQL-only path**
- Start at [`MYSQL/README.md`](MYSQL/README.md). Homework: [`MYSQL/homework/10_Practice_Exercises.md`](MYSQL/homework/10_Practice_Exercises.md).

**Maintainers (pack / PDF)**
- Student pack: `./scripts/pack_student_share.sh` (Python) or `./scripts/pack_student_share.sh java`.
- PDFs: `./scripts/build.sh python` or `./scripts/build.sh java` (also `git`, `frontend`, `mysql`).
- Private ops: `14_Trainer_Only/` inside each program folder — never share. Share each module PDF after teaching (one material).

---

## Repository Structure

```
PFS_MATERIAL_KASI/
├── README.md
│
│   Programs
├── PYTHON/                   # Python FS (calendar, Course_Contents.md, Django, labs)
├── JAVA/                     # Java FS (calendar, Course_Contents.md, Spring Boot, labs)
│
│   Shared topics
├── GIT/                      # Git + GitHub notes + labs/ (Python FS + Java FS)
├── FRONTEND/                 # HTML/CSS/JS + REACT/ (+ labs)
├── MYSQL/                    # SQL notes + Course_Contents.md + homework/ + labs/
│
│   Generated
├── PDF/                      # Student PDFs (tracked)
├── dist/                     # Student batch packs (gitignored)
│
│   Tooling
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
./scripts/build.sh git
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

1. Edit a chapter in `GIT/`, `MYSQL/`, `PYTHON/`, `JAVA/`, or `FRONTEND/`.
2. Commit and push the `.md` change to git.
3. Run `./scripts/build.sh git`, `mysql`, `python`, `java`, or `frontend` as needed.
4. Upload updated PDFs from `PDF/` to Google Drive / LMS / email.

Generated PDFs mirror the source folder structure — e.g. `MYSQL/07_Joins.md` becomes `PDF/MYSQL/07_Joins.pdf`.
