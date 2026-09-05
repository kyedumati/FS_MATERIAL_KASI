## MySQL Course Contents (from `MYSQL`)

**Audience:** Freshers & career switchers | **DB:** MySQL 8+ | **Practice DB:** `training_db`

**Start:** [`README.md`](README.md) (two tracks) · **Homework:** [`homework/10_Practice_Exercises.md`](homework/10_Practice_Exercises.md) · **Seed:** [`labs/training_db_seed.sql`](labs/training_db_seed.sql)

---

### 1. Setup & Connection

- Install MySQL (Windows / macOS / Linux)
- MySQL Workbench
- Connect via CLI & Workbench
- Create `training_db`, useful commands, troubleshooting

### 2. Introduction to Databases

- Data, database, DBMS
- Relational vs non-relational
- Tables, rows, columns
- DBMS vs RDBMS

### 3. SQL Basics (DDL / DML / DQL)

- SQL language categories: **DDL, DML, DQL, TCL, DCL**
- DDL vs DML commit behavior
- **DDL:** CREATE, data types, constraints, DESCRIBE, ALTER, DROP, TRUNCATE
- **DML:** INSERT, UPDATE, DELETE
- **DQL:** SELECT (columns, `*`, WHERE)



### 4. Querying with SQL

- Comparison operators, `IS NULL` / `IS NOT NULL`
- `LIKE` (wildcards)
- AND / OR / NOT
- `IN`, `BETWEEN`
- `ORDER BY`, `DISTINCT`
- Pagination: `LIMIT`, `OFFSET`



### 5. Aggregations & GROUP BY

- COUNT, SUM, AVG, MIN, MAX
- Alias
- GROUP BY, WHERE + GROUP BY, HAVING



### 6. Common Concepts

- SQL expressions
- String, date, arithmetic, CAST functions
- Set operations: UNION / UNION ALL (ORDER BY, pagination)



### 7. Modeling Databases

- ER model: entity, attributes, keys, relationships
- Cardinality (1:1, 1:N, M:N)
- Primary key, foreign key
- Constraints & creating related tables



### 8. Joins

- Natural, INNER, LEFT, RIGHT, FULL, CROSS, Self join
- Multi-table joins
- Joins with filters & aggregations



### 9. Views & Subqueries

- CREATE / query / DROP view
- Subqueries in WHERE, SELECT, FROM
- Correlated subquery, EXISTS / NOT EXISTS
- Subquery vs JOIN



### 10. Transactions, DCL & Indexes

- ACID (Atomicity, Consistency, Isolation, Durability)
- **TCL:** START TRANSACTION, COMMIT, ROLLBACK, SAVEPOINT
- **DCL:** GRANT, REVOKE
- Indexes: CREATE / DROP, when to use



### 11. Window Functions & CTEs

- ROW_NUMBER, RANK, DENSE_RANK
- CTEs (WITH), multiple CTEs, recursive CTEs



### 12. Practice Exercises

- Chapter-wise homework in `MYSQL/homework/10_Practice_Exercises.md`
- Sample rows: `MYSQL/labs/training_db_seed.sql` (before chapter 03)



### 13. Real-Time Projects

1. **Employee Management Portal** — Employee Management
2. **Swiggy** — Food Delivery
3. **Apollo Hospitals** — Hospital Management
4. **HDFC Bank** — Banking

