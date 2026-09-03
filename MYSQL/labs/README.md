# Ticket: Load `training_db` sample tables

**Customer:** Training lab  
**Need:** One script students can run so homework queries have rows. No hunting `CREATE TABLE` across notes.

## Files

- [`training_db_seed.sql`](training_db_seed.sql) — run in MySQL Workbench or the CLI

## When to run

- **After** [setup](../00_MySQL_Setup_and_Connection.md) (`training_db` exists).
- **Before** querying homework (module 03+).
- Module 02 still has you `CREATE` `player` and `employee` yourself — those tables are **not** in the seed.

Re-running the script is safe. It replaces only the drill tables listed in the file. It does not drop `player` or `employee`.

## How to run

**Workbench:** File → Run SQL Script → `MYSQL/labs/training_db_seed.sql` → execute.

**CLI** (from the repo root):

```bash
mysql -u root -p < MYSQL/labs/training_db_seed.sql
```

## Done when

- [ ] `USE training_db;` then `SHOW TABLES;` lists `product`, `movie`, `student`, `course`, and the other drill tables
- [ ] `SELECT COUNT(*) FROM product;` returns rows
- [ ] You can start [homework chapter 03](../homework/10_Practice_Exercises.md)
