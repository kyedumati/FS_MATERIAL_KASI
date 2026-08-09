# Module 01 — Functions, Decorators & Generators

**Phase:** Advanced Python

**Previous module:** Data Structures Overview
**Next module:** Modules and Packages

---

## Learning Outcomes

By the end of this session, learners will be able to:

1. Define and call functions with parameters, default values, and return values.
2. Explain variable scope (local, global, LEGB rule) and use `*args` / `**kwargs`.
3. Write one-line functions using `lambda` where appropriate.
4. Use `map`, `filter`, and `functools.reduce` (and know when a comprehension is clearer).
5. Build and apply simple decorators (timing, login check).
6. Write generator functions with `yield`, use `next()`, and explain exhaustion vs lists.
7. Write generator expressions and stream in-memory rows one at a time (CSV files come in Files week).
8. Refactor repetitive scripts into reusable utility functions.

---

## Classroom Ticket

Open the lab kit **before** long notes. Read the ticket → code in `starter/` or fix `broken/`.

- **[Refactor ATM into functions](../15_Lab_Assets/13_function_refactor/)** (S28)
- **[Login-gate decorator](../15_Lab_Assets/14_decorator_login_gate/)** (S30)
- **[Ship](../15_Lab_Assets/30_ksr_utils_toolkit/)** `ksr_utils` **[toolkit](../15_Lab_Assets/30_ksr_utils_toolkit/)** (homework — **no generators**)
- **[Stream CSV with yield](../15_Lab_Assets/15_generator_csv_stream/)** (S31 — after functions homework)

Finish the ticket in class; compare with the official solution only when your trainer says so.

### Motivation — Feel the pain of copy-paste

Look at this ATM-style script. The same `amount <= 0` check appears in every action:

```python
balance = 1000.0

# --- deposit ---
amount = 200.0
if amount <= 0:
    print("Invalid amount")
else:
    balance = balance + amount
    print("Deposited. Balance:", balance)

# --- withdraw ---
amount = 150.0
if amount <= 0:
    print("Invalid amount")
else:
    if amount > balance:
        print("Insufficient funds")
    else:
        balance = balance - amount
        print("Withdrawn. Balance:", balance)

# --- another deposit (copy-paste again) ---
amount = -50.0
if amount <= 0:
    print("Invalid amount")
else:
    balance = balance + amount
    print("Deposited. Balance:", balance)
```

Problems with this style:

1. The same validation is written **three times**.
2. Changing the message to `"Amount must be positive"` means editing **every** copy.
3. Miss one copy → one path keeps the old behaviour (a silent bug).

**Visual — same logic, three copies (the bug factory):**

```mermaid
flowchart TB
  subgraph Pain["Without a function"]
    D1["deposit block<br/>if amount <= 0 ..."]
    W1["withdraw block<br/>if amount <= 0 ..."]
    D2["another deposit<br/>if amount <= 0 ..."]
  end
  Bug["Change message / rule"] --> D1
  Bug --> W1
  Bug -.->|easy to miss| Missed["D2 still old — silent bug"]
```

Write the check **once**, then reuse it:

```python
def is_positive(amount):
    if amount <= 0:
        print("Invalid amount")
        return False
    return True

balance = 1000.0

if is_positive(200.0):
    balance = balance + 200.0

if is_positive(-50.0):
    balance = balance + (-50.0)  # never runs — guard stopped us
```

**Visual — write once, call many times:**

```mermaid
flowchart LR
  Def["def is_positive(amount)"] --> C1["call for deposit"]
  Def --> C2["call for withdraw"]
  Def --> C3["call for transfer"]
  Fix["Fix the rule in ONE place"] --> Def
  C1 --> Same["Same behaviour everywhere"]
  C2 --> Same
  C3 --> Same
```

That named unit is a **function**. Your Classroom Ticket ([Refactor ATM into functions](../15_Lab_Assets/13_function_refactor/)) is the same idea at ATM scale.

### What is a function?

If a group of statements is needed again and again, do **not** copy-paste them. Bundle those statements into **one named unit**, then **call** that unit whenever you need it. That unit is a **function**.

Kitchen analogy: instead of rewriting “boil water → noodles → masala” every time, you write the recipe once (`def make_maggi(...)`) and call it when hungry.

**Visual — recipe once, cook many times:**

```mermaid
flowchart LR
  R["def make_maggi(...)"] --> H1["hungry at 1 pm"]
  R --> H2["hungry at 8 pm"]
  R --> H3["friend visits"]
```

In other languages the same idea may be called a *method*, *procedure*, or *subroutine*. In Python we mostly say **function** (and later **method** when it lives on a class).

### Why do we need functions?

| Without functions                        | With functions                               |
| ---------------------------------------- | -------------------------------------------- |
| Same validation copied in 5 places       | One `is_valid_email()` reused everywhere     |
| Bug fixed in one place, missed in others | Fix once — every call benefits               |
| 400-line script hard to read             | Named steps: `load()`, `process()`, `save()` |

**Main advantage: code reusability** — write once, call many times. Secondary wins: clearer names, easier testing, and smaller pieces you can put in modules later.

### Two kinds of functions in Python

1. **Built-in (predefined)** — already available with Python: `print()`, `len()`, `type()`, `input()`, `int()`, `sum()`, …
2. **User-defined** — you write them for your project: `calculate_bill()`, `wish()`, `withdraw()`.

**Visual — you already call built-ins; now you create your own:**

```mermaid
flowchart TB
  subgraph BuiltIn["Built-in (Python gives you)"]
    P["print / len / sum / ..."]
  end
  subgraph UserDef["User-defined (you write)"]
    U["def calculate_bill(...)<br/>def withdraw(...)"]
  end
  BuiltIn --> Use["You call them"]
  UserDef --> Use
```

You already *use* built-ins. This module teaches you to *create* user-defined ones, then stretch into decorators and generators.

### Parameter vs argument (words interviewers mix up)

- **Parameter** — placeholder name in the definition: `def wish(name):`
- **Argument** — real value you pass when calling: `wish("Priya")`

Recipe placeholders vs the ingredients you actually put in the bowl.

**Visual — definition vs call:**

```mermaid
flowchart LR
  Def["def wish(name):<br/>← parameter (placeholder)"]
  Call["wish('Priya')<br/>← argument (real value)"]
  Call -->|fills| Def
```

### 1. Creating a user-defined function (`def` and `return`)

**What:** A named block that runs when called.  
**Why:** So you can reuse logic and give that logic a clear name.

Two keywords matter:

1. `def` — **mandatory** — starts the definition
2. `return` — **optional** — sends a result back to the caller (if omitted, Python returns `None`)

**Visual — call → run body → return to caller:**

```mermaid
sequenceDiagram
  participant Main as Your script
  participant F as greet(name)
  Main->>F: greet("Priya")
  F->>F: build message
  F-->>Main: return "Hello, Priya!"
  Main->>Main: result = that value
```

```python
def wish():
    """Print a greeting. No inputs, no return value."""
    print("Hello Good Morning")

wish()
wish()  # call as many times as you need — no rewrite
```

With an input (parameter) and a returned result:

```python
def greet(name):          # name is a parameter
    message = f"Hello, {name}!"
    return message        # sends value back to caller

result = greet("Priya")   # "Priya" is the argument
print(result)             # Hello, Priya!
```

**Rules people often forget:**

- `return` exits the function immediately (code after it does not run).
- No `return` → the call evaluates to `None` (easy to miss when you `print(f())`).
- Python can return **multiple values** as a tuple: `return sum, diff` then `x, y = sum_sub(10, 5)`.

**Try these (2 programs):**

**Program 1 — Celsius to Fahrenheit**

```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

for temp in (0, 37, 100):
    print(f"{temp}°C → {celsius_to_fahrenheit(temp)}°F")
```

**Program 2 — Even or Odd**

```python
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_odd(10))  # Even
print(even_odd(15))  # Odd
```

### 2. Types of arguments (what / why, then syntax)

When you write `def sub(a, b):` and call `sub(100, 200)`, `a`/`b` are **formal** parameters and `100`/`200` are **actual** arguments.

Python allows four common ways to pass arguments. Understand **why** each exists before memorizing the table.

**Visual — four ways to fill the same recipe:**

```mermaid
flowchart TB
  F["def f(a, b=10, *args, **kwargs)"]
  F --> Pos["Positional: f(1, 2)"]
  F --> Key["Keyword: f(b=2, a=1)"]
  F --> Def["Default: f(1) → b stays 10"]
  F --> Var["Variable: f(1, 2, 3, x=9)<br/>*args / **kwargs catch extras"]
```

#### 2a. Positional arguments

**What:** Values match parameters **by order**.  
**Why:** Simple and short for small APIs.  
**Caution:** Swap order → wrong result (`sub(100, 200)` ≠ `sub(200, 100)`). Count must match.

```python
def sub(a, b):
    return a - b

print(sub(100, 200))  # -100
print(sub(200, 100))  # 100
```

#### 2b. Keyword arguments

**What:** Pass by **parameter name**: `wish(name="Ravi", msg="Hi")`.  
**Why:** Order no longer matters; calls stay readable when there are many options.  
**Rule:** After a keyword argument, you cannot put a bare positional one.

```python
def wish(name, msg):
    print(f"Hello {name}, {msg}")

wish(name="Ravi", msg="Good Morning")
wish(msg="Good Morning", name="Ravi")  # same result
# wish(name="Ravi", "Good Morning")  # SyntaxError
```

#### 2c. Default arguments

**What:** A parameter already has a value if the caller skips it.  
**Why:** Optional behaviour without writing two functions (`wish("Ravi")` and `wish()`).  
**Rule:** Non-default parameters must come **before** defaults (`def wish(name="Guest", msg):` is invalid).

```python
def wish(name="Guest"):
    print(f"Hello {name}, Good Morning")

wish("Ravi")
wish()  # uses "Guest"
```

#### 2d. Variable-length arguments (`*args`, `**kwargs`)

**What:** Accept **any number** of positional (`*args` → tuple) or keyword (`**kwargs` → dict) values.  
**Why:** Helpers like `sum_all(...)`, flexible loggers, and wrappers that forward arguments.  
**Rule (definition order):** required positional → `*args` → keyword-only → `**kwargs`.

**Visual — packing extras into a bag:**

```mermaid
flowchart LR
  Call["build_profile('Arjun', 'Python', 'SQL', city='Hyd')"]
  Call --> Name["name = 'Arjun'"]
  Call --> Args["*skills → ('Python', 'SQL')"]
  Call --> Kw["**meta → {city: 'Hyd'}"]
```

```python
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all())           # 0
print(sum_all(10, 20, 30)) # 60

def build_profile(name, *skills, **meta):
    return {"name": name, "skills": list(skills), **meta}

print(build_profile("Arjun", "Python", "SQL", city="Hyderabad"))
```

**Quick reference (after you understand the why):**

| Type       | Syntax            | Use when                           |
| ---------- | ----------------- | ---------------------------------- |
| Positional | `f(a, b)`         | Few args; order is obvious         |
| Keyword    | `f(b=5, a=2)`     | Clarity / optional skip of order   |
| Default    | `def f(a, b=10)`  | Sensible optional value            |
| `*args`    | `def f(*args)`    | Unknown count of positional values |
| `**kwargs` | `def f(**kwargs)` | Unknown named options              |

**Try these (2 programs):**

**Program 1 — Default + keyword arguments**

```python
def greet(name, msg="Good Morning"):
    print(f"Hello {name}, {msg}")

greet("Priya")
greet(name="Ravi", msg="Good Evening")
```

**Program 2 —** `*args` **with tax**

```python
def total(*amounts, tax_rate=0.05):
    subtotal = sum(amounts)
    return round(subtotal * (1 + tax_rate), 2)

print(total(100, 200, 50))  # 367.5
```

### 3. Scope — local vs global (and LEGB)

**What:** Where a name is visible.  
**Why:** Without scope rules, every variable would collide; with them, functions stay self-contained.

- **Global** — declared outside functions; readable from functions in that module.
- **Local** — declared inside a function; invisible outside.

Python looks up names in this order (**LEGB**): **L**ocal → **E**nclosing (nested `def`) → **G**lobal → **B**uilt-in (`len`, `print`, …).

**Visual — name lookup stops at the first hit:**

```mermaid
flowchart TD
  Need["Need name: tax_rate"] --> L{Found in Local?}
  L -->|Yes| UseL[Use local]
  L -->|No| E{Found in Enclosing?}
  E -->|Yes| UseE[Use enclosing]
  E -->|No| G{Found in Global?}
  G -->|Yes| UseG[Use global]
  G -->|No| B{Found in Built-in?}
  B -->|Yes| UseB["Use len / print / ..."]
  B -->|No| Err[NameError]
```

```python
tax_rate = 0.18  # global

def calculate_total(amount):
    tax = amount * tax_rate   # read global OK
    return amount + tax
```

Use `global x` only when you must **reassign** a global name. Prefer passing values in and returning results — globals make bugs hard to find in real projects.

**Try these (2 programs):**

**Program 1 — Fix counter with return (prefer this over** `global`**)**

```python
count = 0

def bump(n):
    return n + 1

count = bump(count)
print(count)  # 1
```

**Program 2 — Closure counter (no globals)**

```python
def make_counter():
    n = 0

    def next_count():
        nonlocal n
        n += 1
        return n

    return next_count

c = make_counter()
print(c())  # 1
print(c())  # 2
```

### 4. Lambda (anonymous) functions

**What:** A tiny function **without a** `def` **name**, written as `lambda args: expression`.  
**Why:** Instant one-off use — especially as the `key=` for `sorted`, or with `map`/`filter`.  
**When not to:** Multi-step logic, docstrings, or anything you will reuse and test — use `def`.

```python
square = lambda n: n * n
print(square(5))  # 25

names = ["Meera", "Ravi", "An"]
print(sorted(names, key=lambda x: len(x)))
```

Lambda **returns** the expression result automatically — no `return` keyword.

**Try these (2 programs):**

**Program 1 — Sort names by length**

```python
names = ["Meera", "Ravi", "An"]
print(sorted(names, key=lambda x: len(x)))  # ['An', 'Ravi', 'Meera']
```

**Program 2 — Sort marks descending**

```python
marks = [("A", 88), ("B", 95), ("C", 70)]
print(sorted(marks, key=lambda row: row[1], reverse=True))
# [('B', 95), ('A', 88), ('C', 70)]
```

### 5. `map`, `filter`, and `reduce`

**What:** Built-in helpers that apply a function across an iterable.  
**Why:** Short pipelines for “transform every item”, “keep matching items”, or “fold many values into one” — often with `lambda` or a small `def`.

**Visual — three jobs on a list of numbers:**

```mermaid
flowchart LR
  Data["prices / marks"] --> Map["map — transform each"]
  Data --> Filter["filter — keep some"]
  Data --> Reduce["reduce — fold to one"]
  Map --> Out1["new sequence"]
  Filter --> Out2["shorter sequence"]
  Reduce --> Out3["single value"]
```

| Tool                        | Idea                          | Campus example           |
| --------------------------- | ----------------------------- | ------------------------ |
| `map(fn, data)`             | Transform each item           | Prices → prices with GST |
| `filter(fn, data)`          | Keep items where `fn` is true | Marks ≥ 75 only          |
| `reduce(fn, data[, start])` | Combine into one value        | Sum / max of expenses    |

`map` and `filter` return **lazy iterators** in Python 3 — wrap with `list(...)` when you need a list. Prefer a **list comprehension** when it reads clearer; still learn these for interviews and older codebases.

```python
from functools import reduce

prices = [100, 250, 80]
with_gst = list(map(lambda p: round(p * 1.05, 2), prices))
print(with_gst)  # [105.0, 262.5, 84.0]

marks = [45, 78, 92, 61, 88]
passed = list(filter(lambda m: m >= 75, marks))
print(passed)  # [78, 92, 88]

total = reduce(lambda acc, x: acc + x, prices, 0)
print(total)  # 430
```

**Same ideas with comprehensions (often clearer):**

```python
with_gst = [round(p * 1.05, 2) for p in prices]
passed = [m for m in marks if m >= 75]
```

**Rules:**

- `map`/`filter` need a **function** (named or `lambda`) that takes one item (or more if you pass several iterables to `map`).
- `reduce` lives in `functools` (not a built-in). The function takes **(accumulator, next_item)**.
- Do not force `reduce` for a simple sum — `sum(prices)` is better. Use `reduce` when the fold is custom (e.g. merge dicts, running max with a twist).

**Try these (2 programs):**

**Program 1 —** `map` **+** `filter` **on canteen prices**

```python
prices = [40, 25, 60, 15, 120]
with_gst = list(map(lambda p: round(p * 1.05, 2), prices))
big = list(filter(lambda p: p >= 50, with_gst))
print(with_gst)
print(big)
```

**Program 2 —** `reduce` **for bill total (and contrast with** `sum`**)**

```python
from functools import reduce

bill = [40, 25, 60]
total = reduce(lambda acc, x: acc + x, bill, 0)
print(total)       # 125
print(sum(bill))   # same — prefer sum for plain addition
```

### 6. Decorators

**What:** A function that takes another function and returns a **wrapped** version (extra behaviour before/after).  
**Why:** Cross-cutting concerns — timing, login checks, retries — without copy-pasting into every function.

**Visual —** `@timer` **wraps your function like gift wrap:**

```mermaid
flowchart LR
  Call[You call greet] --> Wrap[timer wrapper]
  Wrap --> Inner[original greet runs]
  Inner --> Wrap
  Wrap --> Out[return result + print time]
```

```python
def timer(func):
    def wrapper(*args, **kwargs):
        # before logic
        result = func(*args, **kwargs)
        # after logic
        return result
    return wrapper

@timer
def slow_task():
    ...
```

`@timer` above `def slow_task` means: `slow_task = timer(slow_task)`.

**Try these (2 programs):**

**Program 1 —** `@shout` **decorator**

```python
def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"hello, {name}"

print(greet("Priya"))  # HELLO, PRIYA
```

**Program 2 —** `@require_login` **gate**

```python
current_user = None

def require_login(func):
    def wrapper(*args, **kwargs):
        if current_user is None:
            print("Access denied — please log in")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_dashboard():
    return f"Welcome, {current_user}"

print(view_dashboard())   # Access denied
current_user = "Ravi"
print(view_dashboard())   # Welcome, Ravi
```

### 7. Generators (S31 focus)

**Calendar:** Session 31 — Generators vs lists.  
**Lab kit:** [15_generator_csv_stream](../15_Lab_Assets/15_generator_csv_stream/) (in-memory `yield` now; real CSV after Files week).

#### 7a. List vs generator (What / Why + table)

**What:** A **generator** is an iterator that produces values **lazily** — one at a time — using `yield` inside a function, or a **generator expression** `(… for … in …)`.

**Why:** A list of lakhs of rows holds everything in RAM at once. A generator holds **only the current value** (plus a little state). Use it for streams, large reports, and “process then forget” pipelines.

Kitchen analogy: a list is the whole buffet on the table; a generator is a waiter who brings **one dish at a time**.

**Visual — RAM picture (buffet vs waiter):**

```mermaid
flowchart TB
  subgraph ListWay["List — eager"]
    L1["row1"] --- L2["row2"] --- L3["row3"] --- Ln["... lakh rows"]
    RAM1["All in memory at once"]
  end
  subgraph GenWay["Generator — lazy"]
    Only["only current row"]
    Wait["next() / for → next row"]
    Only --> Wait
  end
```

|            | List / list comprehension   | Generator / `yield`                  |
| ---------- | --------------------------- | ------------------------------------ |
| When built | Immediately (eager)         | On demand (lazy)                     |
| Memory     | All items                   | One item at a time                   |
| Syntax     | `[x*2 for x in range(n)]`   | `(x*2 for x in range(n))` or `yield` |
| Reusable   | Yes — walk it many times    | **Exhausted** after one full pass    |
| Indexing   | `data[0]` works             | `gen[0]` fails — use `next` / `for`  |
| Best for   | Small/medium data you reuse | Large streams, one-pass processing   |

```python
# Eager — builds the whole list in memory first
squares_list = [x * x for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Lazy — nothing computed until you iterate
squares_gen = (x * x for x in range(5))
print(squares_gen)          # <generator object ...>
print(list(squares_gen))    # [0, 1, 4, 9, 16] — now exhausted
```

**Note:**

- Calling a generator function does **not** run the body yet — it returns a generator object. Values appear only when you iterate or call `next()`.

#### 7b. `yield` vs `return`

|                    | `return`              | `yield`                                 |
| ------------------ | --------------------- | --------------------------------------- |
| Ends the function? | Yes (exits)           | Pauses — resumes on next request        |
| Gives back         | One value (or `None`) | One value **per pause**; many over time |
| After call         | Function is done      | Generator object keeps state            |

**Visual — `return` exits; `yield` pauses and resumes:**

```mermaid
sequenceDiagram
  participant Caller
  participant Gen as squares(n)
  Caller->>Gen: next / for
  Gen-->>Caller: yield 0 (paused)
  Caller->>Gen: next / for
  Gen-->>Caller: yield 1 (paused)
  Caller->>Gen: next / for
  Gen-->>Caller: yield 4 (paused)
  Note over Gen: state remembered between yields
```

```python
def one_square(n):
    return n * n          # function ends here

def squares(n):
    for x in range(n):
        yield x * x       # pause; resume for next x
```

#### 7c. `next()`, loops, and exhaustion

**Visual — one pass empties the generator:**

```mermaid
flowchart LR
  Fresh["g = countdown(3)"] --> N1["next → 3"]
  N1 --> N2["next → 2"]
  N2 --> N3["next → 1"]
  N3 --> Empty["exhausted<br/>next → StopIteration"]
  Empty -.->|need again| New["call countdown(3) again"]
```

```python
def countdown(n):
    while n >= 1:
        yield n
        n -= 1

g = countdown(3)
print(next(g))  # 3
print(next(g))  # 2
print(next(g))  # 1
# print(next(g))  # StopIteration — generator is exhausted

# Prefer a for-loop in real code (handles StopIteration for you)
for value in countdown(3):
    print(value, end=" ")  # 3 2 1
print()

# One full pass — then empty
g2 = countdown(2)
print(list(g2))  # [2, 1]
print(list(g2))  # []  — already exhausted; create a new generator if you need another pass
```

**Note:**

- Do not index a generator like a list (`gen[0]` fails). Use `next(gen)` or a `for` loop.
- After one full `for` / `list(gen)`, the generator is empty. Call the function again to get a fresh generator.

**Try these (2 programs):**

**Program 1 — Countdown with** `next`

```python
def countdown(n):
    while n >= 1:
        yield n
        n -= 1

g = countdown(5)
print(next(g), next(g), next(g))  # 5 4 3
for value in g:
    print(value, end=" ")  # 2 1 — remaining values only
print()
```

**Program 2 — Even number stream**

```python
def even_stream(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

print(list(even_stream(10)))  # [0, 2, 4, 6, 8, 10]
```

#### 7d. Generator expressions + when to use which

Same idea as a list comprehension, but with **parentheses** — lazy, not a list.

```python
marks = [45, 78, 92, 33, 88]
# List — all at once
passed_list = [m for m in marks if m >= 40]
# Generator — one at a time
passed_gen = (m for m in marks if m >= 40)

print(sum(passed_gen))   # 303 — consumes the generator
# print(sum(passed_gen))  # 0 — already exhausted
```

**When to use which:**

- Need the full collection, reuse, or indexing → **list** comprehension.
- One-pass filter/transform (especially large) → **generator** expression or `yield` function.

**Try these (2 programs):**

**Program 1 — GST with a generator expression**

```python
prices = [40, 25, 60, 15, 120]
with_gst = (round(p * 1.05, 2) for p in prices)
for p in with_gst:
    print(p)
```

**Program 2 — First failing mark (stop early)**

```python
marks = [80, 72, 35, 90, 28]

def failing(marks, cutoff=40):
    for m in marks:
        if m < cutoff:
            yield m

first = next(failing(marks), None)  # default None if none fail
print(first)  # 35 — did not need to scan the whole list into memory first
```

#### 7e. Row-stream lab pattern + Done when

In class / homework for S31: yield **dict rows from an in-memory list**. Opening CSV files comes in **Files week** (Stretch on the same lab kit).

```python
SAMPLE_ROWS = [
    {"name": "Anita", "city": "Hyderabad"},
    {"name": "Ravi", "city": "Chennai"},
    {"name": "Priya", "city": "Bengaluru"},
]

def iter_rows(rows):
    for row in rows:
        yield row

for i, row in enumerate(iter_rows(SAMPLE_ROWS)):
    print(row)
    if i >= 1:
        break  # stop early — remaining rows never forced into a big result list
```

**Lab Done when (S31):** [15_generator_csv_stream](../15_Lab_Assets/15_generator_csv_stream/)

- [ ] `iter_rows` uses `yield` (not `return` of a full list)
- [ ] Printing a few rows works without building an extra result list first
- [ ] You can explain: call → generator object → `next` / `for` → exhaustion

**Stretch after Files week:** `yield` from `csv.DictReader` on `seed/large_sample.csv`.

---

## Step-by-Step Annotated Python 3 Code

### Example 1 — Basic function with default and return

```python
# file: utils_math.py

def calculate_bill(units, rate_per_unit=8.5, fixed_charge=50):
    """
    Calculate electricity bill.
    units: int — consumption
    rate_per_unit: float — default 8.5 INR
    fixed_charge: flat fee added every month
    """
    if units < 0:
        return None  # invalid input guard
    variable_cost = units * rate_per_unit
    total = variable_cost + fixed_charge
    return round(total, 2)

# Call with positional args
print(calculate_bill(120))           # uses default rate

# Call with keyword args (order flexible)
print(calculate_bill(units=200, rate_per_unit=10))
```

### Example 2 — *args and **kwargs

```python
def build_profile(name, *skills, **meta):
    """
    name: required positional
    *skills: tuple of extra positional args (Java, Python, ...)
    **meta: dict of keyword extras (city=..., experience=...)
    """
    profile = {"name": name, "skills": list(skills)}
    profile.update(meta)
    return profile

p = build_profile("Arjun", "Python", "SQL", city="Hyderabad", experience=2)
print(p)
# {'name': 'Arjun', 'skills': ['Python', 'SQL'], 'city': 'Hyderabad', 'experience': 2}
```

### Example 3 — Scope demonstration

```python
counter = 0  # global

def increment():
    global counter   # needed because we ASSIGN to counter
    counter += 1
    return counter

print(increment())  # 1
print(increment())  # 2
```

### Example 4 — Lambda with sorted

```python
students = [
    {"name": "Meera", "score": 78},
    {"name": "Ravi", "score": 92},
    {"name": "Anita", "score": 85},
]

# Sort by score descending
ranked = sorted(students, key=lambda s: s["score"], reverse=True)
for s in ranked:
    print(s["name"], s["score"])
```

### Example 5 — `map` / `filter` / `reduce`

```python
from functools import reduce

marks = [55, 72, 91, 40, 88]
graded = list(map(lambda m: "Pass" if m >= 35 else "Fail", marks))
toppers = list(filter(lambda m: m >= 90, marks))
highest = reduce(lambda a, b: a if a > b else b, marks)
print(graded)
print(toppers)   # [91]
print(highest)   # 91
```

### Example 6 — Timing decorator

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__}: {time.perf_counter()-start:.4f}s")
        return result
    return wrapper

@timing_decorator
def fetch_data():
    time.sleep(0.5)
    return ["row1", "row2"]
```

### Example 7 — Login decorator

```python
logged_in_user = None

def require_login(func):
    def wrapper(*args, **kwargs):
        if logged_in_user is None:
            print("Access denied. Please login first.")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_salary():
    print(f"Salary slip for {logged_in_user}")
```

### Example 8 — Generator vs list (memory idea)

```python
def squares_list(n):
    result = []
    for x in range(n):
        result.append(x * x)
    return result  # whole list exists at once

def squares_gen(n):
    for x in range(n):
        yield x * x   # one value at a time

print(squares_list(5))           # [0, 1, 4, 9, 16]
print(list(squares_gen(5)))      # same values, different delivery

g = squares_gen(3)
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
```

### Example 9 — Generator expression + row stream

```python
names = ["Ravi", "Ananya", "Om", "Priya"]
long_names = (n for n in names if len(n) >= 5)
print(list(long_names))  # ['Ananya', 'Priya']

rows = [
    {"sku": "TEA", "qty": 2},
    {"sku": "SAMOSA", "qty": 1},
]

def read_rows(rows):
    for row in rows:
        yield row

for row in read_rows(rows):
    print(row["sku"], row["qty"])
```

---

## Practice Exercises

### Basic

1. Write `celsius_to_fahrenheit(c)` returning `F = C * 9/5 + 32`.
  **Model answer:**
2. Write `full_name(first, last, middle="")` returning formatted name.
  **Model answer:**
3. Write `sum_all(*numbers)` returning sum of any count of numbers.
  **Model answer:**
4. Predict the output of these three scope snippets (use LEGB: Local → Enclosing → Global → Built-in):

```python
# Snippet A
x = 10
def show():
    print(x)
show()
```

```python
# Snippet B
x = 10
def bump():
    x = x + 1
    print(x)
bump()
```

```python
# Snippet C
x = 10
def bump():
    global x
    x = x + 1
    print(x)
bump()
print(x)
```

  **Model answer:**
   A prints `10` (reads global). B raises `UnboundLocalError` (assignment makes `x` local, so the read on the right fails). C prints `11` then `11` (`global` reassigns the module name).
5. Use `map` to add 5% GST to `[100, 200, 50]` and `filter` to keep totals ≥ 150.
  **Model answer:**
6. Write generator `countdown(n)` that yields `n … 1`. Print with a `for` loop.
  **Model answer:**
7. Using `next` twice on `countdown(5)`, what prints? Then finish with `list` on the same generator object.
  **Model answer:**

### Intermediate

1. Refactor ATM menu into functions: `show_menu()`, `deposit()`, `withdraw()`.
  **Model answer:**
2. Create `@log_calls` decorator printing function name and arguments.
  **Model answer:**
3. Write generator `fibonacci(n)` yielding first `n` Fibonacci numbers.
  **Model answer:**
4. Use `functools.reduce` to find the longest name in `["Ravi", "Ananya", "Om"]`.
  **Model answer:**
5. Write a generator expression for squares of even numbers from `0` to `10` (inclusive). Convert to list once to print.
  **Model answer:**
6. Implement `iter_rows(rows)` with `yield` over an in-memory list of dicts; print only the first two rows (lab pattern).
  **Model answer:**

### Interview-style

1. Write decorator that retries a function up to 3 times on exception.
  **Model answer:**
2. When choose generator over list for 10 million records?
  **Model answer:**
   Prefer a generator when you process records one at a time and do not need random access or the full collection in memory. A list of 10 million rows can exhaust RAM; `yield` streams values lazily and keeps peak memory low.
3. `map`/`filter` vs list comprehension — when prefer each?
  **Model answer:**
   Prefer a comprehension when the transform/condition is short and readability matters (most campus code). Prefer `map`/`filter` when you already have a named function to reuse, or when matching interview/library style. Always know both.
4. What is generator exhaustion? How do you iterate again?
  **Model answer:**
   After one full pass (`for`, `list(gen)`, or enough `next` calls), the generator raises `StopIteration` and yields nothing more. To iterate again, call the generator function (or rebuild the generator expression) to create a **new** generator object.
5. Generator expression vs list comprehension — one concrete difference besides syntax?
  **Model answer:**
   List comprehension is eager and reusable; a generator expression is lazy, memory-light, and single-pass. Example: `sum(x*x for x in range(1_000_000))` never builds a million-element list.

## Mini-Project: Reusable Utility Library

**Title:** `ksr_utils` — Personal Python Toolkit  
**Lab kit (build here):** [15_Lab_Assets/30_ksr_utils_toolkit/](../15_Lab_Assets/30_ksr_utils_toolkit/)  
**Also use:** [14_decorator_login_gate](../15_Lab_Assets/14_decorator_login_gate/), [16_venv_package_bootstrap](../15_Lab_Assets/16_venv_package_bootstrap/)  
**Generators (S31+ only):** [15_generator_csv_stream](../15_Lab_Assets/15_generator_csv_stream/) — not part of this homework

**Homework scope:** functions + lambda/`map`/`filter` + decorators. **No** `yield` **/ generators.**

### What to build

| File            | Functions                                     | Notes                                                           |
| --------------- | --------------------------------------------- | --------------------------------------------------------------- |
| `validators.py` | `is_email`, `is_phone_in`, `is_positive`      | Pure functions; no `print`                                      |
| `formatters.py` | `format_inr`, `format_date(day, month, year)` | ₹ formatting; zero-padded DD-MM-YYYY (no `datetime` module yet) |
| `transforms.py` | `with_gst`, `keep_high`                       | Use `map` and `filter` (wrap with `list(...)`)                  |
| `decorators.py` | `timing`, `require_token`                     | Wrapper functions; `*args` / `**kwargs`                         |
| `__init__.py`   | re-exports                                    | Clean imports: `from ksr_utils import format_inr`               |
| `demo.py`       | smoke test                                    | Prints + one timed call + GST/filter demo                       |

### Stretch

- Add `is_strong_password(s)` (length ≥ 8, has digit).  
- Add `@retry(times=3)` decorator for flaky calls.  
- **After S31:** finish `generators.py` (`read_rows` must `yield`).  
- **Later (Files week):** `yield` rows from a CSV with `csv.DictReader`.  
- Add `README.md` with install/run and 3 import examples.

### Done when

- [ ] Starter kit `demo.py` passes (**without** generators)  
- [ ] `with_gst` / `keep_high` use `map` / `filter`  
- [ ] Package pushed to GitHub  
- [ ] README shows how a teammate imports your helpers  

---

## Revision Map — Memorize / Understand / Practise / Build

| Topic             | Memorize                                | Understand                                    | Practise                          | Build                                |
| ----------------- | --------------------------------------- | --------------------------------------------- | --------------------------------- | ------------------------------------ |
| Function basics   | `def`, `return`, parameter vs argument  | Why functions reduce duplication              | Write 5 utility functions         | String/date helper module            |
| Parameters        | Default args, `*args`, `**kwargs`       | Positional vs keyword binding                 | Variadic function drills          | Flexible logger wrapper              |
| Scope             | `global`, LEGB                          | Why globals are risky                         | Scope prediction exercises        | Refactor global-heavy script         |
| Lambda            | Syntax `lambda x: x*2`                  | When **not** to use lambda                    | Sort with `key=`                  | Mini map/filter demos                |
| map/filter/reduce | `map`, `filter`, `functools.reduce`     | Lazy iterators; when comprehension is clearer | GST map + pass filter             | Bill fold with reduce                |
| Decorators        | `@decorator` syntax                     | Wrapper + closure idea                        | Timing + auth decorators          | Login-gated CLI menu                 |
| Generators (S31)  | `yield`, `next()`, gen expression `(…)` | Lazy vs eager; exhaustion                     | Countdown, fibonacci, `iter_rows` | Yield lab + optional `generators.py` |

**Label legend:** **Memorize** = recall in interviews · **Understand** = explain in English · **Practise** = daily labs · **Build** = portfolio artefacts

---

## Interview & Discussion Q&A

Shared with students after concepts and the mini-project. Use for review and interview prep — questions and model answers are included.

1. Why are functions the building blocks of clean Python code?
2. Can a function return multiple values? How?
3. What happens when you call a generator function? What is exhaustion?
4. Generator expression vs list comprehension — when prefer each?
5. When would you use `map`/`filter` instead of a list comprehension?
6. Why might a login-check decorator be useful before a sensitive function runs?
7. How does `@timing_decorator` relate to production monitoring?

**Q1. What is the difference between** `*args` **and** `**kwargs`**?**  
**A:** `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary. They make functions flexible when the number of inputs varies.

**Q2. Explain decorators in simple terms.**  
**A:** A decorator wraps a function to extend its behavior (logging, timing, auth) without modifying the original function body. Syntax `@dec` applies `func = dec(func)`.

**Q3. Generator vs list comprehension?**  
**A:** List comprehension builds the entire list in memory immediately and is reusable. A generator produces items lazily on demand, which saves memory for large or infinite sequences, but is exhausted after one full pass.

**Q3b. What happens when you call a generator function?**  
**A:** The body does not run yet — you get a generator object. Values appear when you iterate (`for`) or call `next()`. After all values are taken, further `next` raises `StopIteration` (exhaustion); call the function again for a fresh generator.

**Q4. What is a lambda function? When not to use it?**  
**A:** Lambda is an anonymous single-expression function. Avoid it for complex logic, multiple statements, or when readability suffers — use `def` instead.

**Q5. What are** `map`**,** `filter`**, and** `reduce`**?**  
**A:** `map` applies a function to every item; `filter` keeps items where the function is true; `reduce` (from `functools`) folds items into one value. In Python 3, `map`/`filter` are lazy — use `list(...)` when you need a concrete list. Prefer comprehensions/`sum` when clearer.

**Q6. What is variable scope? Explain LEGB.**  
**A:** Scope determines where a name is visible. Python searches Local → Enclosing (nested functions) → Global (module) → Built-in (len, print, etc.).

---

