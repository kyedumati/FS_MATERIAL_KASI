# Ticket: MedCare — Never Crash on Bad Input

**Customer:** MedCare registration desk  
**Need:** Read a **patient age** from text. Non-integers are a format error. Age outside **1–120** is a domain error (`InvalidAgeException`). The program must **not** dump a traceback for those cases.

**Teaching-order:** `try` / `catch` / `finally`, `throw`, `throws`, custom exceptions, try-with-resources on **`Scanner`**. **No files** (File Handling is next). No Spring. No Lombok. No JDBC.

## Starter
Complete `readAge` in `starter/SafeInput.java`. Keep `InvalidAgeException` checked (`extends Exception`).

## Broken
Bare `catch` swallows the error and returns `-1`. No range check. No custom exception.

## Done when
- [ ] `"21"` → `21`
- [ ] `"abc"` is caught as `NumberFormatException` (friendly message; no traceback)
- [ ] `"0"` and `"200"` raise / are caught as `InvalidAgeException`
- [ ] `InvalidAgeException extends Exception` (checked) and `readAge` declares `throws InvalidAgeException`
- [ ] Catch **specific** types — not a bare `catch (Exception e)` that hides bugs
- [ ] No files / Spring / Lombok / JDBC

## Stretch
- `while` prompt until a valid age (retry on both error types).
- `readPositiveAmount` for INR (same parse + range pattern).
- **Later — Files week:** wrap a `Scanner` on a text file with try-with-resources (same `AutoCloseable` idea).
