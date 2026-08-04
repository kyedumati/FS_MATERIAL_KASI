# Required MySQL Labs Checklist (Full Stack Python)

SQL is **core placement skill**, not an optional side course.  
This package keeps deep SQL notes in repo folder [`MYSQL/`](../../MYSQL/) to avoid duplication, but the labs below are **mandatory** for every Full Stack Python batch.

**Schedule authority:** [11_Session_Calendar_100.md](11_Session_Calendar_100.md) — MySQL phase is **Weeks 10–11** (Sessions 46–55).  
**Bridge lesson:** [`../05_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md`](../05_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md)  
**Python connectivity:** [`../03_Advanced_Python/06_Database_Programming_Bridge.md`](../03_Advanced_Python/06_Database_Programming_Bridge.md)

---

## How to use this checklist

**Learners:** Tick Required labs during **Weeks 10–11**; aim for Independent skill on CRUD + JOINs before Django models / capstone schema.

**Trainers:** Teach the FS MySQL bridge in this window, assign Required rows as homework, and block Django ORM / capstone DB design until CRUD + JOINs are Independent or better.

---

## Required labs (Must)

| Done | When | Lab file | Learner must be able to |
|:----:|------|----------|-------------------------|
| ☐ | W10 / S46 | [`MYSQL/00_MySQL_Setup_and_Connection.md`](../../MYSQL/00_MySQL_Setup_and_Connection.md) | Install/connect; create `training_db` |
| ☐ | W10 / S46–47 | [`MYSQL/01_Introduction_to_Databases.md`](../../MYSQL/01_Introduction_to_Databases.md) | Explain table/row/DBMS vs Excel |
| ☐ | W10 / S47–48 | [`MYSQL/02_Introduction_to_SQL_Basic_Concepts.md`](../../MYSQL/02_Introduction_to_SQL_Basic_Concepts.md) | DDL + DML CRUD + constraints |
| ☐ | W10 / S49 | [`MYSQL/03_Querying_with_SQL.md`](../../MYSQL/03_Querying_with_SQL.md) | WHERE, LIKE, ORDER BY, LIMIT |
| ☐ | W10 / S50 | FS MySQL bridge module above | ER sketch for Library / CampusCart |
| ☐ | W11 / S51 | [`MYSQL/06_Modeling_Databases.md`](../../MYSQL/06_Modeling_Databases.md) | PK/FK, 1:N |
| ☐ | W11 / S52–53 | [`MYSQL/07_Joins.md`](../../MYSQL/07_Joins.md) | INNER + LEFT JOIN multi-table reports |
| ☐ | W11 / S54 | [`MYSQL/09_Transactions_and_Indexes.md`](../../MYSQL/09_Transactions_and_Indexes.md) | COMMIT/ROLLBACK; when index helps |
| ☐ | W11 | [`MYSQL/10_Practice_Exercises.md`](../../MYSQL/10_Practice_Exercises.md) | Complete exercises for ch. 02, 03, 07 |
| ☐ | W11 / S55 | Python bridge module above | Parameterized INSERT/SELECT/UPDATE/DELETE from Python |

---

## Strongly recommended (before placement mocks)

| Done | Lab file | Why |
|:----:|----------|-----|
| ☐ | [`MYSQL/04_Aggregations_and_Group_By.md`](../../MYSQL/04_Aggregations_and_Group_By.md) | COUNT/SUM interviews |
| ☐ | [`MYSQL/05_Common_Concepts.md`](../../MYSQL/05_Common_Concepts.md) | Dates/strings in reports |
| ☐ | [`MYSQL/08_Views_and_Subqueries.md`](../../MYSQL/08_Views_and_Subqueries.md) | Common interview depth |
| ☐ | One project from [`MYSQL/12_Real_Time_Projects.md`](../../MYSQL/12_Real_Time_Projects.md) | Portfolio SQL proof |

*Optional advanced:* [`MYSQL/11_Window_Functions_and_CTEs.md`](../../MYSQL/11_Window_Functions_and_CTEs.md) — only if Required set is solid.

---

## Placement SQL mini-bar (exit ticket)

Learner can, without notes:

1. Write CREATE TABLE with PK + FK  
2. INSERT / UPDATE / DELETE safely  
3. SELECT with WHERE + ORDER BY  
4. INNER JOIN two tables and explain LEFT JOIN  
5. Explain why we use parameterized queries from Python  

---

## Delivery notes

- Say “open `MYSQL/07` now” in class — make the dependency **visible and scheduled**, not “read later if you want.”  
- One join diagram on the whiteboard beats three abstract definitions.  
- Do not start Django models until Required CRUD + JOIN labs are attempted.
