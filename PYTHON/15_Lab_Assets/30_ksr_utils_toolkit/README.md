# Ticket: Ship `ksr_utils` — Personal Python Toolkit

**Customer:** Your future self (and GitHub reviewers)  
**Need:** A small reusable package with validators, formatters, `map`/`filter` helpers, and decorators.

**Teaching order:** Core homework does **not** use `yield` / generators. Add `generators.py` only after Session 31.

## Starter

1. Open `starter/ksr_utils/` and finish every TODO in validators, formatters, transforms, decorators.  
2. Run `starter/demo.py` until prints succeed.  
3. Push the package to GitHub with a short README.

## Broken

`broken/` has classic bugs (mutable default, wrong phone clean). Fix them.  
`broken/ksr_utils/generators.py` is **stretch after S31** (returns a list instead of yielding).

## Done when (functions homework)

- [ ] `is_email`, `is_phone_in`, `is_positive` work  
- [ ] `format_inr` / `format_date(day, month, year)` work  
- [ ] `with_gst` uses `map`; `keep_high` uses `filter`  
- [ ] `@timing` prints elapsed time  
- [ ] `demo.py` runs clean (**no** `read_rows` required)

## Stretch (after S31 — Generators)

- [ ] Finish `generators.py`: `read_rows` must **`yield`** (not `return` a list)  
- [ ] Re-export from `__init__.py` and print rows in `demo.py`  
- [ ] **Later (Files week):** `yield` from a real CSV with `csv.DictReader`
