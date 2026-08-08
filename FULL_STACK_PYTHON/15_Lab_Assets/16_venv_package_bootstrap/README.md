# Ticket: Ship a Tiny Utils Package

**Customer:** Team lead  
**Need:** Package `campus_utils` with `format_inr` + venv instructions.

## By day

| Focus | Do this |
|-------|---------|
| Day 1 | Open `starter/`; understand folder layout; finish `formatters.py` TODO; import from `main.py` |
| Day 2 | Re-export from `__init__.py`; create/activate `venv`; `pip freeze` → `requirements.txt` |
| Day 3 | Optional: load a small JSON defaults file; polish README; push (no `venv/` in Git) |

## Starter

1. Complete `starter/campus_utils/formatters.py`.  
2. Make `from campus_utils import format_inr` work via `__init__.py`.  
3. Run `starter/main.py` inside an activated venv.

## Broken

`broken/` has a classic import / formatter bug — fix it.

## Seed

`seed/requirements.txt` — example freeze list for teammates.

## Done when

- [ ] `format_inr` works and `main.py` prints a ₹ amount  
- [ ] Package import works **without** `sys.path` hacks  
- [ ] `venv` activated; `requirements.txt` present  
- [ ] README shows activate → install → run for a teammate (Windows + macOS/Linux)  
- [ ] No `venv/` committed when you push  

**Stretch:** second helper module + relative import in `__init__.py`; pin versions in `requirements.txt`.
