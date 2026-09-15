# Java Full Stack Development — Course Guide

**Program:** Java Full Stack Development (KSR Datavizon)  
**Audience:** Learners preparing for entry-level Java / Spring Boot / full-stack roles  
**Stack:** JDK 17 · Maven 3.9+ · MySQL 8+ · Spring Boot 3.x (Jakarta) · HTML/CSS/JS · React · Git/GitHub · VS Code or IntelliJ Community · Postman · JUnit 5  
**Default schedule:** **DURATION = 20 weeks** · **HOURS_PER_DAY = 1 hour 15 minutes** (Mon–Fri live class)  
**Live contact:** 20 × 5 × 1.25h = **125 hours** (100 sessions)  
**Homework:** ~45–90 min most days → total engagement well above brochure **150+ hours**  

> **Schedule authority:** [Session_Calendar_100.md](../Session_Calendar_100.md) — one session, one focus. Do not put Duration on module headers (calendar owns timing).  
> Live class is **1h 15m only**. Do not use old 4-hour agendas.  
> External deps: [09_External_Dependencies.md](09_External_Dependencies.md) · Toolchain: [Tested_Toolchain.md](../Tested_Toolchain.md) · Labs: [../15_Lab_Assets/](../15_Lab_Assets/) · Biweekly tests: [../16_Assessments/](../16_Assessments/)

---

## 1. Complete Curriculum Map

### Learning journey (flowchart)

```
[Computer foundations]
        ↓
[Core Java: types → I/O → flow → strings → arrays → methods]
        ↓
[OOP Parts 1–3 → Collections → Exceptions → Files]
        ↓
[Git + GitHub habit]  ←── continue every week
        ↓
[MySQL: DDL/DML/DQL/TCL/JOINS] → [JDBC PreparedStatement]
        ↓
[HTML → CSS → JavaScript/DOM]
        ↓
[Maven + Spring Boot REST → JPA → DTOs → Security lite]
        ↓
[Protected labs 06–07] → [Servlet vs Spring map]
        ↓
[React + Java API]
        ↓
[Testing + Clean code]
        ↓
[Capstone deploy + Portfolio + Placement]
        ↓
[AI Integration Lite — OPTIONAL stretch only]
```

**Same journey (interactive view):**

```mermaid
flowchart TD
  A[Foundations] --> B[Core Java]
  B --> C[OOP Java]
  C --> D[Collections Exceptions IO]
  D --> E[Git habit]
  E --> F[MySQL + JDBC]
  F --> G[HTML CSS JS]
  G --> H[Spring Boot + labs]
  H --> I[React]
  I --> J[Testing]
  J --> K[Capstone + Placement]
  K -.-> L[AI stretch optional]
```

**Key takeaways:**
- SQL is learned in `MYSQL/`; Java talks to it with JDBC first, then JPA
- HTML/CSS/JS before Spring; React after a real REST API exists
- AI never sits on the critical path to placement

### Module index (detailed notes live under `JAVA/`)

| # | Module folder / file | Phase | Memorize | Understand | Practise | Build |
|---|----------------------|-------|----------|------------|----------|-------|
| 01 | `01_Foundations/01_Computer_and_Programming_Foundations.md` | Foundations | OS, file paths | Client–server | Terminal + IDE | Career roadmap note |
| 02 | `02_Core_Java/01_Java_Setup_and_First_Programs.md` | Core | `javac`, `main` | Compile vs run | Hello apps | Environment checklist |
| 03 | `02_Core_Java/02_Variables_Datatypes_Operators_IO.md` | Core | Types, operators | Casting, `Scanner` | Calculator drills | CLI calculator |
| 04 | `02_Core_Java/03_Flow_Control.md` | Core | if/for/while/switch | Nested logic | Patterns, menus | ATM menu |
| 05 | `02_Core_Java/04_Strings.md` | Core | Methods, `equals` | Immutability | Parsing text | Text utilities |
| 06 | `02_Core_Java/05_Arrays.md` | Core | Index, loops | 1D vs 2D | Marks arrays | Marks Manager |
| 07 | `02_Core_Java/06_Methods.md` | Core | `static`, return | Overloading | Refactor scripts | Methods ATM |
| 08 | `03_OOP_Java/03_OOP.md` (+ Parts 1–3) | OOP | class/object | Inheritance, interfaces | Model entities | BankAccount / wallet |
| 09 | `04_Collections_Exceptions_IO/01_Collections.md` | Core+ | List/Set/Map | When to pick | CRUD collections | Contact map |
| 10 | `04_Collections_Exceptions_IO/02_Exception_Handling.md` | Core+ | try-with-resources | Checked vs unchecked | Robust CLI | Safe input |
| 11 | `04_Collections_Exceptions_IO/03_File_Handling.md` | Core+ | nio / streams | Text vs binary lite | CSV/JSON files | Expense file logger |
| 12 | [`GIT/`](../../GIT/) Sessions 1–5 (3–5 extra lab if only S44–S45) | Tools | First push | Daily loop + PRs | Daily commits | Portfolio repos |
| 13 | `06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md` + [`MYSQL/`](../../MYSQL/) | Data | SQL CRUD, JOIN | Normalization | Workbench labs | Library schema |
| 14 | `07_JDBC/01_JDBC_CRUD.md` | Data | PreparedStatement | Why not concat SQL | Java CRUD | Library JDBC |
| 15 | [`FRONTEND/01_HTML.md`](../../FRONTEND/01_HTML.md) | FE | Tags, forms | Semantic HTML | Pages | Profile page |
| 16 | [`FRONTEND/02_CSS_and_Responsive.md`](../../FRONTEND/02_CSS_and_Responsive.md) | FE | Box model, Flex | Responsive | Layouts | Landing page |
| 17 | [`FRONTEND/03_JavaScript_DOM_Forms.md`](../../FRONTEND/03_JavaScript_DOM_Forms.md) | FE | DOM events | Async fetch | Validation | Form + API call |
| 18 | `09_Spring_Boot/01_Maven_and_Spring_Boot_Setup.md` | BE | Maven, starters | JAR vs war lite | start.spring.io | Hello Boot |
| 19 | `09_Spring_Boot/02_Spring_Web_REST.md` | BE | annotations | Request lifecycle | JSON endpoints | In-memory API |
| 20 | `09_Spring_Boot/03_Spring_Data_JPA_Validation.md` | BE | Entity, repo | ORM vs JDBC | Persist catalog | Product JPA |
| 21 | `09_Spring_Boot/04_REST_DTOs_Postman.md` | BE | DTO, status | Mapping | Postman | Validated API |
| 22 | `09_Spring_Boot/05_Spring_Security_Lite.md` | BE | JWT lite | AuthN vs AuthZ | Protected routes | Login API |
| 23 | `09_Spring_Boot/06_Lab_CRUD_Auth_Consolidation.md` | BE lab | — | End-to-end flow | **Guided lab day** | Working CRUD+auth |
| 24 | `09_Spring_Boot/07_Lab_Deploy_Capstone_Debug.md` | BE lab | env, profiles | Debug prod issues | **Guided lab day** | Live URL |
| 25 | `09_Spring_Boot/08_Servlet_vs_Spring_Interview_Map.md` | BE | Buzzwords | Why Spring won | Oral map | 5-bullet note |
| 26 | [`FRONTEND/REACT/01_React_Fundamentals.md`](../../FRONTEND/REACT/01_React_Fundamentals.md) | FE | Components, hooks | State | SPA basics | UI components |
| 27 | [`FRONTEND/REACT/02_React_Hooks_Routing_API_Deploy.md`](../../FRONTEND/REACT/02_React_Hooks_Routing_API_Deploy.md) | FE | useEffect, Router | CORS | API integrate | React + Spring |
| 28 | `12_Testing_Clean_Code/01_Testing_Debugging_Clean_Code.md` | Quality | JUnit 5 | Debug flow | Write tests | Tested utils |
| 29 | `13_Placement/01_Career_Resume_Interview.md` | Jobs | Role keywords | STAR stories | Mocks | Resume + LinkedIn |
| 30 | `12_AI_Integration/01_AI_Integration_Lite.md` | **Stretch only** | API call pattern | Never blocks jobs | Optional demo | Optional widget |

> **Spring Boot package = seven files:** teaching modules `01`–`05` plus two **protected lab days** `06`–`07`. File `08` is a **one-session** Servlet vs Spring interview map — not a Servlets/JSP backbone. JPA/REST are taught in `03`–`04`; [`10_JPA_and_REST/`](../10_JPA_and_REST/README.md) is a pointer only.

**Label legend for learners**

| Label | Meaning |
|-------|---------|
| **Memorize** | Syntax / commands you should recall in interviews without notes |
| **Understand** | Concepts you must explain in simple English |
| **Practise** | Lab drills every day |
| **Build** | Portfolio artefacts |

---

## 2. Week-by-Week Training Plan

**Schedule authority:** [Session_Calendar_100.md](../Session_Calendar_100.md) (Sessions **01–100**).  
**Assumptions:** **20 weeks** × **1h 15m/day** × 5 days = **6.25 live hours/week** (**125 live hours**).

### Daily timebox (every live class — **75 minutes**)

**Authority:** same shape as [Session_Calendar_100.md](../Session_Calendar_100.md).

| Minutes | Block | Purpose |
|--------:|-------|---------|
| 5 | Open lab kit | Open `15_Lab_Assets/` `starter/` / `broken/` (from Session Calendar) |
| 25 | Type-along demo | One concept cluster; learners type along |
| 35 | Lab | Finish ticket from [15_Lab_Assets](../15_Lab_Assets/) |
| 10 | Exit + homework | Calendar “Homework” column |

**Total:** **75 minutes.** Never paste an old 4-hour agenda into one class.

### Week themes (summary — details in Session Calendar)

| Week | Sessions | Theme | Milestone |
|------|----------|-------|-----------|
| 1 | 01–05 | Foundations + JDK setup | Hello repo |
| 2 | 06–10 | Variables, operators, I/O | CLI calculator |
| 3 | 11–15 | Flow control | ATM menu |
| 4 | 16–20 | Strings + arrays | Marks Manager |
| 5 | 21–25 | Methods + OOP Part 1 start | Student class |
| 6 | 26–30 | OOP Part 1 finish | BankAccount |
| 7 | 31–35 | Inheritance, abstract, interfaces | Employee hierarchy |
| 8 | 36–40 | Polymorphism + collections | Inventory / contacts |
| 9 | 41–45 | Exceptions, files, Git/GitHub | Public Java repo |
| 10 | 46–50 | MySQL setup → DQL + ER | `training_db` |
| 11 | 51–55 | Joins, TCL, JDBC connect | Parameterized SELECT start |
| 12 | 56–60 | JDBC CRUD + HTML | Library JDBC + profile page |
| 13 | 61–65 | CSS/JS + fetch | Responsive page |
| 14 | 66–70 | Maven, Spring REST, Thymeleaf overview | First JSON API |
| 15 | 71–75 | JPA, DTOs, security lite | Login + catalog persist |
| 16 | 76–80 | Lab 06–07 + capstone shell | Deploy checks + M0/M1 |
| 17 | 81–85 | Servlet map + capstone M1–M3 | Orders stub |
| 18 | 86–90 | React + Spring API | SPA list UI |
| 19 | 91–95 | Testing + capstone build/deploy | Live/staging URL |
| 20 | 96–100 | Placement + defense | Demo day |

**Protected sessions (do not skip):** S52–S53 (JOINs), S56–S57 (`PreparedStatement`), S76–S79 (Spring labs), S93–S100 (capstone/placement).

### If you change DURATION

| Batch type | Weeks | Sessions | Notes |
|------------|------:|---------:|-------|
| **Default** | **20** | **100** | **Use Session Calendar as-is** |
| Comfortable | 22–24 | 110–120 | Extra buffer on Spring/React |
| Compressed | 16 | 80 | Only with Sat labs; drop React depth and AI |

---

## 3. Capstone Project Roadmap

### Project title

**CampusCart** — College E-Commerce & Booking Portal  
CampusCart is the college storefront; it uses the same catalog / cart / order patterns as **Swiggy**. Teaching brands across the course: **Employee Management Portal**, **Swiggy**, **Apollo Hospitals**, **HDFC Bank** — see [12_Named_Product_Domains.md](12_Named_Product_Domains.md).  
*(Alternate titles for batches: Swiggy storefront, MediBook Clinic → **Apollo Hospitals**, HDFC Bank teller portal, TaskFlow Pro, LearnBlog CMS — same architecture.)*

### Problem statement

Students and staff browse products/services, register, place orders or bookings, and admins manage catalog and orders. Built with **Spring Boot 3 + MySQL + REST** (core), optional **React** storefront and a short **Thymeleaf** overview page.

### Features (MVP → stretch)

**MVP (Must)**

- [ ] User registration / login / logout
- [ ] Product or service catalog (list, detail, search)
- [ ] Cart / booking request
- [ ] Place order; order history
- [ ] Admin: manage products and orders
- [ ] Validation on write APIs
- [ ] Deployed demo (Railway / Render / AWS lite)

**Stretch (only after MVP is deployed)**

- [ ] React product listing consuming API
- [ ] Thymeleaf catalog page (if not already used as overview)
- [ ] Email notification stub
- [ ] AI “recommend / summarize” endpoint — **optional enrichment; never blocks placement**

### Database schema (simplified)

```
users ──< orders >── products
            │
       order_items
categories ──< products
```

**Tables / entities**

| Entity | Key fields |
|--------|------------|
| Category | id, name, slug |
| Product | id, category_id, name, price, stock, image, isActive |
| Order | id, user_id, status, total, createdAt |
| OrderItem | id, order_id, product_id, quantity, price |
| Profile *(optional)* | user_id, phone, address |

### UI pages / API

| Surface | Actor | Notes |
|---------|-------|-------|
| REST `/api/products` | Guest, User | List, detail, search |
| REST `/api/auth/*` | Guest | Register, login |
| REST `/api/cart`, `/api/orders` | User | Login required |
| Admin endpoints or staff UI | Staff | Manage catalog |
| React listing *(stretch)* | Guest, User | `fetch` Spring API |

### API endpoints (MVP)

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/products` | List products |
| GET | `/api/products/{id}` | Detail |
| POST | `/api/auth/register` | Register |
| POST | `/api/auth/login` | JWT (or session) |
| GET/POST | `/api/cart` | Cart ops |
| GET/POST | `/api/orders` | Orders |

### GitHub milestones

| Milestone | Week | Done when |
|-----------|------|-----------|
| M0 Repo + README + `.gitignore` + Maven | 14–16 | Empty Spring project pushed |
| M1 Auth shell | 16–17 | Login works |
| M2 JPA catalog | 17 | Products in DB |
| M3 Cart + orders | 17–19 | End-to-end order |
| M4 Deploy + screenshots | 16 / 19 | Live URL in README |
| M5 React (optional) | 18 | Documented in README |
| M6 Defense | 20 | 10-min demo + Q&A |

### Deployment checklist

- [ ] Secrets from env (never in git)
- [ ] `application.yml` profiles for prod
- [ ] Allowed origins / CORS set
- [ ] MySQL or managed DB credentials secured
- [ ] Migrations or `schema.sql` applied
- [ ] HTTPS / platform SSL on
- [ ] README: setup, env vars, demo accounts
- [ ] No passwords committed

---

## 4. Project Portfolio Plan

Teaching brands in labs and notes (soft-apply): **Employee Management Portal**, **Swiggy**, **Apollo Hospitals**, **HDFC Bank**. CampusCart remains the major capstone.

| # | Project | Stack | When | Resume one-liner |
|---|---------|-------|------|------------------|
| 1 | Student Marks Manager | Java CLI (arrays) | Week 4 | “CLI app for student scores using arrays and methods.” |
| 2 | Campus Wallet / BankAccount | Java OOP | Week 6–8 | “Account types with inheritance, interfaces, and encapsulation.” |
| 3 | Library DB + JDBC CRUD | MySQL + JDBC | Week 12 | “Normalized library schema with PreparedStatement CRUD.” |
| 4 | Responsive Portfolio + Form | HTML/CSS/JS | Week 13 | “Personal site with validated contact form.” |
| 5 | Product API (Spring) | Spring Boot + MySQL | Week 14–16 | “REST catalog with JPA, validation, and JWT lite.” |
| 6 | **CampusCart (major)** | Spring Boot + MySQL + REST (+ React) | Weeks 16–20 | “Full-stack e-commerce/booking portal with deploy.” |

**Standard submission bundle (every mini-project & capstone)**  
See [Standard_Project_Deliverables.md](../Standard_Project_Deliverables.md).

Required for grading:

- [ ] Public GitHub repo (no secrets)
- [ ] README (problem, features, setup, screenshots)
- [ ] `pom.xml` and/or `package.json`
- [ ] `.env.example` (never commit `.env`)
- [ ] Sample / seed test data
- [ ] Screenshots (desktop + mobile where UI exists)
- [ ] Short demo video (2–5 min) or Loom link
- [ ] Meaningful commits; issues/milestones for major project

---

## 5. Placement-Readiness Plan (Weeks 18–20)

### Week 18 (start soft skills while React runs)

- Resume v1 (projects + skills aligned to JD keywords)
- LinkedIn: photo, headline (“Java Full Stack Developer | Spring Boot | MySQL”), About, Featured repos
- Aptitude: 30 min/day (quant lite + logical)
- Coding: 2 easy problems/day (arrays/strings)

### Week 19

- Resume v2 after mentor review
- 2 technical mock interviews (Java + SQL)
- 1 HR mock (background / motivation story)
- Postman collection + GitHub pinned repos
- Capstone feature freeze + a11y pass

### Week 20

- Capstone demo day
- Company JD mapping worksheet (Java Developer / Spring Boot / Full Stack)
- Final mocks + feedback
- Application tracker spreadsheet
- Negotiation & joining basics (entry-level joining context)

### Target roles (entry-level India)

- Java Developer  
- Spring Boot Developer  
- Backend Developer (Java)  
- Full Stack Developer (Java)  
- Web Developer  

### Interview topic weights (suggested)

| Area | Weight |
|------|--------|
| Core Java + OOP | 25% |
| SQL + joins | 20% |
| Spring Boot / JPA / REST / security lite | 25% |
| HTML/CSS/JS + HTTP/JSON | 15% |
| Git + projects storytelling | 10% |
| Aptitude / HR | 5% |

---

## 6. Learner Progress Tracker

Copy one row set per student.

| Week | Attendance | Lab % | Assignment | GitHub push | Quiz score | Confidence (1–5) | Notes |
|------|------------|-------|------------|-------------|------------|------------------|-------|
| 1 | | | | | | | |
| 2 | | | | | | | |
| … | | | | | | | |
| 16 | | | | | | | |

**RAG status:** 🟢 On track · 🟡 Needs support · 🔴 At risk (attendance <70% or labs incomplete)

### Trainer checklist (per module) — trainer copy only

- [ ] Outcomes stated in learner language  
- [ ] Prerequisites checked   
- [ ] Terms defined before use  
- [ ] Live demo runs on trainer machine **before** class  
- [ ] Lab sheet printed / shared (basic / intermediate / interview)  
- [ ] Common mistakes reviewed  
- [ ] Exit ticket collected  
- [ ] GitHub push encouraged same day  
- [ ] Inclusive pace: no “you should already know this” language  

---

## 7. Final Assessment Rubric

Score each dimension **0–10**. Passing job-ready bar: **≥ 35/50** and all Must projects submitted.

| Dimension | 8–10 (Strong) | 5–7 (Developing) | 0–4 (Needs work) |
|-----------|---------------|------------------|------------------|
| **Coding** | Clean, working code; edge cases handled | Works for happy path | Frequent syntax/logic failures |
| **Projects** | Capstone MVP + 4+ small repos + full deliverables bundle | Partial capstone; incomplete bundle | Incomplete / not runnable |
| **Communication** | Explains design in simple English | Needs prompting | Cannot explain own code |
| **GitHub usage** | Daily-ish commits, branches, clear README | Occasional pushes | Zip uploads only / no repo |
| **Interview readiness** | Answers core Java/SQL/Spring with examples | Partial answers | Blank on fundamentals |

**Per-module skill levels** (use on labs and exit tickets):

| Level | Meaning |
|-------|---------|
| **Not started** | No attempt / blank |
| **Guided** | Completes only with trainer/pair help |
| **Independent** | Completes lab from notes without help |
| **Interview-ready** | Explains trade-offs and answers related interview Qs |

Trainer-only keys: `JAVA/14_Trainer_Only/` (do **not** share with learners).

**Oral defense (10 min):** problem → demo → schema → one tough bug you fixed → what you’d add next.

---

## 8. How Trainers Use This Folder

1. Start every batch with [Session Calendar](../Session_Calendar_100.md) + [Course Contents](../Course_Contents.md).  
2. Teach module files in numbered order under `JAVA/` — same files students receive.  
3. SQL: follow **Required MySQL labs** in [01_MySQL_for_Full_Stack_Developers.md](../06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md) — labs live in `MYSQL/` but are **required**, not optional extras.  
4. Convert each module’s headings into PPT; labs → lab manual; graded checks → [`16_Assessments/`](../16_Assessments/) biweekly papers (not per-module MCQs).  
5. Never skip GitHub, `PreparedStatement`, JPA after JDBC, auth, or Spring lab days `06`–`07`.  
6. Grade with [standard deliverables](../Standard_Project_Deliverables.md) + skill-level rubric; keep `*_KEY.md` and `14_Trainer_Only/` private.
7. AI module is **stretch only** after a deployed Spring Boot MVP.  
8. Share students the pack from repo root `./scripts/pack_student_share.sh java` (or week’s module/PDF), **plus** sibling `MYSQL/` when needed.

---

## Delivery reminders (course-wide)

- Lead with **business stories** (student portal, expenses, bookings), then syntax — jargon after purpose.  
- Ban shame language. Normalize “I don’t know yet.”  
- Require **typing along** in demos — watching alone does not build muscle memory.  
- Celebrate first GitHub push as a ceremony; it builds professional identity.  
- Map every week to a **resume bullet** so motivation stays job-oriented.
- Teach **one voice for all learners** — never split notes into fresher vs experienced tracks.
