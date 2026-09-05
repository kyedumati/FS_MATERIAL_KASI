# Biweekly Assessment BW02 — Weeks 3–4

**Sessions covered:** S11–20  
**Topics:** `if` / `else if` / `else`, `switch`, `for` / `while`, `break`/`continue`, menus, strings (`equals`, `substring`, `trim`), arrays, marks manager

**Timebox:** 45–60 minutes (homework or Friday of the even week).  
**Rules:** Closed notes unless your trainer allows open notes. No copying.  
**Coding constraint:** Loops, `if`, and arrays OK. **No extra methods** (Methods start Week 5). **No `ArrayList`.**

---

## A. Multiple Choice (12)

Circle the best option.

1. `else if` means:
   a) another test after `if` failed
   b) end if
   c) error if
   d) empty if

2. `for (int i = 1; i <= 4; i++)` runs how many times?
   a) 4
   b) 5
   c) 3
   d) 1

3. `break` in a loop:
   a) Restarts Java
   b) Deletes variables
   c) Skips one iteration
   d) Exits the loop immediately

4. `continue` in a loop:
   a) Creates a new loop
   b) Exits the program
   c) Skips the rest of this iteration
   d) Pauses forever

5. A `while (true)` menu needs:
   a) No exit path
   b) A `break` (or flag) when the user quits
   c) Only `for`
   d) Only `println`

6. Strings in Java are:
   a) Immutable
   b) Always integers
   c) Only uppercase
   d) Mutable in place (you can change `s.charAt(0)`)

7. `"Hello".substring(1, 4)` is:
   a) `ello`
   b) `H`
   c) `Hel`
   d) `ell`

8. Arrays use which brackets for access?
   a) `<>`
   b) `()`
   c) `{}` only
   d) `[]`

9. Last index of `int[] a = new int[5]` is:
   a) 5
   b) 4
   c) 0
   d) 6

10. Empty marks (`count == 0`) average should:
    a) Be guarded (message / skip)
    b) Always be 100
    c) Crash intentionally in production
    d) Divide by zero quietly

11. Nested `if` means:
    a) Only loops
    b) Only strings
    c) `if` inside another `if`
    d) Two files

12. `"  Hi ".trim()` returns:
    a) `"  Hi"`
    b) `"  Hi "`
    c) `"Hi"`
    d) `"Hi "`

---

## B. Coding (2)

1. Write a mini **HDFC Bank** ATM menu (balance starts 1000): options Balance / Deposit / Withdraw / Quit. Block overdraft. Use `while`/`if` only — **no extra methods**.

```java
// your code
```

2. Keep marks in an `int[]` plus `count`. Menu: add mark (0–100), list, average (safe if empty), toppers (≥90), quit. No extra methods. No `ArrayList`.

```java
// your code
```

---

## C. Short answer (1)

When do you choose `for` vs `while`? Give one example of each from a student-portal style app.

_(Write 3–6 sentences.)_
