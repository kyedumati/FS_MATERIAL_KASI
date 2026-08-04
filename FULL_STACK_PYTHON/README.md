# Python Full Stack Development — Training Material

> **One material policy for the Python program.** Teach Python/Django from this folder.  
> **Shared topics** (also for Java FS later): [`../FRONTEND/`](../FRONTEND/) (HTML/CSS/JS + [`REACT/`](../FRONTEND/REACT/)), [`../MYSQL/`](../MYSQL/).  
> Pointers only: `06_Frontend/`, `10_React/`. Legacy `PDF/PYTHON/` removed.

**Source syllabus:** KSR Datavizon *FULL STACK PYTHON 2026–27*  
**Audience:** Learners preparing for entry-level Python / Django / full-stack roles
**Default schedule:** **20 weeks × 1 hour 15 minutes/day** (Mon–Fri live) — see Session Calendar  
**Live contact = 125 hours (100 sessions)** + daily homework  
**Stack:** Python 3 · MySQL 8+ · Django 5.x · HTML/CSS/JS · React · Flask (overview) · Git/GitHub · VS Code · Postman  

---

## Start here

1. [**One Material / Sharing Guide**](00_Course_Guide/07_Student_and_Trainer_Sharing_Guide.md) — teach & share the same pack  
2. [**Session Calendar (authority)**](00_Course_Guide/11_Session_Calendar_100.md) — 100 sessions, one focus each  
3. [Master Course Guide](00_Course_Guide/00_Master_Course_Guide.md) — capstone, portfolio, placement, rubrics  
4. [Tested Toolchain](00_Course_Guide/10_Tested_Toolchain.md) · [External Dependencies](00_Course_Guide/09_External_Dependencies.md) · [**Lab Assets**](15_Lab_Assets/) · [**Biweekly Assessments**](16_Assessments/) · [Writing Standard](00_Course_Guide/12_Module_Writing_Standard.md)  
5. [Course Contents (syllabus map)](../COURSE_CONTENTS/Full_Stack_Python_Course_Contents.md)  
6. Printables: progress tracker, capstone one-pager, MySQL checklist, deliverables, a11y checklist  
7. Teach in **Session Calendar order** (module files below support those sessions)  
8. Optional: [Professional Python Deep Dive](03_Advanced_Python/07_Professional_Python_Deep_Dive.md)  
9. Trainers only: [14_Trainer_Only/](14_Trainer_Only/) — **never share with learners**

### Share with students (from **repo root**)

```bash
# cwd must be PFS_MATERIAL_KASI/ (repo root), not FULL_STACK_PYTHON/
./scripts/pack_student_share.sh          # → dist/FULL_STACK_PYTHON_STUDENT/
./scripts/build.sh fullstack             # → PDF/FULL_STACK_PYTHON/
```

Also share is **built into** the student pack: it nests `FRONTEND/` (with React) and `MYSQL/` beside `FULL_STACK_PYTHON/`.

---

## Teaching order

**Schedule authority:** always [`00_Course_Guide/11_Session_Calendar_100.md`](00_Course_Guide/11_Session_Calendar_100.md) (order below matches it).

| Order | Path | Topic |
|------:|------|-------|
| 1 | [01_Foundations/01_Computer_and_Programming_Foundations.md](01_Foundations/01_Computer_and_Programming_Foundations.md) | Computer & programming foundations |
| 2 | [02_Core_Python/01_Python_Setup_and_First_Programs.md](02_Core_Python/01_Python_Setup_and_First_Programs.md) | Python setup & first programs |
| 3 | [02_Core_Python/02_Variables_Datatypes_Operators_IO.md](02_Core_Python/02_Variables_Datatypes_Operators_IO.md) | Variables, types, operators, I/O |
| 4 | [02_Core_Python/03_Flow_Control.md](02_Core_Python/03_Flow_Control.md) | Flow control |
| 5 | [02_Core_Python/04_Strings.md](02_Core_Python/04_Strings.md) | Strings |
| 6 | [02_Core_Python/05_Lists.md](02_Core_Python/05_Lists.md) | Lists |
| 7 | [02_Core_Python/06_Tuples_and_Sets.md](02_Core_Python/06_Tuples_and_Sets.md) | Tuples & sets |
| 8 | [02_Core_Python/07_Dictionaries.md](02_Core_Python/07_Dictionaries.md) | Dictionaries |
| 9 | [02_Core_Python/08_Data_Structures_Overview.md](02_Core_Python/08_Data_Structures_Overview.md) | Data structures overview |
| 10 | [03_Advanced_Python/01_Functions_Decorators_Generators.md](03_Advanced_Python/01_Functions_Decorators_Generators.md) | Functions, decorators, generators |
| 11 | [03_Advanced_Python/02_Modules_and_Packages.md](03_Advanced_Python/02_Modules_and_Packages.md) | Modules & packages |
| 12 | [03_Advanced_Python/03_OOP.md](03_Advanced_Python/03_OOP.md) | OOP |
| 13 | [03_Advanced_Python/04_Exception_Handling.md](03_Advanced_Python/04_Exception_Handling.md) | Exception handling |
| 14 | [03_Advanced_Python/05_File_Handling_and_Logging.md](03_Advanced_Python/05_File_Handling_and_Logging.md) | Files & logging |
| 15 | [04_Git_GitHub/01_Git_and_GitHub.md](04_Git_GitHub/01_Git_and_GitHub.md) | Git & GitHub |
| 16 | [05_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md](05_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md) | MySQL bridge + [Required labs](00_Course_Guide/04_Required_MySQL_Labs_Checklist.md) / [`MYSQL/`](../MYSQL/) |
| 17 | [03_Advanced_Python/06_Database_Programming_Bridge.md](03_Advanced_Python/06_Database_Programming_Bridge.md) | Python ↔ MySQL |
| 15A | [03_Advanced_Python/07_Professional_Python_Deep_Dive.md](03_Advanced_Python/07_Professional_Python_Deep_Dive.md) | Optional enrichment (not on critical path) |
| 18 | [../FRONTEND/01_HTML.md](../FRONTEND/01_HTML.md) | HTML *(shared)* |
| 19 | [../FRONTEND/02_CSS_and_Responsive.md](../FRONTEND/02_CSS_and_Responsive.md) | CSS & responsive *(shared)* |
| 20 | [../FRONTEND/03_JavaScript_DOM_Forms.md](../FRONTEND/03_JavaScript_DOM_Forms.md) | JavaScript, DOM, forms *(shared)* |
| 21 | [07_Django/01_Django_Introduction_and_Setup.md](07_Django/01_Django_Introduction_and_Setup.md) | Django setup |
| 22 | [07_Django/02_URLs_Views_Templates_Static.md](07_Django/02_URLs_Views_Templates_Static.md) | URLs, views, templates, static |
| 23 | [07_Django/03_Models_ORM_Admin.md](07_Django/03_Models_ORM_Admin.md) | Models, ORM, admin |
| 24 | [07_Django/04_Forms_Sessions_Auth.md](07_Django/04_Forms_Sessions_Auth.md) | Forms, sessions, auth |
| 25 | [07_Django/05_Security_and_Deployment.md](07_Django/05_Security_and_Deployment.md) | Security & deployment (`load_dotenv`, `STORAGES`, `check --deploy`) |
| 26 | [07_Django/06_Lab_CRUD_Auth_Consolidation.md](07_Django/06_Lab_CRUD_Auth_Consolidation.md) | **Protected lab:** CRUD + auth |
| 27 | [07_Django/07_Lab_Deploy_Capstone_Debug.md](07_Django/07_Lab_Deploy_Capstone_Debug.md) | **Protected lab:** deploy + debug |
| 28 | [08_Flask/01_Flask_Overview.md](08_Flask/01_Flask_Overview.md) | Flask overview |
| 29 | [09_APIs_REST/01_APIs_JSON_Postman_DRF.md](09_APIs_REST/01_APIs_JSON_Postman_DRF.md) | APIs, JSON, Postman, DRF (**full CRUD code in-module**) |
| 30 | [../FRONTEND/REACT/01_React_Fundamentals.md](../FRONTEND/REACT/01_React_Fundamentals.md) | React fundamentals *(shared)* |
| 31 | [../FRONTEND/REACT/02_React_Hooks_Routing_API_Deploy.md](../FRONTEND/REACT/02_React_Hooks_Routing_API_Deploy.md) | Hooks, routing, API, deploy *(shared)* |
| 32 | [11_Testing_Clean_Code/01_Testing_Debugging_Clean_Code.md](11_Testing_Clean_Code/01_Testing_Debugging_Clean_Code.md) | Testing, debugging, clean code |
| 33 | [13_Placement/01_Career_Resume_Interview.md](13_Placement/01_Career_Resume_Interview.md) | Resume, interview, placement |
| 34 | [12_AI_Integration/01_AI_Integration_Lite.md](12_AI_Integration/01_AI_Integration_Lite.md) | AI lite — **optional stretch only** |

---

## What each module contains

Every teaching module follows the [Writing Standard](00_Course_Guide/12_Module_Writing_Standard.md):

- Learning outcomes + **Classroom Ticket** (lab kit first)  
- What / Why before syntax  
- Important concepts with **Try these (2 programs)** + runnable code (Core / Advanced Python; expanding elsewhere)  
- Step-by-step annotated code  
- Common mistakes + Practice exercises  
- **Mini-project** with lab kit, Stretch, and **Done when** (when present)  
- **Revision Map** (Memorize / Understand / Practise / Build)  
- Interview & Discussion Q&A  
- Graded checks: [`16_Assessments/`](16_Assessments/) (biweekly) — not an Assessment block in every module  

**SQL depth** lives in repo **`MYSQL/`** (required checklist) — not duplicated here.

> Mermaid diagrams render on GitHub, many Markdown previewers, and Cursor. In plain text viewers you still see the diagram source as a readable sketch.

---

## Sequence improvements vs brochure

| Brochure order | Improved order (this material) | Why |
|----------------|--------------------------------|-----|
| Django before frontend | HTML/CSS/JS **before** Django | Templates and forms make sense after markup/JS |
| Git not explicit | Git early (Week 7, then continuous) | Portfolio habit for hiring |
| React after Django | Kept after Django + APIs | Learners need a backend API to integrate |
| AI Integration last | **Stretch after** deployed MVP | Never delays core competence / placement |
| Thin Django calendar | 5 teach modules + **2 lab days** (`06`–`07`) | Career-switcher consolidation time |

Brochure modules **preserved:** Core Python, Advanced Python (incl. decorators/generators, logging, DB programming), MySQL DDL/DML/DQL/TCL/JOINS, Django full path, Flask, Frontend, React, AI Integration, Agile/resume/live project.
