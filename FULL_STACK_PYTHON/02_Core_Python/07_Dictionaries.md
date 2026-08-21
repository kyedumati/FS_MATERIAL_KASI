# Dictionaries in Python 3

**Module:** Core Python · Collections  
**Previous module:** Tuples and Sets
**Next module:** Data Structures Overview

---

## Learning Outcomes

By the end of this session, learners will be able to:

1. Perform **CRUD** operations on dictionaries (create, read, update, delete key-value pairs).
2. Use `.get()`, `.keys()`, `.values()`, `.items()` safely and idiomatically.
3. Build and traverse **nested dictionaries** (employee profile, product catalog, order JSON).
4. Iterate dictionaries with `for` loops without losing track of keys and values.
5. Relate Python dicts to **JSON-like** structures used in APIs and front-end apps.

---

A **dictionary** is like a real dictionary or phone contacts app:

- You look up a **word (key)** and get a **meaning (value)**.
- Keys must be **unique** — one phone number cannot map to two different people in the same dict.
- Values can be anything: string, number, list, or even another dictionary.

**Icons:** Employee · Order · Bank · Payroll · CRM

**Where used?**
- Payroll / Employee portal — `{emp_id: profile}` lookups
- Ecommerce — product by SKU, order JSON with nested items
- Banking — account record fields, UPI txn metadata
- College apps — student dict (`roll`, `marks`, `grade`)
- Hospital / CRM — contact book, ticket fields from APIs

**Examples from daily work:**

| Key | Value | Scenario |
|-----|-------|----------|
| `"emp_id"` | `101` | Employee record |
| `"email"` | `"aisha@company.com"` | Login profile |
| `"price"` | `1499.00` | E-commerce product |
| `"items"` | `[{"sku": "P1", "qty": 2}]` | Order JSON from API |

When you fetch data from a REST API, you almost always handle **dicts** (and lists of dicts).

---

## Concepts and Definitions

| Term | Definition |
|------|------------|
| **Dictionary (`dict`)** | Mutable mapping of unique keys to values. |
| **Key** | Lookup identifier — str, int, tuple (hashable), etc. |
| **Value** | Data stored for a key — any type. |
| **Key-value pair** | One entry: `"name": "Ananya"`. |
| **Hashable** | Can be used as dict key (not list/dict). |
| **Nested dict** | Dict inside dict — models JSON documents. |
| **`.get(key, default)`** | Safe read; no KeyError if missing. |
| **JSON** | JavaScript Object Notation — text format; Python dict ↔ JSON in APIs. |

---

## Step-by-Step Notes with Annotated Python 3 Code

### Step 1 — Create and read (CRUD: Create, Read)

```python
# CREATE — literal or dict()
employee = {
    "emp_id": 101,
    "name": "Ananya Sharma",
    "department": "Engineering",
    "salary": 85000,
}

empty_cart = {}
product = dict(sku="P001", name="Wireless Mouse", price=799)

# READ — bracket notation
print(employee["name"])             # Ananya Sharma
print(product["price"])             # 799

# READ — safe with .get()
print(employee.get("email"))          # None — key missing, no crash
print(employee.get("email", "N/A"))   # N/A — default provided

# KeyError if missing with brackets:
# print(employee["email"])          # KeyError
```

**Note:**
- Wrong: Using a list as a key → `TypeError: unhashable type: 'list'`; `d["missing"]` without a check → `KeyError`; duplicate keys in a literal (last value wins silently).
- Prefer: String or tuple keys; `.get()` or `if key in d`; avoid duplicate keys (`{"a": 1, "a": 2}` → `a` is 2).

**Try these (2 programs):**

**Program 1 — Student dict with .get**

```python
student = {"name": "Priya", "roll": "2026001", "marks": 88}
print(student["name"])
print(student.get("phone", "N/A"))
```

**Expected Output:**

```
Priya
N/A
```

**Remember:** Prefer `.get("key", default)` when a field might be missing — brackets `d["key"]` raise `KeyError`.

**Program 2 — Product via dict()**

```python
product = dict(sku="P10", name="Chai Mug", price=299)
print(product["price"])
```

**Expected Output:**

```
299
```

### Step 2 — Update and add (CRUD: Update)

```python
contact = {"name": "Dev Kumar", "phone": "9876543210"}

# UPDATE existing key
contact["phone"] = "9876500000"

# ADD new key
contact["email"] = "dev@example.com"
contact["city"] = "Bengaluru"

print(contact)
# {'name': 'Dev Kumar', 'phone': '9876500000', 'email': 'dev@example.com', 'city': 'Bengaluru'}

# update() — merge another dict
extra = {"company": "KSR Tech", "role": "Developer"}
contact.update(extra)
```

**Try these (2 programs):**

**Program 1 — Update and add contact fields**

```python
contact = {"name": "Ravi", "phone": "9876543210"}
contact["phone"] = "9876500000"
contact["email"] = "ravi@example.com"
contact["city"] = "Bengaluru"
print(contact)
```

**Program 2 — update with role and company**

```python
contact = {"name": "Ravi", "phone": "9876543210"}
contact.update({"role": "Intern", "company": "KSR Tech"})
print(contact)
```

### Step 3 — Delete (CRUD: Delete)

```python
expense = {"date": "2025-07-01", "category": "Food", "amount": 450}

# DELETE one key
del expense["category"]

# pop — remove and return value
amount = expense.pop("amount", 0)     # 450; default 0 if missing
print(amount, expense)                # 450 {'date': '2025-07-01'}

# clear all
expense.clear()                       # {}
```

**Try these (2 programs):**

**Program 1 — pop amount**

```python
expense = {"date": "01-08-2026", "category": "Food", "amount": 450}
amount = expense.pop("amount")
print(amount)
print(expense)
```

**Expected Output:**

```
450
{'date': '01-08-2026', 'category': 'Food'}
```

**Program 2 — del then clear**

```python
expense = {"date": "01-08-2026", "category": "Food", "amount": 450}
del expense["category"]
expense.clear()
print(expense)
```

**Expected Output:**

```
{}
```

### Step 4 — Keys, values, items

```python
product = {"sku": "P002", "name": "Keyboard", "price": 1499, "stock": 25}

print(list(product.keys()))           # ['sku', 'name', 'price', 'stock']
print(list(product.values()))         # ['P002', 'Keyboard', 1499, 25]

# items() — pairs for looping
for key, value in product.items():
    print(f"{key}: {value}")
```

**Try these (2 programs):**

**Program 1 — Loop marks items**

```python
marks = {"Python": 88, "SQL": 76}
for subject, score in marks.items():
    print(f"{subject}: {score}")
```

**Expected Output:**

```
Python: 88
SQL: 76
```

**Program 2 — keys and values lists**

```python
product = {"sku": "P10", "name": "Chai Mug", "price": 299}
print(list(product.keys()))
print(list(product.values()))
```

### Step 5 — Iterate and build new dicts

```python
# Word frequency from review text (e-commerce)
reviews = ["good", "fast", "good", "quality", "fast", "good"]
frequency = {}

for word in reviews:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)                      # {'good': 3, 'fast': 2, 'quality': 1}

# Dict comprehension — 10% discount prices
prices = {"mouse": 799, "keyboard": 1499, "hub": 599}
sale_prices = {k: round(v * 0.9, 2) for k, v in prices.items()}
print(sale_prices)
```

**Note:**
- Wrong: Modifying a dict while iterating — RuntimeError or skipped keys.
- Prefer: Iterate over a copy: `list(d.items())`.

**Try these (2 programs):**

**Program 1 — Word frequency with .get**

```python
words = ["good", "fast", "good", "ok", "fast"]
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)
```

**Expected Output:**

```
{'good': 2, 'fast': 2, 'ok': 1}
```

**Program 2 — 10% off dict comprehension**

```python
prices = {"mouse": 799, "hub": 599}
discounted = {k: round(v * 0.9, 2) for k, v in prices.items()}
print(discounted)
```

**Expected Output:**

```
{'mouse': 719.1, 'hub': 539.1}
```

### Step 6 — Nested dictionaries

```python
# Employee with nested address
employee = {
    "emp_id": 101,
    "name": "Meera Iyer",
    "address": {
        "city": "Chennai",
        "pincode": "600001",
        "country": "India",
    },
    "skills": ["Python", "SQL", "Git"],
}

# READ nested
print(employee["address"]["city"])    # Chennai
print(employee["skills"][0])          # Python

# UPDATE nested
employee["address"]["pincode"] = "600002"
```

**Note:**
- Wrong: Shared nested dict reference — changing a shallow copy affects the original.
- Prefer: `copy.deepcopy()` for nested structures.

**Try these (2 programs):**

**Program 1 — Nested employee city and skill**

```python
employee = {
    "name": "Meera",
    "address": {"city": "Pune", "pincode": "411001"},
    "skills": ["Python", "SQL"],
}
print(employee["address"]["city"])
print(employee["skills"][0])
```

**Program 2 — Update nested pincode**

```python
employee = {
    "name": "Meera",
    "address": {"city": "Pune", "pincode": "411001"},
}
employee["address"]["pincode"] = "411014"
print(employee["address"])
```

### Step 7 — JSON-like order structure (API shape)

```python
order = {
    "order_id": "ORD-9001",
    "customer": {
        "name": "Ravi Patel",
        "email": "ravi@example.com",
    },
    "items": [
        {"sku": "P001", "name": "Notebook", "qty": 2, "price": 120},
        {"sku": "P003", "name": "Pen", "qty": 5, "price": 15},
    ],
    "status": "confirmed",
    "total": 315,
}

# Loop line items
for item in order["items"]:
    line_total = item["qty"] * item["price"]
    print(f"{item['name']}: ₹{line_total}")
```

**Try these (2 programs):**

**Program 1 — Order line totals**

```python
order = {
    "customer": {"name": "Ravi", "email": "ravi@example.com"},
    "items": [
        {"sku": "P001", "qty": 2, "price": 120},
        {"sku": "P002", "qty": 1, "price": 499},
    ],
}
for item in order["items"]:
    print(f"₹{item['qty'] * item['price']}")
```

**Program 2 — Nested customer email**

```python
order = {
    "customer": {"name": "Ravi", "email": "ravi@example.com"},
    "items": [],
}
print(order["customer"]["email"])
```

### Step 8 — Check membership and copy

```python
user = {"username": "aisha", "role": "staff", "active": True}

print("username" in user)             # True — checks keys
print("admin" in user)                # False

# Shallow copy
user_backup = user.copy()
user_backup["role"] = "admin"
print(user["role"])                   # staff — original unchanged
```

**Note:**
- Wrong: Using `in` as if it checks values (`"aisha" in d` checks **keys** only).
- Prefer: `if "aisha" in d.values():` when you mean values.

**Try these (2 programs):**

**Program 1 — Key membership check**

```python
contact = {"name": "Ravi", "phone": "9876543210"}
print("Found" if "email" in contact else "Missing")
```

**Expected Output:**

```
Missing
```

**Common Error:** `"Ravi" in contact` checks **keys**, not values — that expression is `False` even though `"Ravi"` is stored as a value.

**Program 2 — Shallow copy independence**

```python
user = {"username": "aisha", "role": "staff"}
backup = user.copy()
backup["role"] = "admin"
print(user["role"])    # staff
print(backup["role"])  # admin
```

### Step 9 — Python dict ↔ JSON (preview for APIs)

```python
import json

# Python dict → JSON string (for API response)
product = {"sku": "P001", "name": "Mouse", "price": 799}
json_text = json.dumps(product)
print(json_text)                      # {"sku": "P001", "name": "Mouse", "price": 799}

# JSON string → Python dict (from API request body)
parsed = json.loads(json_text)
print(parsed["name"])                 # Mouse
```

**Note:**
- Wrong: Assuming JSON allows a tuple — JSON has no tuple type.
- Prefer: Convert tuples to lists before `json.dumps`.

**Try these (2 programs):**

**Program 1 — dict to JSON string**

```python
import json

product = {"sku": "P001", "name": "Mouse", "price": 799}
print(json.dumps(product))
```

**Program 2 — JSON string back to dict**

```python
import json

text = json.dumps({"sku": "P001", "name": "Mouse", "price": 799})
product = json.loads(text)
print(product["name"])
```

---

## Practice Exercises

### Basic

1. Create a dict for one student: `name`, `roll`, `marks`. Print each field using `.items()`.

   **Model answer:**

```python
student = {"name": "Dev", "roll": 21, "marks": 88}
for key, value in student.items():
    print(f"{key}: {value}")
```


2. Add key `"grade"` based on marks (A if ≥90, B if ≥75, else C).

   **Model answer:**

```python
student = {"name": "Dev", "roll": 21, "marks": 88}
marks = student["marks"]
if marks >= 90:
    student["grade"] = "A"
elif marks >= 75:
    student["grade"] = "B"
else:
    student["grade"] = "C"
print(student)
```


3. Use `.get()` to read `"phone"` with default `"Not provided"`.

   **Model answer:**

```python
student = {"name": "Dev", "roll": 21, "marks": 88}
phone = student.get("phone", "Not provided")
print(phone)  # Not provided
```


### Intermediate

4. Build a product catalog: `{sku: {"name": ..., "price": ...}}` for 3 products. Lookup by SKU from user input.

   **Model answer:**

```python
catalog = {
    "P101": {"name": "Notebook", "price": 80.0},
    "P102": {"name": "Pen Set", "price": 120.0},
    "P103": {"name": "USB Drive", "price": 499.0},
}
sku = input("Enter SKU: ").strip().upper()
product = catalog.get(sku)
if product:
    print(f"{product['name']} — ₹{product['price']}")
else:
    print("SKU not found")
```


5. Count how many expenses per category: `[{"cat":"Food","amt":450}, ...]`.

   **Model answer:**

```python
expenses = [
    {"cat": "Food", "amt": 450},
    {"cat": "Travel", "amt": 120},
    {"cat": "Food", "amt": 200},
    {"cat": "Utilities", "amt": 900},
    {"cat": "Travel", "amt": 80},
]
counts = {}
for row in expenses:
    cat = row["cat"]
    counts[cat] = counts.get(cat, 0) + 1
print(counts)  # {'Food': 2, 'Travel': 2, 'Utilities': 1}
```


6. Update nested dict: change customer city inside an order dict.

   **Model answer:**

```python
order = {
    "order_id": "ORD-901",
    "customer": {"name": "Meera", "city": "Pune"},
    "total": 2499.0,
}
order["customer"]["city"] = "Bengaluru"
print(order["customer"])
```


### Interview-style

7. Merge two dicts; if same key, **sum** numeric values (assume int/float).

   **Model answer:**

```python
def merge_sum(a, b):
    result = dict(a)
    for key, value in b.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value
    return result

left = {"Food": 450, "Travel": 120}
right = {"Food": 200, "Utilities": 900}
print(merge_sum(left, right))
# {'Food': 650, 'Travel': 120, 'Utilities': 900}
```


8. Invert dict `{101: "Ananya", 102: "Dev"}` → `{"Ananya": 101, "Dev": 102}` (assume unique values).

   **Model answer:**

```python
original = {101: "Ananya", 102: "Dev"}
inverted = {value: key for key, value in original.items()}
print(inverted)
```


9. Flatten one level: `{"a": 1, "b": {"c": 2, "d": 3}}` → keys `a`, `b.c`, `b.d` (optional stretch).

   **Model answer:**

```python
def flatten_one_level(data):
    flat = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for inner_key, inner_val in value.items():
                flat[f"{key}.{inner_key}"] = inner_val
        else:
            flat[key] = value
    return flat

print(flatten_one_level({"a": 1, "b": {"c": 2, "d": 3}}))
# {'a': 1, 'b.c': 2, 'b.d': 3}
```


---

## Mini-Project (Assignment): Contact Book CLI

**Title:** Phone-keyed contact book with CRUD  
**Lab kit (build here):** [15_Lab_Assets/11_contact_book/](../15_Lab_Assets/11_contact_book/)

### What to build

```python
contacts = {}   # key: phone (str), value: dict with name, email

def add_contact():
    phone = input("Phone: ").strip()
    if phone in contacts:
        print("Contact exists. Use update.")
        return
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    contacts[phone] = {"name": name, "email": email}
    print("Added.")

def search_contact():
    phone = input("Phone to search: ").strip()
    info = contacts.get(phone)
    if info:
        print(f"{info['name']} | {info['email']}")
    else:
        print("Not found.")

def list_contacts():
    for phone, info in contacts.items():
        print(f"{phone}: {info['name']} ({info['email']})")

# Menu: 1 Add  2 Search  3 List  4 Update  5 Delete  6 Exit
```

### Stretch

- Search by name (scan values) when phone is unknown.  
- Export contacts as a JSON string with `json.dumps`.  

### Done when

- [ ] Lab kit contact-book ticket add/search/list works  
- [ ] Update and delete by phone work without KeyError  
- [ ] Menu exits cleanly on option 6  


## Interview Q&A

Shared with students after concepts and the mini-project. Use for review and interview prep — questions and model answers are included.

1. Why are dict lookups often preferred over scanning a list for a matching ID?
2. How is a Python dict similar to a MySQL row + column names?
3. What happens if two API clients send the same JSON key twice?
4. When would nested dict become hard to maintain? (Preview: classes and methods.)
5. Can dict values be lists? Give an order example.

1. **Dict vs list for lookup by ID?**  
   **A:** Dict O(1) average vs list O(n) scan.

2. **Are dict keys ordered?**  
   **A:** Insertion order preserved since Python 3.7; still treat order as a bonus, not the main reason to use a dict.

3. **Copy dict?**  
   **A:** `.copy()` shallow; `copy.deepcopy()` for nested.

4. **dict comprehension example?**  
   **A:** `{k: v*2 for k, v in d.items()}`.

5. **Can we sort a dict?**  
   **A:** Sort keys: `sorted(d)`; items: `sorted(d.items(), key=...)`.

---

