# 07 — JDBC

| File | Focus | Calendar |
|------|-------|----------|
| [01_JDBC_CRUD.md](01_JDBC_CRUD.md) | Connection, `PreparedStatement`, CRUD | S55–S58 |

**Lab kit:** [16_jdbc_library_crud](../15_Lab_Assets/16_jdbc_library_crud/) (S55–S58)

**Authored:** JDBC CRUD (`01`). Same *ideas* as the Python FS database-programming bridge; Java uses JDBC + `PreparedStatement` `?` (not `mysql.connector` / `%s` / Django). After required `MYSQL/` labs; **before** Spring / JPA. try-with-resources for `Connection`. No string-concat SQL. No Spring Boot. No Lombok. No `DataSource` / Hikari as required. Secrets: `.env.example` (never commit passwords). `application.yml` is Spring — not this module.

[Session Calendar](../Session_Calendar_100.md)
