# Module 04 — Exception Handling

**Phase:** Advanced Python

**Duration:** See [Session Calendar](../00_Course_Guide/11_Session_Calendar_100.md) (1h 15m live sessions).

**Previous module:** OOP
**Next module:** File Handling and Logging

---

## Learning Outcomes

By the end of this session, learners will be able to:

1. Use `try`, `except`, `else`, and `finally` blocks correctly.
2. Identify and handle common built-in exceptions.
3. Raise exceptions intentionally with `raise`.
4. Create custom exception classes for domain errors.
5. Write robust CLI and file programs that fail gracefully.
6. Explain exception handling best practices for interviews and production code.

---

## Classroom Ticket

Open the lab kit **before** long notes. Read the ticket → code in `starter/` or fix `broken/`.

- **[Safe age input + custom error](../15_Lab_Assets/18_safe_input_exceptions/)**

Finish the ticket in class; compare with the official solution only when your trainer says so.

### What is an exception?

When Python hits a problem it cannot solve — dividing by zero, opening a missing file, converting `"abc"` to `int` — it **raises an exception** and, if nobody handles it, **stops** with a traceback.

### Why handle exceptions?

Without handling, a wrong PIN or a missing CSV crashes the whole program. With handling, you show a clear message and continue (or shut down cleanly).

Think of an ATM: wrong PIN should not “explode” the machine — it shows “Invalid PIN” and lets the user retry.

| Piece | Plain meaning |
|-------|----------------|
| `try` | Attempt this risky code |
| `except` | If this error type happens, do this instead of crashing |
| `else` | Runs only when **no** exception happened |
| `finally` | Always runs — cleanup (close file, release connection) |

**Custom exceptions** name business failures clearly: `InsufficientBalanceError`, `SeatAlreadyBookedError` — better for readers and APIs than a bare `Exception`.

---

## Important Concepts

### 1. Basic try/except — what / why, then syntax

**What:** Catch errors by type and recover.  
**Why:** User input and files fail often; crash-only programs are not shippable.

```python
try:
    num = int(input("Enter number: "))
    print(100 / num)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

**Note / trap:**
- Bare `except:` catches `KeyboardInterrupt` and hides bugs — catch specific exceptions.
- Swallowing exceptions with empty `except: pass` — log and handle, or re-raise.
- Using exceptions for flow control is slow and unreadable — use if/else for expected cases.

**Try these (2 programs):**

**Program 1 — UPI PIN with retry**

```python
# Simulate two attempts: bad then good (replace with input() in lab)
attempts = ["ab12", "1234"]

for attempt in attempts:
    try:
        pin = int(attempt)
        print("PIN accepted:", pin)
        break
    except ValueError:
        print("PIN must be digits only")
```

**Program 2 — Split bill safely**

```python
bill = 500
# Simulate inputs; use input() in lab: friends = int(input("Friends: "))
for friends in (4, 0):
    try:
        share = bill / friends
        print(f"Each pays ₹{share:.2f}")
    except ZeroDivisionError:
        print("Cannot split among 0 friends")
```

### 2. Catching multiple exceptions

**What:** One handler for several related error types.  
**Why:** Same recovery path (e.g. “bad data file”) without duplicate blocks.

```python
try:
    data = open("missing.txt")
    value = int(data.read())
except (FileNotFoundError, ValueError) as e:
    print("Error:", e)
```

**Note / trap:**
- Over-broad `except Exception` masks real bugs — catch narrow types first.

**Try these (2 programs):**

**Program 1 — File + int with one handler**

```python
# Create marks.txt with a non-integer to also hit ValueError, or omit file for FileNotFoundError
try:
    with open("marks.txt", encoding="utf-8") as f:
        value = int(f.readline().strip())
    print("Marks:", value)
except (FileNotFoundError, ValueError) as e:
    print("Could not read marks — check file exists and holds a number.", e)
```

**Program 2 — Dict KeyError / ValueError**

```python
samples = [
    {"age": "21"},
    {"age": "twenty"},
    {"name": "Ravi"},  # missing age
]

for data in samples:
    try:
        age = int(data["age"])
        print("Age:", age)
    except (KeyError, ValueError) as e:
        print("Bad age data:", type(e).__name__, e)
```

### 3. else and finally

**What:** Success path (`else`) vs guaranteed cleanup (`finally`).  
**Why:** Keep “happy path” separate from error handling; always release resources.

```python
try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print("Read success, length:", len(content))   # runs if no exception
finally:
    print("Cleanup block always runs")
    # if f was opened, close here in real code — prefer `with`
```

**Note / trap:**
- `return` inside `finally` can suppress exceptions — keep `finally` for cleanup only.

**Try these (2 programs):**

**Program 1 — `else` and `finally` on age input**

```python
# Simulate: try "abc" then "20" — or use input("Age: ") in lab
for raw in ("abc", "20"):
    try:
        age = int(raw)
    except ValueError:
        print(f"Invalid age: {raw!r}")
    else:
        print("Welcome to the form")
    finally:
        print("Attempt finished")
```

**Program 2 — `finally` runs even after `return`**

```python
def demo():
    try:
        print("In try — about to return")
        return "success"
    finally:
        print("finally still runs before the return completes")

print("Result:", demo())
```

### 4. raise — intentional errors

**What:** You create an error on purpose when input or state is invalid.  
**Why:** Fail fast with a clear message instead of continuing with bad data.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    return balance - amount
```

**Try these (2 programs):**

**Program 1 — `set_discount` with `raise`**

```python
def set_discount(percent):
    if not 0 <= percent <= 100:
        raise ValueError(f"Discount must be 0–100, got {percent}")
    print(f"Discount set to {percent}%")

for p in (120, -5, 15):
    try:
        set_discount(p)
    except ValueError as e:
        print("Error:", e)
```

**Program 2 — `book_seat` capacity check**

```python
def book_seat(available, requested):
    if requested > available:
        raise ValueError("Not enough seats")
    print(f"Booked {requested} seat(s). Left: {available - requested}")

for avail, req in ((5, 2), (3, 5)):
    try:
        book_seat(avail, req)
    except ValueError as e:
        print("Booking failed:", e)
```

### 5. Custom exception class

```python
class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds balance."""
    pass

class InvalidAccountError(Exception):
    def __init__(self, account_id, message="Invalid account"):
        self.account_id = account_id
        super().__init__(f"{message}: {account_id}")
```

**Note / trap:**
- Custom exception not inheriting `Exception` → not caught as expected — always inherit `Exception`.

**Try these (2 programs):**

**Program 1 — Custom `UnderAgeError`**

```python
class UnderAgeError(Exception):
    """Raised when voter age is below 18."""
    pass

def register_voter(age):
    if age < 18:
        raise UnderAgeError(age)
    print(f"Voter registered (age {age})")

def main():
    for age in (16, 21):
        try:
            register_voter(age)
        except UnderAgeError as e:
            print(f"पंजीकरण नहीं / Registration denied — age {e} is under 18")

main()
```

**Program 2 — `InvalidRollError` with roll stored**

```python
class InvalidRollError(Exception):
    def __init__(self, roll, message="Roll not found"):
        self.roll = roll
        super().__init__(f"{message}: {roll}")

def find_student(roll, db):
    if roll not in db:
        raise InvalidRollError(roll)
    return db[roll]

db = {101: "Anita", 102: "Ravi"}
for roll in (101, 999):
    try:
        print(find_student(roll, db))
    except InvalidRollError as e:
        print("Error:", e, "| roll attr:", e.roll)
```

### 6. Common built-in exceptions

| Exception | Typical cause |
|-----------|---------------|
| `ValueError` | Wrong value (`int("abc")`) |
| `TypeError` | Wrong type operation |
| `IndexError` | Invalid list index |
| `KeyError` | Missing dict key |
| `FileNotFoundError` | File missing |
| `ZeroDivisionError` | `/` or `//` by zero |
| `AttributeError` | Missing attribute/method |
| `ImportError` / `ModuleNotFoundError` | Import failure |

**Try these (2 programs):**

**Program 1 — Three built-ins, three handlers**

```python
try:
    print([10, 20, 30][5])
except IndexError as e:
    print("IndexError:", e)

try:
    print({"a": 1}["b"])
except KeyError as e:
    print("KeyError:", e)

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
```

**Program 2 — Name that error quiz**

```python
# Fill answers after running each line inside its own try/except

# Expected: TypeError
try:
    "a" + 1
except Exception as e:
    print(type(e).__name__)

# Expected: IndexError
try:
    [1][5]
except Exception as e:
    print(type(e).__name__)

# Expected: KeyError
try:
    {}["missing"]
except Exception as e:
    print(type(e).__name__)

# Expected: ZeroDivisionError
try:
    1 // 0
except Exception as e:
    print(type(e).__name__)

# Expected: ValueError
try:
    int("hello")
except Exception as e:
    print(type(e).__name__)
```

---

## Step-by-Step Annotated Python 3 Code

### Example 1 — Safe user input loop

```python
def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Number must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

age = read_positive_int("Enter your age: ")
print("Valid age:", age)
```

### Example 2 — Full try/except/else/finally

```python
def read_config(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Config {path} not found.")
        return {}
    else:
        return {"content": content}
    finally:
        print("Cleanup complete")
```

### Example 3 — raise with validation

```python
def validate_pan(pan):
    """Indian PAN format: ABCDE1234F (simplified check)."""
    if pan is None or len(pan) != 10:
        raise ValueError("PAN must be 10 characters")
    if not pan[:5].isalpha() or not pan[5:9].isdigit() or not pan[9].isalpha():
        raise ValueError("Invalid PAN format")
    return pan.upper()

try:
    validate_pan("ABCDE1234F")
    validate_pan("INVALID")
except ValueError as err:
    print("Validation failed:", err)
```

### Example 4 — Custom exception hierarchy

```python
class AppError(Exception):
    """Base for application errors."""
    pass

class PaymentError(AppError):
    pass

class GatewayTimeoutError(PaymentError):
    pass

def process_payment(amount):
    if amount > 100000:
        raise PaymentError("Amount exceeds limit")
    # simulate gateway failure
    raise GatewayTimeoutError("Razorpay timeout")

try:
    process_payment(150000)
except PaymentError as e:
    print("Payment issue:", e)
except AppError as e:
    print("App error:", e)
```

### Example 5 — Re-raising pattern

```python
def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        logging.error("JSON file missing: %s", path)
        raise
```

### Example 6 — Exception in OOP method

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Requested ₹{amount}, available ₹{self.balance}"
            )
        self.balance -= amount
        return self.balance

class InsufficientBalanceError(Exception):
    pass

acct = BankAccount(500)
try:
    acct.withdraw(800)
except InsufficientBalanceError as e:
    print("Transaction failed:", e)
```

---

## Practice Exercises

### Basic

1. Handle `ZeroDivisionError` in calculator.
   **Model answer:**
   ```python
   a = float(input("a: "))
   b = float(input("b: "))
   try:
       print(a / b)
   except ZeroDivisionError:
       print("Cannot divide by zero")
   ```

2. Catch `ValueError` when converting user input to float.
   **Model answer:**
   ```python
   raw = input("Enter a number: ")
   try:
       value = float(raw)
       print("OK:", value)
   except ValueError:
       print("Not a valid number")
   ```

3. Use `try/except` when accessing dict key — prefer `.get()` too.
   **Model answer:**
   ```python
   data = {"name": "Priya"}
   try:
       print(data["email"])
   except KeyError:
       print("email missing")

   print(data.get("email", "email missing"))  # preferred
   ```

### Intermediate

1. Write `safe_divide(a, b)` returning `None` on error instead of crashing.
   **Model answer:**
   ```python
   def safe_divide(a, b):
       try:
           return a / b
       except (ZeroDivisionError, TypeError):
           return None
   ```

2. Create `InvalidEmailError` and validator function.
   **Model answer:**
   ```python
   class InvalidEmailError(ValueError):
       pass

   def validate_email(email):
       if "@" not in email or "." not in email.split("@")[-1]:
           raise InvalidEmailError(f"Invalid email: {email}")
       return email
   ```

3. Refactor file reader to use `try/except/else/finally`.
   **Model answer:**
   ```python
   path = "notes.txt"
   f = None
   try:
       f = open(path, encoding="utf-8")
   except FileNotFoundError:
       print("File missing")
   else:
       print(f.read())
   finally:
       if f is not None:
           f.close()
   ```

### Interview-style

1. Difference between `except Exception` and bare `except`?
   **Model answer:**
   `except Exception` catches almost all application errors but not system exits like `KeyboardInterrupt`/`SystemExit`. Bare `except:` catches everything including those, which can hide bugs and block clean shutdown — avoid it.

2. When to create custom exceptions?
   **Model answer:**
   Create them when callers need to distinguish your domain failure (e.g. `InvalidEmailError`) from generic errors and handle it specifically. Prefer a clear hierarchy under `Exception` over overloading `ValueError` for every case.

3. What happens if exception in `finally` block?
   **Model answer:**
   An exception raised in `finally` replaces any pending exception from the `try`/`except` block. The original error is lost unless you explicitly chain or log it before the `finally` raises.

## Mini-Project: Safe Age Input CLI

**Title:** Never crash on bad age  
**Lab kit (build here):** [15_Lab_Assets/18_safe_input_exceptions/](../15_Lab_Assets/18_safe_input_exceptions/)

### What to build

| Feature | Detail |
|---------|--------|
| `InvalidAgeError` | Custom exception for age outside 1–120 |
| `read_age(raw)` | `int` conversion; raise `ValueError` on non-int; raise `InvalidAgeError` on range |
| Demo loop | Test `"21"`, `"abc"`, `"0"`, `"200"` without a traceback for expected cases |
| Clear messages | Print exception type + message |

**Sample:**

```
21 -> 21
abc ValueError age must be an integer
0 InvalidAgeError age out of range: 0
200 InvalidAgeError age out of range: 200
```

### Stretch

- Wrap `read_age` in a `while True` prompt until a valid age is entered.  
- Add `read_positive_float` for amounts (reuse the same pattern).  
- Log failures with a timestamp (`datetime.now()`) before File Handling module.

### Done when

- [ ] Lab kit `safe_age` ticket passes for the four samples  
- [ ] Custom `InvalidAgeError` is raised for out-of-range ages  
- [ ] Non-numeric input raises / is caught as `ValueError` (no crash)  
- [ ] Repo pushed with a short README of sample outputs  

---

## Revision Map — Memorize / Understand / Practise / Build

| Topic | Memorize | Understand | Practise | Build |
|-------|----------|------------|----------|-------|
| try/except | Syntax blocks | Flow when error occurs | Fix 5 broken scripts | Safe input reader |
| Exception types | Common 6–8 names | When each is raised | Match except to error | Typed handlers |
| else/finally | When each runs | Cleanup vs success path | Predict output quizzes | Resource cleanup |
| raise | `raise ValueError("msg")` | Fail fast principle | Validation guards | Custom error triggers |
| Custom exceptions | `class MyError(Exception)` | Domain-specific errors | Payment errors | App error hierarchy |
| Best practices | Don't bare `except:` | Log and re-raise patterns | Code review exercise | Robust file reader |

---

## Interview & Discussion Q&A

### Discuss in class

1. Should you use exceptions for normal control flow (e.g., end of loop)?
2. How does Django return HTTP 404 vs 500 related to exceptions?
3. Why log before re-raising?
4. Difference between error and exception in everyday language vs Python?
5. How would you handle errors in a payment API integration?

*No memorized script — push for plain-English answers, then continue to interview Qs below.*

### Interview answers

**Q1. try/except/else/finally execution order?**  
**A:** Run try; on exception matching except, run that handler (skip else); else runs only if no exception; finally always runs (cleanup).

**Q2. Checked vs unchecked exceptions in Python?**  
**A:** Python doesn't have Java-style checked exceptions; all exceptions are unchecked — not required to declare throws.

**Q3. When create custom exception?**  
**A:** When domain needs specific error types callers can catch separately (`SeatNotAvailableError` vs generic `Exception`).

**Q4. EAFP vs LBYL?**  
**A:** EAFP: try operation, handle failure. LBYL: Look Before You Leap — check conditions first. Python culture favors EAFP for many I/O cases.

**Q5. Exception vs assert?**  
**A:** `assert` for developer sanity checks (can be disabled with `-O`); exceptions for runtime errors and user-facing failures.

---

