# Ticket: Employee Management Portal Expense CSV Append

**Customer:** Employee Management Portal accounts team  
**Need:** Record travel / stationery / canteen spends in **`expenses.csv`**. Rows must **survive** after the program exits. A second run must **add**, not wipe yesterday.

**Teaching-order:** `Path` / `Files`, UTF-8 text, `CREATE` + `APPEND`, simple CSV header, try-with-resources on a writer/reader, `catch (IOException e)`. No Git as a topic. No Spring. No Lombok. No JDBC. No MySQL.

## Starter
Complete `ensureHeader`, `appendExpense`, `listExpenses`, and `totalAmount` in `starter/ExpenseFiles.java`. Keep notes **comma-free** (simple `split(",")`).

## Broken
Default `writeString` **truncates** — the second expense wipes the first. No header. Bare `catch (Exception e)` swallows I/O failures.

## Seed
`seed/sample_expenses.csv` — use for the import Stretch (print its total).

## Done when
- [ ] Header `date,category,amount,note` is written **once** when the file is missing
- [ ] Three demo rows append; a second `java ExpenseFiles` **adds** more rows (does not replace)
- [ ] `listExpenses` prints data rows; missing file → friendly message (no traceback)
- [ ] `totalAmount` sums the amount column (`155` on the first three-row demo)
- [ ] try-with-resources on the writer (and reader if you open one)
- [ ] `IOException` is handled — not a bare `catch (Exception e)`
- [ ] No Git / Spring / Lombok / JDBC / MySQL

## Stretch
- Tiny menu: 1 Add · 2 List · 3 Total · 4 Exit (`Scanner` try-with-resources).
- Category totals with a `HashMap`.
- Import `seed/sample_expenses.csv` and print its total.
- **`java.util.logging` lite:** `INFO` when a row is saved.
- **Later — Git week:** push the folder with a short README.
- **Later — JDBC:** the same rows become `INSERT`s.
