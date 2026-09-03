# Java Full Stack Development — Training Material

> **One material policy for the Java program.** Java / Spring Boot notes live in this folder.  
> **Shared topics** (same files as Python FS): [`../FRONTEND/`](../FRONTEND/) (HTML/CSS/JS + [`REACT/`](../FRONTEND/REACT/)), [`../MYSQL/`](../MYSQL/).  
> Pointers only: `08_Frontend/`, `11_React/`. JPA/REST home is `09_Spring_Boot/` — `10_JPA_and_REST/` is a pointer, not a second copy.

**Source syllabus:** KSR Datavizon *Java Full Stack Development*  
**Audience:** Learners preparing for entry-level Java / Spring Boot / full-stack roles  
**Default schedule:** **20 weeks × 1 hour 15 minutes/day** (Mon–Fri live) — see Session Calendar  
**Live contact = 125 hours (100 sessions)** + daily homework  
**Stack:** JDK 17 · Maven 3.9+ · MySQL 8+ · Spring Boot 3.x (Jakarta) · HTML/CSS/JS · React · Git/GitHub · VS Code or IntelliJ Community · Postman · JUnit 5  

---

## Start here

1. [**Session Calendar**](Session_Calendar_100.md) — 100 sessions, one focus each  
2. [**Tested Toolchain**](Tested_Toolchain.md) · [**Project deliverables**](Standard_Project_Deliverables.md) · [**Capstone one-pager**](Capstone_CampusCart_One_Pager.md)  
3. [**Lab Assets**](15_Lab_Assets/) · [**Biweekly Assessments**](16_Assessments/)  
4. [Course Contents (syllabus map)](../COURSE_CONTENTS/Full_Stack_Java_Course_Contents.md)  
5. Open the **same** module files in Session Calendar order  
6. Optional: [AI Integration Lite](12_AI_Integration/01_AI_Integration_Lite.md) — stretch after a deployed MVP only  

### Typical class shape (75 min)

| Minutes | Block |
|--------:|-------|
| 5 | Open lab kit |
| 25 | Concept demo / notes |
| 35 | Lab |
| 10 | Exit + homework |

---

## Teaching order

**Schedule authority:** always [`Session_Calendar_100.md`](Session_Calendar_100.md) (order below matches it).

| Order | Path | Topic |
|------:|------|-------|
| 1 | [01_Foundations/01_Computer_and_Programming_Foundations.md](01_Foundations/01_Computer_and_Programming_Foundations.md) | Computer & programming foundations |
| 2 | [02_Core_Java/01_Java_Setup_and_First_Programs.md](02_Core_Java/01_Java_Setup_and_First_Programs.md) | JDK setup & first programs |
| 3 | [02_Core_Java/02_Variables_Datatypes_Operators_IO.md](02_Core_Java/02_Variables_Datatypes_Operators_IO.md) | Variables, types, operators, I/O |
| 4 | [02_Core_Java/03_Flow_Control.md](02_Core_Java/03_Flow_Control.md) | Flow control |
| 5 | [02_Core_Java/04_Strings.md](02_Core_Java/04_Strings.md) | Strings |
| 6 | [02_Core_Java/05_Arrays.md](02_Core_Java/05_Arrays.md) | Arrays |
| 7 | [02_Core_Java/06_Methods.md](02_Core_Java/06_Methods.md) | Static methods & overloading |
| 8 | [03_OOP_Java/03_OOP.md](03_OOP_Java/03_OOP.md) | OOP (index) → [Part 1](03_OOP_Java/03_OOP_Part1_Classes_Encapsulation.md) · [Part 2](03_OOP_Java/03_OOP_Part2_Inheritance.md) · [Part 3](03_OOP_Java/03_OOP_Part3_Polymorphism_Interfaces.md) |
| 9 | [04_Collections_Exceptions_IO/01_Collections.md](04_Collections_Exceptions_IO/01_Collections.md) | Collections (`List` / `Set` / `Map`) |
| 10 | [04_Collections_Exceptions_IO/02_Exception_Handling.md](04_Collections_Exceptions_IO/02_Exception_Handling.md) | Exception handling |
| 11 | [04_Collections_Exceptions_IO/03_File_Handling.md](04_Collections_Exceptions_IO/03_File_Handling.md) | Files & I/O |
| 12 | [05_Git_GitHub/01_Git_and_GitHub.md](05_Git_GitHub/01_Git_and_GitHub.md) | Git & GitHub (Java `.gitignore`, Maven) |
| 13 | [06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md](06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md) | MySQL bridge + required labs in-module / [`MYSQL/`](../MYSQL/) |
| 14 | [07_JDBC/01_JDBC_CRUD.md](07_JDBC/01_JDBC_CRUD.md) | JDBC CRUD (`PreparedStatement`) |
| 15 | [../FRONTEND/01_HTML.md](../FRONTEND/01_HTML.md) | HTML *(shared)* |
| 16 | [../FRONTEND/02_CSS_and_Responsive.md](../FRONTEND/02_CSS_and_Responsive.md) | CSS & responsive *(shared)* |
| 17 | [../FRONTEND/03_JavaScript_DOM_Forms.md](../FRONTEND/03_JavaScript_DOM_Forms.md) | JavaScript, DOM, forms *(shared)* |
| 18 | [09_Spring_Boot/01_Maven_and_Spring_Boot_Setup.md](09_Spring_Boot/01_Maven_and_Spring_Boot_Setup.md) | Maven + Spring Boot setup |
| 19 | [09_Spring_Boot/02_Spring_Web_REST.md](09_Spring_Boot/02_Spring_Web_REST.md) | Spring Web REST (Thymeleaf overview only) |
| 20 | [09_Spring_Boot/03_Spring_Data_JPA_Validation.md](09_Spring_Boot/03_Spring_Data_JPA_Validation.md) | Spring Data JPA + validation |
| 21 | [09_Spring_Boot/04_REST_DTOs_Postman.md](09_Spring_Boot/04_REST_DTOs_Postman.md) | REST, DTOs, Postman |
| 22 | [09_Spring_Boot/05_Spring_Security_Lite.md](09_Spring_Boot/05_Spring_Security_Lite.md) | Spring Security lite (JWT) |
| 23 | [09_Spring_Boot/06_Lab_CRUD_Auth_Consolidation.md](09_Spring_Boot/06_Lab_CRUD_Auth_Consolidation.md) | **Protected lab:** CRUD + auth |
| 24 | [09_Spring_Boot/07_Lab_Deploy_Capstone_Debug.md](09_Spring_Boot/07_Lab_Deploy_Capstone_Debug.md) | **Protected lab:** deploy + debug |
| 25 | [09_Spring_Boot/08_Servlet_vs_Spring_Interview_Map.md](09_Spring_Boot/08_Servlet_vs_Spring_Interview_Map.md) | Servlet vs Spring (interview map only) |
| 26 | [../FRONTEND/REACT/01_React_Fundamentals.md](../FRONTEND/REACT/01_React_Fundamentals.md) | React fundamentals *(shared)* |
| 27 | [../FRONTEND/REACT/02_React_Hooks_Routing_API_Deploy.md](../FRONTEND/REACT/02_React_Hooks_Routing_API_Deploy.md) | Hooks, routing, API, deploy *(shared)* |
| 28 | [12_Testing_Clean_Code/01_Testing_Debugging_Clean_Code.md](12_Testing_Clean_Code/01_Testing_Debugging_Clean_Code.md) | Testing, debugging, clean code |
| 29 | [13_Placement/01_Career_Resume_Interview.md](13_Placement/01_Career_Resume_Interview.md) | Resume, interview, placement |
| 30 | [12_AI_Integration/01_AI_Integration_Lite.md](12_AI_Integration/01_AI_Integration_Lite.md) | AI lite — **optional stretch only** |

**Pointer (not a second syllabus):** [10_JPA_and_REST/](10_JPA_and_REST/README.md) → teach JPA/REST from `09_Spring_Boot/` `03`–`04`.

**Authored so far:** Foundations + Core Java (`01`–`06`) + OOP Parts 1–3 + [Collections](04_Collections_Exceptions_IO/01_Collections.md) + [Exception Handling](04_Collections_Exceptions_IO/02_Exception_Handling.md) + [File Handling](04_Collections_Exceptions_IO/03_File_Handling.md) + [Git and GitHub](05_Git_GitHub/01_Git_and_GitHub.md) + [MySQL for Full Stack Developers](06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md) (bridge; SQL depth in [`MYSQL/`](../MYSQL/)) + [JDBC CRUD](07_JDBC/01_JDBC_CRUD.md) (`PreparedStatement`) + [Maven and Spring Boot Setup](09_Spring_Boot/01_Maven_and_Spring_Boot_Setup.md) + [Spring Web REST](09_Spring_Boot/02_Spring_Web_REST.md) + [Spring Data JPA and Validation](09_Spring_Boot/03_Spring_Data_JPA_Validation.md) + [REST, DTOs, and Postman](09_Spring_Boot/04_REST_DTOs_Postman.md) + [Spring Security Lite](09_Spring_Boot/05_Spring_Security_Lite.md) with lab kits 01–19 (kit 19: JWT register/login + protect POST; Lab 06 freeze 400/404 + demo bundle; Lab 07 Actuator health + env / PaaS / M0) and [BW01](16_Assessments/BW01_Weeks_01_02_Foundations_Setup.md) / [BW02](16_Assessments/BW02_Weeks_03_04_Flow_Strings_Arrays.md) / [BW03](16_Assessments/BW03_Weeks_05_06_Methods_OOP_Part1.md) / [BW04](16_Assessments/BW04_Weeks_07_08_OOP_Collections.md) / [BW05](16_Assessments/BW05_Weeks_09_10_Exceptions_Files_Git_MySQL.md) / [BW06](16_Assessments/BW06_Weeks_11_12_SQL_JDBC_HTML.md). Shared FRONTEND HTML/CSS/JS is already used. Protected labs [`06_Lab_CRUD_Auth_Consolidation.md`](09_Spring_Boot/06_Lab_CRUD_Auth_Consolidation.md) and [`07_Lab_Deploy_Capstone_Debug.md`](09_Spring_Boot/07_Lab_Deploy_Capstone_Debug.md) (kit 19) and [`08_Servlet_vs_Spring_Interview_Map.md`](09_Spring_Boot/08_Servlet_vs_Spring_Interview_Map.md) (kit 19 point-only; five comparison bullets) are authored. Later rows (CORS recap via `04`, React onward) are still planned file names until those phases are written.

---

## What each module contains

Every teaching module follows the same shape:

- **Module Outcome** (3–5 can-do bullets) right after the header
- **Definition** / **Purpose** before syntax
- Important concepts with **Try these (2 programs)** + runnable Java (JDK 17); MySQL bridge Try these are SQL (depth in `MYSQL/`)  
- Step-by-step annotated code  
- Practice exercises  
- **Mini-Project (Assignment)** — take-home homework with lab kit, Stretch, and **Done when** (when present)  
- Interview Q&A  
- Graded checks: [`16_Assessments/`](16_Assessments/) (biweekly) — not an Assessment block in every module  

**SQL depth** lives in repo **`MYSQL/`** (required labs listed in the MySQL bridge module) — not duplicated here.

> Mermaid diagrams render on GitHub, many Markdown previewers, and Cursor. PDF builds pre-render them to SVG (`./scripts/build.sh java` needs Node/`npx` + Chrome). In plain text viewers you still see the diagram source as a readable sketch.

---

## Sequence improvements vs brochure

| Brochure order | Improved order (this material) | Why |
|----------------|--------------------------------|-----|
| Spring views before frontend | HTML/CSS/JS **before** Spring | Markup/JS before JSON or Thymeleaf overview |
| Git not explicit | Git early (Week 9, then continuous) | Portfolio habit for hiring |
| JPA without JDBC | **JDBC first**, then JPA | Learners see SQL before the ORM |
| Servlets/JSP as backbone | One **interview map** session only | Job market is Spring Boot + REST |
| React after “some backend” | After Spring REST + labs | SPA needs a real Java API |
| AI Integration last | **Stretch after** deployed MVP | Never delays core competence / placement |
| Thin Spring calendar | 5 teach modules + **2 lab days** (`06`–`07`) | Career-switcher consolidation time |

Brochure modules **preserved:** Core Java, OOP, Collections, Exceptions, JDBC, JPA, Spring Boot, REST, Security overview, Frontend, React, Git, MySQL, testing, Agile/resume/live project.

---

## Maintainers

PDFs / optional share mirror (from **repo root**):

```bash
./scripts/build.sh java                 # → PDF/JAVA/  (same notes as class)
./scripts/pack_student_share.sh java    # optional zip mirror; excludes private folders only
```

Python FS is unchanged: `./scripts/build.sh python` · `./scripts/pack_student_share.sh`.

**Share habit:** send each module PDF after that module is taught.  
Private ops (keys, rubrics): [`14_Trainer_Only/`](14_Trainer_Only/).
