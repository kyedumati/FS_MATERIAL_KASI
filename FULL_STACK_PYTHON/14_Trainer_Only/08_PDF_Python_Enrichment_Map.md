# Legacy Python notes — Removed

**Status:** `PDF/PYTHON/` and source folder `PYTHON/` were **removed** from this repo.  
Do **not** restore them as a parallel curriculum.

All Python teaching lives in **`FULL_STACK_PYTHON/`**. SQL depth lives in **`MYSQL/`**.

## Where topics live now

| Old topic (was PDF 01–20) | Use this instead |
|---|---|
| Programming fundamentals | `01_Foundations/` + `02_Core_Python/01_…` |
| Operators · I/O | `02_Core_Python/02_…` |
| Flow control | `02_Core_Python/03_…` |
| String | `02_Core_Python/04_…` |
| List / Tuple / Set / Dict | `02_Core_Python/05`–`07` (+ `08` DS overview) |
| Functions | `03_Advanced_Python/01_…` |
| Modules / Packages | `03_Advanced_Python/02_…` |
| OOP | `03_Advanced_Python/03_OOP.md` + Parts 1–3 + optional `07_Professional_Python_Deep_Dive.md` |
| Exceptions | `03_Advanced_Python/04_…` |
| Files · Logging | `03_Advanced_Python/05_…` |
| Database programming | `03_Advanced_Python/06_…` + Required MySQL labs (`MYSQL/`) |

## Why we removed them

- Two packs = double prep and conflicting examples.  
- Legacy notes used outdated or unsafe patterns (`eval(input)`, bare `except`, `has_key`, etc.).  
- Full Stack modules already include labs, assessments, visuals, and the placement path.

**Source of truth for class and students:** `FULL_STACK_PYTHON/` only (+ share sibling `MYSQL/` for SQL weeks).
