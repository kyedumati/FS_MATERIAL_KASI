# Module 02 — Modules and Packages

**Phase:** Advanced Python

**Duration:** See [Session Calendar](../00_Course_Guide/11_Session_Calendar_100.md) (1h 15m live sessions).

**Previous module:** Functions Decorators Generators
**Next module:** OOP

---

## Learning Outcomes

By the end of this session, learners will be able to:

1. Explain what a module and package are and why Python uses them.
2. Use all common `import` forms (`import`, `from ... import`, aliases).
3. Work confidently with standard library modules: `math`, `datetime`, `random`, `json`, `os`.
4. Create a multi-file package with `__init__.py` and relative imports.
5. Set up a virtual environment (`venv`) and install packages with `pip`.
6. Structure a small project ready for GitHub and future Django apps.

---

## Classroom Ticket

Open the lab kit **before** long notes. Read the ticket → code in `starter/` or fix `broken/`.

- **[Ship campus_utils package + venv](../15_Lab_Assets/16_venv_package_bootstrap/)**

Finish the ticket in class; compare with the official solution only when your trainer says so.

### What is a module? What is a package?

- A **module** is one Python file (`.py`) that holds related names: variables, functions, classes.  
- A **package** is a **folder** of modules. An `__init__.py` file (even empty) tells Python: “this folder is importable.”

**Function → module → library (big picture):**

| Unit | Plain meaning |
|------|----------------|
| Function | A named group of statements |
| Module | A group of related functions/classes in one `.py` file |
| Package / library | A group of modules (folder or installable project) |

### Why do we need them?

Without modules, one script becomes thousands of lines — hard to read, hard to reuse, impossible to share. Real products (Django, any team codebase) split work across many files. `import` lets you use that work without copy-paste.

**Virtual environment (`venv`)** is a private Python sandbox per project so Project A (Django 5) and Project B (Django 4) do not fight on the same machine. Required on shared lab PCs and for clean deploy.

When you write `import math`, Python loads the standard-library `math` module and exposes its tools. When you `pip install requests`, that package lands in `site-packages` for the active environment.

---

## Important Concepts

### 1. Import forms — what / why, then syntax

**What:** Ways to bring another file’s names into the current file.  
**Why:** Reuse without duplication; keep call sites readable.

```python
import math                          # whole module — use math.sqrt
print(math.sqrt(16))

from math import sqrt, pi            # specific names — shorter calls
print(sqrt(16))

import datetime as dt                 # alias — shorter module name
now = dt.datetime.now()

from os import path as osp           # alias for one imported name
```

**Avoid:** `from math import *` — pollutes the namespace; readers cannot see where a name came from.

**Try these (2 programs):**

**Program 1 — `import` vs `from … import`**

```python
import math
print(math.ceil(4.2))   # 5
print(math.sqrt(81))    # 9.0

from math import ceil, sqrt
print(ceil(4.2))        # 5 — no prefix
print(sqrt(81))         # 9.0
```

**Program 2 — Attendance date header**

```python
import datetime as dt

today = dt.date.today()
print(f"Hyderabad Attendance — {today.strftime('%d-%m-%Y')}")
```

### 2. Module search path

**What:** The ordered list of folders Python checks when you `import`.  
**Why:** Explains `ModuleNotFoundError` and why `venv` / project layout matter.

Python looks in:

1. Current directory  
2. Directories in `PYTHONPATH`  
3. Standard library  
4. `site-packages` (pip installs)

```python
import sys
print(sys.path)  # debugging import errors
```

**Try these (2 programs):**

**Program 1 — Inspect `sys.path`**

```python
import sys
import os

print("sys.path entries:")
for i, entry in enumerate(sys.path):
    tag = ""
    if entry == "" or entry == os.getcwd():
        tag = "  # ← current folder"
    elif "site-packages" in entry.replace("\\", "/"):
        tag = "  # ← site-packages (pip installs)"
    print(f"{i}: {entry!r}{tag}")
```

**Program 2 — Local module import (and ModuleNotFoundError demo)**

```python
# Save as greetings.py (same folder), then run this as main.py
# --- greetings.py ---
# def namaste(name):
#     return f"Namaste, {name}!"

# --- main.py ---
from greetings import namaste

print(namaste("Priya"))  # Namaste, Priya!

# After rename/move greetings.py away and re-run:
# ModuleNotFoundError: No module named 'greetings'
```

### 3. Standard library highlights

**What:** Modules that ship with Python — no `pip` needed.  
**Why:** Prefer these before adding third-party packages for simple tasks.

| Module | Purpose | Common functions |
|--------|---------|------------------|
| `math` | Numeric functions | `sqrt`, `ceil`, `floor`, `pow` |
| `datetime` | Dates and times | `datetime.now()`, `strftime`, `timedelta` |
| `random` | Pseudo-random | `randint`, `choice`, `shuffle` |
| `json` | JSON ↔ Python | `loads`, `dumps`, `load`, `dump` |
| `os` | OS interface | `getcwd`, `listdir`, `path.join`, `environ` |

**Try these (2 programs):**

**Program 1 — Random lunch picker**

```python
import random

spots = ["Canteen", "Mess", "Tiffin centre", "Home"]
print("Today's lunch:", random.choice(spots))
```

**Program 2 — JSON dump and load**

```python
import json

batch = {"city": "Pune", "batch": "PFS-01"}
text = json.dumps(batch)
print("JSON string:", text)

data = json.loads(text)
print("City:", data["city"])  # Pune
```

### 4. Package structure

**What:** A folder of modules you own (e.g. `ksr_utils/`).  
**Why:** Capstone and Django apps both expect this layout.

```
my_project/
├── venv/                 # not committed to Git
├── requirements.txt
├── main.py
└── mypackage/
    ├── __init__.py       # package marker + optional exports
    ├── core.py
    └── helpers/
        ├── __init__.py
        └── strings.py
```

**Try these (2 programs):**

**Program 1 — `format_inr` package (illustrative layout)**

```python
# Folder layout:
#   campus_utils/__init__.py   (can be empty for Program 1)
#   campus_utils/formatters.py
#   main.py

# --- campus_utils/formatters.py ---
def format_inr(n):
    return f"₹{n:,.2f}"

# --- main.py ---
from campus_utils.formatters import format_inr

print(format_inr(1250))  # ₹1,250.00
```

**Program 2 — Re-export from `__init__.py`**

```python
# --- campus_utils/formatters.py ---
def format_inr(n):
    return f"₹{n:,.2f}"

# --- campus_utils/__init__.py ---
from campus_utils.formatters import format_inr

__all__ = ["format_inr"]

# --- main.py ---
from campus_utils import format_inr  # short import via package init

print(format_inr(1250))  # ₹1,250.00
```

### 5. pip and venv workflow

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt
```

**Try these (2 programs):**

**Program 1 — Prove `requests` is installed**

```python
# First (in terminal):
#   python -m venv venv
#   source venv/bin/activate          # Windows: venv\Scripts\activate
#   pip install requests
#   pip freeze > requirements.txt

import importlib.util

spec = importlib.util.find_spec("requests")
print("requests found:", spec is not None)
if spec:
    print("Location:", spec.origin)
```

**Program 2 — GET via `requests` (run inside venv)**

```python
import requests

response = requests.get("https://httpbin.org/get", timeout=10)
print("Status:", response.status_code)
print("URL:", response.json()["url"])
# Deactivate venv first → ModuleNotFoundError: No module named 'requests'
```

---

## Step-by-Step Annotated Python 3 Code

### Example 1 — math module

```python
import math

radius = 7
area = math.pi * math.pow(radius, 2)
print(f"Area: {area:.2f}")

print(math.ceil(4.2))    # 5
print(math.floor(4.9))   # 4
print(math.sqrt(81))     # 9.0
```

### Example 2 — datetime module

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%d-%m-%Y %H:%M"))   # Indian date format common in UIs

# 30 days from today (e.g., subscription expiry)
expiry = now + timedelta(days=30)
print("Expires on:", expiry.date())

# Parse string to datetime
dob = datetime.strptime("15-08-1995", "%d-%m-%Y")
print("Birth year:", dob.year)
```

### Example 3 — random module

```python
import random

# OTP for demo (use secrets module in production)
otp = random.randint(100000, 999999)
print("OTP:", otp)

colors = ["red", "green", "blue"]
print("Lucky color:", random.choice(colors))

nums = [10, 20, 30, 40]
random.shuffle(nums)
print("Shuffled:", nums)
```

### Example 4 — json module

```python
import json

# Python dict → JSON string
user = {"id": 1, "name": "Ananya", "city": "Chennai", "active": True}
json_str = json.dumps(user, indent=2)
print(json_str)

# JSON string → Python dict
parsed = json.loads(json_str)
print(parsed["city"])

# Write/read JSON file
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)
```

### Example 5 — os module

```python
import os

print("Current folder:", os.getcwd())
print("Files here:", os.listdir("."))

# Cross-platform path (important for Windows + Mac labs)
data_path = os.path.join("data", "students.csv")
print("Data path:", data_path)

# Environment variable (used in Django settings later)
db_host = os.environ.get("DB_HOST", "localhost")
print("DB host:", db_host)
```

### Example 6 — Creating and importing your own module

**File: `greetings.py`**

```python
def say_hello(name):
    return f"Namaste, {name}!"

APP_VERSION = "1.0.0"
```

**File: `main.py`**

```python
import greetings

print(greetings.say_hello("KSR Batch"))
print("Version:", greetings.APP_VERSION)
```

### Example 7 — Package with __init__.py

**File: `ksr_tools/__init__.py`**

```python
"""KSR training utility package."""
from .validators import is_email
from .formatters import format_inr

__all__ = ["is_email", "format_inr"]
```

**File: `ksr_tools/validators.py`**

```python
def is_email(text):
    return "@" in text and "." in text.split("@")[-1]
```

**File: `ksr_tools/formatters.py`**

```python
def format_inr(amount):
    return f"₹{amount:,.2f}"
```

**File: `demo.py`**

```python
from ksr_tools import is_email, format_inr

print(is_email("student@ksr.com"))
print(format_inr(125000.5))
```

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Circular imports | ImportError / partial init | Restructure; move shared code to third module |
| Wrong working directory | Module not found | Run from project root or fix `PYTHONPATH` |
| Committing `venv/` | Huge repo, OS-specific paths | Add `venv/` to `.gitignore` |
| `pip install` globally | Version conflicts | Always use venv per project |
| Typo in module name | `ModuleNotFoundError` | Match filename exactly (case-sensitive on Linux) |
| `from package import *` | Namespace pollution | Import explicit names |
| Missing `__init__.py` (older Python) | Package not recognized | Add `__init__.py` in each package folder |

---

## Practice Exercises

### Basic

1. Use `math` to compute EMI: `emi = P * r * (1+r)**n / ((1+r)**n - 1)`.
   **Model answer:**
   ```python
   P, annual_rate, months = 500000, 0.10, 60
   r = annual_rate / 12
   emi = P * r * (1 + r) ** months / ((1 + r) ** months - 1)
   print(round(emi, 2))
   ```

2. Print today's date in `DD/MM/YYYY` using `datetime`.
   **Model answer:**
   ```python
   from datetime import date

   print(date.today().strftime("%d/%m/%Y"))
   ```

3. Generate a list of 6 unique lottery numbers (1–49) using `random`.
   **Model answer:**
   ```python
   import random

   numbers = random.sample(range(1, 50), 6)
   print(sorted(numbers))
   ```

4. Save and load a dictionary to `config.json`.
   **Model answer:**
   ```python
   import json

   config = {"app": "CampusCart", "debug": True}
   with open("config.json", "w", encoding="utf-8") as f:
       json.dump(config, f, indent=2)
   with open("config.json", encoding="utf-8") as f:
       loaded = json.load(f)
   print(loaded)
   ```

### Intermediate

1. Create module `date_utils.py` with `days_until(date_str)` function.
   **Model answer:**
   ```python
   # date_utils.py
   from datetime import datetime, date

   def days_until(date_str):
       """date_str format: DD-MM-YYYY"""
       target = datetime.strptime(date_str, "%d-%m-%Y").date()
       return (target - date.today()).days
   ```

2. Build package `inventory/` with `products.py` and `stock.py`.
   **Model answer:**
   ```python
   # inventory/__init__.py
   from .products import Product
   from .stock import adjust_stock

   # inventory/products.py
   class Product:
       def __init__(self, sku, name, qty):
           self.sku, self.name, self.qty = sku, name, qty

   # inventory/stock.py
   def adjust_stock(product, delta):
       product.qty += delta
       return product.qty
   ```

3. Write script listing all `.py` files in current directory using `os`.
   **Model answer:**
   ```python
   import os

   for name in os.listdir("."):
       if name.endswith(".py"):
           print(name)
   ```

4. Create venv, install `python-dotenv`, freeze to `requirements.txt`.
   **Model answer:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install python-dotenv
   pip freeze > requirements.txt
   ```

### Interview-style

1. Difference between module and package?
   **Model answer:**
   A module is a single `.py` file you import. A package is a directory with `__init__.py` (or a namespace package) that groups related modules so you can write `from inventory.products import Product`.

2. What is `if __name__ == "__main__":` used for?
   **Model answer:**
   It runs a block only when the file is executed as a script, not when imported. Put demos/CLI entry points there so importing the module does not side-effect.

3. How does Python find modules when you `import django`?
   **Model answer:**
   Python searches `sys.path` in order: the script directory, `PYTHONPATH`, site-packages (where pip installs Django), then standard library locations. The first matching package wins.

## Mini-Project: Project Bootstrap Template

**Title:** `py_starter` — Reusable Project Skeleton  
**Lab kit (build here):** [15_Lab_Assets/16_venv_package_bootstrap/](../15_Lab_Assets/16_venv_package_bootstrap/)  
**Also use:** [30_ksr_utils_toolkit](../15_Lab_Assets/30_ksr_utils_toolkit/) (optional polish)

### What to build

| Piece | Requirement |
|-------|-------------|
| `venv/` + `requirements.txt` | Isolated env; freeze after installs |
| `campus_utils/` package | `__init__.py` + at least one helper module |
| `main.py` | Imports package helpers; prints a short demo |
| `data/sample.json` | Defaults loaded by a small `config`/`settings` module |
| `README.md` | Activate, install, run steps for a teammate |

### Stretch

- Add a second helper module (e.g. `validators.py`) and re-export it from `__init__.py`.  
- Pin versions in `requirements.txt` (`requests==…`).  
- Document “works on Windows / macOS / Linux” activation commands.

### Done when

- [ ] Starter kit / your `main.py` runs inside an activated venv  
- [ ] Package import works without `sys.path` hacks  
- [ ] README shows how a teammate recreates the env from `requirements.txt`  
- [ ] Project pushed to GitHub (no `venv/` committed)

---

## Revision Map — Memorize / Understand / Practise / Build

| Topic | Memorize | Understand | Practise | Build |
|-------|----------|------------|----------|-------|
| Imports | `import x`, `from x import y`, `as` | Module search path (`sys.path`) | Import drills | Clean project layout |
| Stdlib | Key functions per module | When to use stdlib vs pip | 5 stdlib mini scripts | Config reader script |
| Packages | `__init__.py` purpose | Package vs module | Create nested package | `ksr_utils` package |
| venv | `python -m venv venv` | Isolated dependencies | Create/activate venv | Project with requirements.txt |
| pip | `pip install`, `pip freeze` | Version pinning basics | Install requests | Share env with team |

## Interview & Discussion Q&A

### Discuss in class

1. Why is `import json` preferred over writing your own JSON parser?
2. When would you use `os.path.join` instead of string concatenation?
3. What goes into `requirements.txt` and what should never go there?
4. How is a Django "app" similar to a Python package?
5. Why do we add `venv/` to `.gitignore` but commit `requirements.txt`?

*No memorized script — push for plain-English answers, then continue to interview Qs below.*

### Interview answers

**Q1. Module vs package?**  
**A:** A module is a single `.py` file. A package is a directory of modules (with `__init__.py`) that can be imported as a hierarchy, e.g. `mypkg.submod`.

**Q2. Purpose of `if __name__ == "__main__":`?**  
**A:** Code under this block runs only when the file is executed directly, not when imported. Enables reusable modules that also work as scripts.

**Q3. Difference between `json.load` and `json.loads`?**  
**A:** `load` reads from a file object; `loads` parses a JSON string.

**Q4. What is pip?**  
**A:** Python's package installer; downloads third-party libraries from PyPI into your environment's `site-packages`.

**Q5. How do you share dependencies with team?**  
**A:** `pip freeze > requirements.txt`; teammates run `pip install -r requirements.txt` inside their venv.

---

