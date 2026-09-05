# Ticket: Never Crash on Bad Input

**Customer:** Apollo Hospitals registration desk  
**Need:** Read an int age. Non-numeric input is `ValueError`. Age outside 1–120 is custom `InvalidAgeError`. Expected cases must not print a traceback.

**Teaching-order:** `try` / `except` / `raise`, custom exception class. No type hints required. No `raise ... from e` and no `assert` in the core path.

## Starter
Complete `read_age` in `starter/safe_age.py`. `InvalidAgeError` is already declared. Keep the `__main__` loop — it prints the four samples.

## Broken
Bare `except:` returns `-1` (hides bugs and can block Ctrl+C). No range check — `"0"` and `"200"` look successful.

## Done when
- [ ] `"21"` prints `21 -> 21`
- [ ] `"abc"` is caught as `ValueError` with message `age must be an integer` (no traceback)
- [ ] `"0"` and `"200"` raise / are caught as `InvalidAgeError` (`age out of range: …`)
- [ ] Custom `InvalidAgeError` inherits `Exception`
- [ ] No type hints required

## Stretch
- Wrap `read_age` in a `while True` prompt until a valid age is entered.
- Add `read_positive_float` for amounts (same pattern).
- **Later — Files week:** log failures with a timestamp (`datetime.now()`).
