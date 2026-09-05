# Ticket: Campus Library JDBC CRUD

**Customer:** Campus library desk  
**Need:** Clerks must **list**, **add**, **update copies**, and **remove** books in MySQL from a **Java CLI** — not Workbench, not a CSV. User-typed titles must never become SQL commands. (Library stays the kit. Same `?` pattern later maps to **Employee Management Portal** `employee` CRUD.)

**Teaching-order:** `DriverManager` + `Connection` try-with-resources, `PreparedStatement` `?` for SELECT / INSERT / UPDATE / DELETE, `SQLException`, password from env / `.env` (never committed). PK/FK, JOIN, and TCL were already taught in [`MYSQL/`](../../../MYSQL/) — this kit **uses** `books` (seed). No Spring Boot. No JPA / Hibernate. No Lombok. No `DataSource` / Hikari. No `application.yml` (that is Spring). No `Statement` + string-concat SQL on the core path.

## Starter
Complete `openConnection`, `listBooks`, `addBook`, `updateCopies`, and `deleteByTitle` in `starter/LibraryCrud.java`. Copy [`.env.example`](./.env.example) to `.env` and set your lab password. Put **MySQL Connector/J** on the `java -cp` classpath (see run steps).

## Broken
Hard-coded password. `Statement` + `"'" + author + "'"` SELECT. INSERT built with string concat. Connection never closed. Bare `catch (Exception e)` swallows `SQLException`.

## Seed
`seed/library_books.sql` — run **once** against MySQL 8+ (`training_db`, table `books`). Stretch tables `members` / `loans` are in the same file; core path does not need them.

## Run (after Connector/J JAR is next to the `.java` file)

```bash
# download once (version pin — 8.4.x is fine on JDK 17 + MySQL 8)
# curl -L -o mysql-connector-j-8.4.0.jar \
#   https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar

cp ../.env.example .env   # then edit MYSQL_PASSWORD
mysql -u root -p < ../seed/library_books.sql
javac LibraryCrud.java
java -cp ".:mysql-connector-j-8.4.0.jar" LibraryCrud          # macOS / Linux
java -cp ".;mysql-connector-j-8.4.0.jar" LibraryCrud          # Windows
```

## Done when
- [ ] `Connection` (and statements / result sets) use **try-with-resources**
- [ ] Password comes from **env** or **`.env`** — not a literal in source; `.env` is not committed
- [ ] List / add / update copies / delete each use **`PreparedStatement`** and **`?`**
- [ ] Demo `main`: list seed books, INSERT one campus title, UPDATE its copies, DELETE that same title
- [ ] `SQLException` is handled — not a bare `catch (Exception e)`
- [ ] No `Statement`, no `"'" + name + "'"`, no Spring / JPA / Lombok / `DataSource` / `application.yml`

## Stretch
- Tiny menu: 1 List · 2 Add · 3 Update copies · 4 Delete · 5 Exit (`Scanner` try-with-resources).
- Parameterized `SELECT` with `INNER JOIN` on seed `loans` / `members` ([`MYSQL/07`](../../../MYSQL/07_Joins.md) — SQL you already know; bind with `?`).
- `conn.setAutoCommit(false)` around “loan a copy + decrement `copies`”; `rollback` on failure ([`MYSQL/09`](../../../MYSQL/09_Transactions_and_Indexes.md)).
- Title search: `WHERE title LIKE ?` — put the `%` **in the Java value**, not in the SQL string.
- **Later — Maven / Spring:** `pom.xml` + a pool (`DataSource`). Not this ticket.
