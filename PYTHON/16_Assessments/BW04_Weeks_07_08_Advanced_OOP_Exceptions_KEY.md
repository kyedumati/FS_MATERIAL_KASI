# KEY — Biweekly Assessment BW04 — Weeks 7–8 (Trainer only)

**Do not share with students.** Excluded from student pack (`*_KEY.md`).

## A. MCQ answers

1. **b** — Generator
2. **d** — __init__.py (package marker)
3. **c** — Virtual environment / dependencies
4. **c** — Runs when instance is created
5. **b** — Private-ish attributes + methods
6. **a** — Inheritance to call parent
7. **b** — TypeError
8. **b** — ABC with only abstract methods
9. **a** — g = f(g)
10. **a** — tuple
11. **c** — self
12. **b** — One name, different behaviours

## B. Coding — model points

1. Write a generator `read_rows(rows)` that `yield`s each dict from an in-memory list (do not return a full new list).
   - Award marks for correctness + teaching-order constraints respected.

2. Create **SecureBank** `BankAccount` with `__balance`, `deposit`, `withdraw`, `get_balance`. Reject bad amounts with print+return (no `raise` / `try` / `except`).
   - Award marks for correctness + teaching-order constraints respected.

## C. Short answer — model

Memory: yield one row at a time; list loads everything into RAM.

## Suggested scoring

| Section | Marks |
|---------|------:|
| A MCQ (1 each) | 12 |
| B Coding (6 each) | 12 |
| C Short | 6 |
| **Total** | **30** |
