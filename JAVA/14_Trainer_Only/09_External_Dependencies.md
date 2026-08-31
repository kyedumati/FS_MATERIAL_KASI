# External Dependencies (Versioned)

`JAVA/` is the **Java program** (calendar, Core Java / OOP / JDBC / Spring Boot notes, Java lab kits).  
Shared, non-Java topics live at **repo root** so Python FS and Java FS reuse the **same** files.

| Dependency | Path (repo root) | Role | Version / pin |
|------------|------------------|------|----------------|
| **MySQL** | [`MYSQL/`](../../MYSQL/) | Shared SQL depth (FS Weeks 10–11 / S46–54; also MySQL-only batches) | Same git commit as this release |
| **Frontend** | [`FRONTEND/`](../../FRONTEND/) | Shared HTML / CSS / JS (+ `FRONTEND/labs/`) and **React** under [`FRONTEND/REACT/`](../../FRONTEND/REACT/) | Same commit |
| **Syllabus map** | `COURSE_CONTENTS/Full_Stack_Java_Course_Contents.md` | Brochure alignment | Calendar wins on order |

## Contract

1. **Schedule** for the Java batch stays in [Session_Calendar_100.md](../Session_Calendar_100.md) — including days that open `FRONTEND/`, `FRONTEND/REACT/`, `MYSQL/`.  
2. **Edit shared topics once** in `MYSQL/` / `FRONTEND/` — do not copy into `JAVA/`.  
3. Student packs must include those siblings (see pack script).  
4. Pointers only: `JAVA/08_Frontend/README.md` and `11_React/README.md`.  
5. JDBC / JPA modules **point** at required `MYSQL/` labs; they do not rewrite SQL.

## Student distribution

| Option | What to zip |
|--------|-------------|
| A (recommended) | `dist/JAVA_STUDENT/` (nests program + FRONTEND + MYSQL) |
| B (USB offline) | Same + `COURSE_CONTENTS/Full_Stack_Java_Course_Contents.md` |

## Change control

When renaming a shared file, update **both** Session Calendars (Python and Java) and any Prev/Next links.
