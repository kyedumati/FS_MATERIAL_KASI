# Biweekly Assessment BW05 — Weeks 9–10

**Sessions covered:** S41–50  
**Topics:** Exception handling (try/except + custom), files/CSV/logging, Git/GitHub, MySQL setup and SELECT intro

**Timebox:** 45–60 minutes (homework or Friday of the even week).  
**Rules:** Closed notes unless your trainer allows open notes. No copying.  
**Coding constraint:** Files + SQL concepts OK.

---

## A. Multiple Choice (12)

Circle the best option.

1. `with open(...) as f:` mainly helps:
   a) Faster CPU always
   b) Auto-close the file
   c) Skip encoding
   d) Avoid Python

2. CSV rows are often read with:
   a) django only
   b) React
   c) pip freeze
   d) csv.DictReader

3. Logging levels include:
   a) HTML/CSS
   b) SELECT/INSERT
   c) DEBUG/INFO/WARNING/ERROR
   d) Only PRINT

4. `git add` then `git commit`:
   a) Runs tests only
   b) Stages then records a snapshot
   c) Deletes repo
   d) Deploys to AWS

5. `git push` sends commits to:
   a) Local only
   b) Remote (e.g. GitHub)
   c) MySQL
   d) VS Code theme

6. Primary key in SQL uniquely identifies:
   a) A row
   b) A CSS class
   c) A React prop
   d) A column type

7. `SELECT ... WHERE` is used to:
   a) Commit git
   b) Create venv
   c) Filter rows that match a condition
   d) Style HTML

8. Parameterized queries help prevent:
   a) f-string typos
   b) Slow CSS
   c) SQL injection
   d) Git conflicts

9. Custom exception classes usually inherit from:
   a) str
   b) Exception
   c) list
   d) dict

10. `README.md` on GitHub should:
   a) Explain how to run the project
   b) Store passwords
   c) Replace git
   d) Be empty

11. `finally` block runs:
   a) Usually always after try
   b) Never
   c) Only on success
   d) Only on error

12. Foreign key links:
   a) Git branches only
   b) Two unrelated files
   c) A column to another table's key
   d) CSS to HTML only

---

## B. Coding (2)

1. Write `add_expense(title, amount, category)` that raises `ValueError` if amount ≤ 0, else appends to a list of simple objects/dicts. Then sketch `export_csv(path)` using `csv.DictWriter`.

```python
# your code
```

2. Write a safe age reader: convert input to int; if out of 1–120 raise a custom `InvalidAgeError`. Show try/except in a tiny demo loop.

```python
# your code
```

---

## C. Short answer (1)

Why commit often with clear messages during training?

_(Write 3–6 sentences.)_
