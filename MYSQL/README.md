# MySQL (MySQL 8+)

**Kasi Yedumati · Full Stack Training**

**Shared topic pack** — used by Python Full Stack, Java Full Stack, and a MySQL-only course.  
Not owned by `PYTHON/` or `JAVA/`.

**Practice DB:** `training_db` · **Start:** [00_MySQL_Setup_and_Connection.md](00_MySQL_Setup_and_Connection.md) · **Syllabus map:** [Course_Contents.md](Course_Contents.md)

## Two tracks, same files

| Track | Open these | Later / stretch |
|-------|------------|-----------------|
| **Full stack (Weeks 10–11)** | 00 → 01 → 02 → 03 → 06 → 07 → 09 | 04, 05, 08, 11 until placement mocks |
| **MySQL-only (~18 sessions)** | 00 through 09, then 11, then 12 | Homework after each class |

SQL depth lives here. Python/Java folders only hold the **bridge** (ER, why the backend talks SQL).

**Python FS schedule:** Weeks 10–11 — [Session Calendar](../PYTHON/Session_Calendar_100.md)  
**Java FS schedule:** Weeks 10–11 — [Session Calendar](../JAVA/Session_Calendar_100.md)

## Teaching order

| Order | Module | Track |
|------:|--------|-------|
| 1 | [00_MySQL_Setup_and_Connection.md](00_MySQL_Setup_and_Connection.md) | Both |
| 2 | [01_Introduction_to_Databases.md](01_Introduction_to_Databases.md) | Both |
| 3 | [02_Introduction_to_SQL_Basic_Concepts.md](02_Introduction_to_SQL_Basic_Concepts.md) | Both |
| 4 | [03_Querying_with_SQL.md](03_Querying_with_SQL.md) | Both |
| 5 | [04_Aggregations_and_Group_By.md](04_Aggregations_and_Group_By.md) | MySQL-only · FS stretch |
| 6 | [05_Common_Concepts.md](05_Common_Concepts.md) | MySQL-only · FS stretch |
| 7 | [06_Modeling_Databases.md](06_Modeling_Databases.md) | Both |
| 8 | [07_Joins.md](07_Joins.md) | Both |
| 9 | [08_Views_and_Subqueries.md](08_Views_and_Subqueries.md) | MySQL-only · FS stretch |
| 10 | [09_Transactions_and_Indexes.md](09_Transactions_and_Indexes.md) | Both |
| 11 | [11_Window_Functions_and_CTEs.md](11_Window_Functions_and_CTEs.md) | MySQL-only · FS stretch |
| 12 | [12_Real_Time_Projects.md](12_Real_Time_Projects.md) | MySQL-only capstone |

**Homework (use throughout):** [homework/10_Practice_Exercises.md](homework/10_Practice_Exercises.md) — chapter-wise drills. Not a live-class topic; that is why it is not numbered in the table above.

**Sample data:** [labs/training_db_seed.sql](labs/training_db_seed.sql) — run after setup, before querying homework (module 03+). See [labs/README.md](labs/README.md).

### Suggested class plan (~18 sessions, MySQL-only)

| Sessions | Modules | Notes |
|----------|---------|-------|
| 1–2 | 00, 01 | Setup + database concepts; create `training_db` |
| 3–4 | 02 | CRUD, constraints, data types (`player` you CREATE yourself) |
| 5–6 | 03 | Filtering, sorting, pagination (seed loaded) |
| 7–8 | 04, 05 | Aggregations + string/date functions |
| 9–10 | 06 | Schema design and relationships |
| 11–12 | 07 | Joins — spend extra time here |
| 13 | 08 | Subqueries and views |
| 14 | 09 | Transactions, indexes, permissions |
| 15 | 11 | Window functions and CTEs |
| 16–18 | 12 | Real-time project capstone |

**Sibling shared topics:** [`GIT/`](../GIT/) · [`FRONTEND/`](../FRONTEND/)
