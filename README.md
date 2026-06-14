# PFS Training Material

Structured training material for **Python**, **MySQL**, and **React** — designed for freshers and mid-level engineers switching careers.

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

## Python Course

**Audience:** Absolute beginners learning programming fundamentals.

| Order | File | Topic |
|-------|------|-------|
| 1 | [01_Programming_Fundamentals](PYTHON/01_Programming_Fundamentals.md) | Variables, data types, strings |
| 2 | [02_Operators](PYTHON/02_Operators.md) | Arithmetic, comparison, logical operators |
| 3 | [03_Input_and_Output_Statements](PYTHON/03_Input_and_Output_Statements.md) | Input/output, formatting |
| 4 | [04_Flow_Control](PYTHON/04_Flow_Control.md) | if/else, loops |

---

## How to Use This Material

**For trainers**
- Follow the numbered order within each folder.
- Use `10_Practice_Exercises.md` for weekly homework after each MySQL chapter.
- Reserve extra time on **Joins (07)** and the **capstone projects (12)** — these are the highest-value modules for career switchers.

**For students**
- Install MySQL first (file `00`), then work through chapters in order.
- Run every SQL example in Workbench or the CLI — do not just read.
- Complete at least one project from `12_Real_Time_Projects.md` for your portfolio.

---

## Repository Structure

```
PFS_MATERIAL_KASI/
├── README.md
├── PYTHON/          # Python fundamentals (4 modules)
└── MYSQL/             # MySQL course (13 modules + exercises)
```
