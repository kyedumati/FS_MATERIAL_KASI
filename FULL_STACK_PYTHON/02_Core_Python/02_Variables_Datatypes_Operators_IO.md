# Module: Variables, Datatypes, Operators, and I/O

**Phase:** Core Python  

**Previous module:** Python Setup and First Programs
**Next module:** Flow Control

---

## Learning Outcomes

By the end of this module, learners will be able to:

- Create variables and explain dynamic typing in Python
- Use core datatypes: `int`, `float`, `str`, `bool`, and `None`
- Convert between types safely with `int()`, `float()`, `str()`, and `bool()`
- Apply arithmetic, comparison, logical, assignment, membership, and identity operators
- Read user input with `input()` and display output with `print()` and f-strings
- Build a simple CLI calculator for student marks or expense amounts
- Debug common type errors in beginner code

---

## Classroom Ticket

Open the lab kit **before** long notes. Read the ticket → code in `starter/` or fix `broken/`.

- **[Canteen calculator with GST](../15_Lab_Assets/06_cli_calculator/)**
- **[Marks entry casting crashes](../15_Lab_Assets/07_casting_bugs/)**

Finish the ticket in class; compare with the official solution only when your trainer says so.

### What is a variable?

A **variable** is a name that points to a value stored in memory. Think of it as a labelled box: the label is `student_name`, the contents are `"Ravi Kumar"`.

```python
student_name = "Ravi Kumar"   # str
roll_number = 101             # int
percentage = 87.5             # float
is_pass = True                # bool
```

Python uses **dynamic typing**: you do not declare `int x = 5` like Java. The type is decided by the value you assign, and can change (though good code avoids confusing reassignments).

```python
amount = 100      # int
amount = 99.50    # now float — allowed but be clear in real projects
```

### Core datatypes

| Type | Example | Use in training projects |
|------|---------|--------------------------|
| **int** | `42`, `-7`, `0` | Roll numbers, counts, quantities |
| **float** | `3.14`, `99.99` | Salary, expense amounts, percentages |
| **str** | `"hello"`, `'EMP001'` | Names, emails, IDs as text |
| **bool** | `True`, `False` | Flags: logged in, active employee |
| **None** | `None` | Missing value: no manager assigned yet |

Check type:

```python
print(type(roll_number))   # <class 'int'>
print(type(is_pass))       # <class 'bool'>
```

### Type conversion (casting)

User input always arrives as **string**. You must convert for math.

```python
age_text = input("Enter age: ")   # e.g. user types 22
age = int(age_text)               # convert to int
next_year = age + 1
```

Invalid conversion crashes:

```python
int("abc")   # ValueError
```

Always validate or use try/except (later module) in production apps.

### Operators — quick map

```
Arithmetic:  +  -  *  /  //  %  **
Comparison:  ==  !=  <  >  <=  >=
Logical:     and  or  not
Assignment:  =  +=  -=  *=  /=
Membership:  in  not in
Identity:    is  is not
```

### Input and output

**Output:**

```python
name = "Ananya"
print("Hello", name)              # space between
print(f"Hello, {name}!")          # f-string — preferred
```

**Input:**

```python
email = input("Enter work email: ")
print(f"You entered: {email}")
```

Everything from `input()` is `str` until you convert.

---

## Important Concepts and Definitions

| Term | Definition |
|------|------------|
| **Variable** | Identifier bound to an object in memory |
| **Literal** | Fixed value written in code: `10`, `"hi"`, `True` |
| **Dynamic typing** | Type tied to object, not variable declaration |
| **Type conversion / casting** | Changing representation: `int("5")` → `5` |
| **Operator** | Symbol performing operation on operands |
| **Operand** | Value an operator acts on |
| **Expression** | Combines values/operators to produce result |
| **f-string** | Formatted string: `f"Total: {total}"` |
| **Modulo (`%`)** | Remainder after division |
| **Floor division (`//`)** | Integer division discarding fraction |
| **Truthy / Falsy** | Values that behave as True/False in conditions |

**Falsy values in Python:** `0`, `0.0`, `""`, `None`, `False`, empty collections (later)

---

## Step-by-Step Notes (With Annotated Code)

### Step 1: Variables for student record

```python
# student_record.py — partial record (no input yet)

roll = 2026001
name = "Priya Nair"
marks_python = 78
marks_sql = 82
average = (marks_python + marks_sql) / 2   # float result

print("Roll:", roll)
print("Name:", name)
print(f"Average marks: {average:.2f}")     # 2 decimal places
```

**Note:**
- Wrong: Typo in a name (`salary = 100` then `print(salery)`) → `NameError`.
- Prefer: Spell names consistently; copy-paste the identifier when unsure.

**Try these (2 programs):**

**Program 1 — Ravi marks average**

```python
roll = "2026002"
name = "Ravi"
python_marks = 81
sql_marks = 74
average = (python_marks + sql_marks) / 2
print(f"{name} ({roll}) average: {average:.2f}")
```

**Program 2 — Daily expense total**

```python
food = 185.50
travel = 60.0
total = food + travel
print(f"Today's total: ₹{total:.2f}")
```

### Step 2: Datatypes and None

```python
employee_id = "E1024"        # str — IDs often kept as text (leading zeros)
years_experience = 3         # int
ctc_lakh = 4.5               # float — CTC in lakhs
is_remote = True             # bool
manager_id = None            # no manager for top-level employee

print(type(employee_id))     # <class 'str'>
print(manager_id is None)    # True — preferred None check
```

**Note:**
- Wrong: Checking None with `if x == None`.
- Prefer: `if x is None`.

**Try these (2 programs):**

**Program 1 — Employee types for Priya**

```python
emp_id = "E2048"
years = 2
ctc_lakhs = 6.5
is_remote = True
manager_id = None
print(type(emp_id), type(years), type(ctc_lakhs), type(is_remote), type(manager_id))
```

**Program 2 — None and bool checks**

```python
manager_id = None
is_remote = True
print(manager_id is None)
print(is_remote is True)
```

### Step 3: Arithmetic operators

```python
a, b = 17, 5

print(a + b)    # 22   addition
print(a - b)    # 12   subtraction
print(a * b)    # 85   multiplication
print(a / b)    # 3.4  true division (always float in Py3)
print(a // b)   # 3    floor division
print(a % b)    # 2    remainder — useful: even/odd → n % 2
print(a ** b)   # 1419857  power
```

**Expense tracker example:**

```python
food = 450.50
travel = 120.00
total = food + travel
print(f"Today's spend: ₹{total:.2f}")
```

**Note:**
- Wrong: Expecting `5 / 2` to be `2` (it is `2.5` in Python 3); showing raw `0.1 + 0.2` floats in money UIs.
- Prefer: Use `//` for integer division; round for display (`f"{x:.2f}"`).

**Try these (2 programs):**

**Program 1 — All arithmetic on 25 and 4**

```python
a, b = 25, 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

**Program 2 — Split ₹999 among 3 friends**

```python
bill = 999
friends = 3
print(bill / friends)   # exact share
print(bill // friends)  # whole rupees each
print(bill % friends)   # leftover as remainder
```

### Step 4: Comparison and logical operators

```python
marks = 72
passing = 35

print(marks >= passing)           # True
print(marks == 100)               # False

# Employee login check (simplified)
username_ok = True
password_ok = False
can_login = username_ok and password_ok
print(can_login)                  # False

# At least one condition
has_coupon = False
is_member = True
discount = has_coupon or is_member  # True
```

**Truth table (memorize for interviews):**

| A | B | A and B | A or B |
|---|---|---------|--------|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

**Note:**
- Wrong: Using `=` inside a condition (`if x = 5`) — assignment, not comparison.
- Prefer: `==` for comparison.

**Try these (2 programs):**

**Program 1 — Pass / distinction / fail flags**

```python
marks = 68
pass_mark = 35
print("pass:", marks >= pass_mark)
print("distinction:", marks >= 75)
print("fail:", marks < pass_mark)
```

**Program 2 — Login and discount with and/or**

```python
user_ok = True
pin_ok = False
can_login = user_ok and pin_ok
print("can_login:", can_login)

is_member = False
has_coupon = True
print("discount eligible:", is_member or has_coupon)
```

### Step 5: Assignment operators

```python
balance = 1000
balance += 250    # same as balance = balance + 250  → 1250
balance -= 400    # 850
balance *= 2      # 1700

task_count = 0
task_count += 1   # common pattern when adding tasks
```

**Try these (2 programs):**

**Program 1 — ATM deposit and withdraw**

```python
balance = 8000
balance += 1500
balance -= 2000
print(f"Final balance: ₹{balance}")
```

**Program 2 — Month total with +=**

```python
month_total = 0
month_total += 120
month_total += 85.5
month_total += 40
print(f"Month total: ₹{month_total}")
```

### Step 6: Membership and identity

```python
email = "ravi@company.com"
print("@" in email)          # True
print("gmail" in email)      # False

status = None
if status is None:
    print("Status not set yet")
```

Use `==` for value comparison; `is` mainly for `None` and small integers cache (interview nuance — avoid `is` for strings/content).

**Try these (2 programs):**

**Program 1 — Email membership checks**

```python
email = "priya@ksr.in"
print("@" in email)
print(".in" in email)
```

**Program 2 — manager is None message**

```python
manager = None
if manager is None:
    print("No manager assigned yet")
```

### Step 7: input() and type conversion

```python
# expense_entry.py

print("--- Expense Tracker ---")
category = input("Category (food/travel/other): ")
amount_str = input("Amount in ₹: ")

amount = float(amount_str)   # convert for calculations
print(f"Saved: {category} → ₹{amount:.2f}")
```

**Safe-ish integer input pattern (beginner):**

```python
roll_str = input("Roll number: ")
if roll_str.isdigit():
    roll = int(roll_str)
    print("Roll as int:", roll)
else:
    print("Invalid roll — digits only")
```

**Note:**
- Wrong: Treating `input()` as a number (`input("N: ") + 1`) or casting `int("12.5")` directly.
- Prefer: `int(input(...))` / `float(input(...))`; for `"12.5"` use `float` first (then `int` if needed).

**Try these (2 programs):**

**Program 1 — Category and amount entry**

```python
category = "food"
amount = float("250")
print(f"Saved: {category} → ₹{amount:.2f}")
```

**Program 2 — Validate roll with isdigit**

```python
roll_text = "2026001"
if roll_text.isdigit():
    roll = int(roll_text)
    print(roll)
else:
    print("Invalid roll")
```

### Step 8: f-strings in depth

```python
name = "Karthik"
role = "Backend Intern"
salary = 25000

# Basic
print(f"{name} works as {role}")

# Expressions inside braces
print(f"Annual (approx): ₹{salary * 12:,}")   # ₹300,000 formatting

# Alignment (reports)
print(f"{'Item':<15}{'Amount':>10}")
print(f"{'Food':<15}{450.5:>10.2f}")
```

**Note:**
- Wrong: Concatenating str + int (`"Age: " + 22`) → `TypeError`.
- Prefer: `f"Age: {22}"` or `str(22)`.

**Try these (2 programs):**

**Program 1 — Offer letter f-string**

```python
name = "Ravi"
role = "Intern"
salary = 25000
print(f"{name} — {role} — ₹{salary:,}/month")
```

**Program 2 — Aligned canteen receipt**

```python
print(f"{'Item':<10}{'Price':>8}")
print(f"{'Chai':<10}{'₹20':>8}")
print(f"{'Samosa':<10}{'₹25':>8}")
```

### Step 9: Mini CLI calculator

```python
# simple_calculator.py

print("=== Student Marks Calculator ===")
m1 = float(input("Python marks: "))
m2 = float(input("SQL marks: "))
m3 = float(input("HTML marks: "))

total = m1 + m2 + m3
average = total / 3

print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"Pass?" , average >= 35)   # preview of flow control
```

**Try these (2 programs):**

**Program 1 — Three-subject average**

```python
m1, m2, m3 = 78, 82, 91
total = m1 + m2 + m3
average = total / 3
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print("Pass:", average >= 35)
```

**Program 2 — Line total with 18% GST**

```python
price = 499.0
qty = 2
line_total = price * qty * 1.18
print(f"Line total with GST: ₹{line_total:.2f}")
```

---

## Practice Exercises

### Basic

1. Create variables for a student: name, age, course, fees (float). Print with f-string.

   **Model answer:**

   ```python
   name = "Ananya"
   age = 21
   course = "Full Stack Python"
   fees = 45000.0
   print(f"{name}, age {age}, enrolled in {course}. Fees: ₹{fees}")
   ```

2. Convert `"100"` and `"3.14"` to int and float; print types.

   **Model answer:**

   ```python
   n = int("100")
   x = float("3.14")
   print(n, type(n))
   print(x, type(x))
   ```

3. Evaluate: `10 + 5 * 2`, `20 // 3`, `20 % 3`, `2 ** 4`.

   **Model answer:**

   ```python
   print(10 + 5 * 2)  # 20 — multiply first
   print(20 // 3)     # 6 — floor division
   print(20 % 3)      # 2 — remainder
   print(2 ** 4)      # 16 — power
   ```

4. Ask user for name and city; print greeting.

   **Model answer:**

   ```python
   name = input("Name: ")
   city = input("City: ")
   print(f"Namaste, {name} from {city}!")
   ```

### Intermediate

1. **Employee portal:** Input basic salary and HRA (float); print total compensation.

   **Model answer:**

   ```python
   basic = float(input("Basic salary: "))
   hra = float(input("HRA: "))
   total = basic + hra
   print(f"Total compensation: ₹{total:.2f}")
   ```

2. Check if email contains `@` and `.com` using `in` and `and`.

   **Model answer:** (boolean expression only — no `if` yet)

   ```python
   email = input("Email: ")
   looks_ok = "@" in email and ".com" in email
   print(looks_ok)
   print(f"Contains @ and .com: {looks_ok}")
   ```

3. Use `+=` to simulate adding three expenses to a running total starting at 0.

   **Model answer:**

   ```python
   total = 0
   total += 120   # chai + snack
   total += 450   # lunch
   total += 80    # metro
   print(f"Running total: ₹{total}")
   ```

4. Format a receipt table (3 items, amounts, grand total) with aligned f-strings.

   **Model answer:**

   ```python
   item1, amt1 = "Samosa", 40.0
   item2, amt2 = "Thali", 180.0
   item3, amt3 = "Lassi", 60.0
   grand = amt1 + amt2 + amt3
   print(f"{'Item':<12}{'Amount':>8}")
   print(f"{item1:<12}{amt1:>8.2f}")
   print(f"{item2:<12}{amt2:>8.2f}")
   print(f"{item3:<12}{amt3:>8.2f}")
   print(f"{'TOTAL':<12}{grand:>8.2f}")
   ```

### Interview-Oriented

1. Difference between `/` and `//` in Python 3 with examples.

   **Model answer:** `/` is true division and returns a **float** (`7 / 2` → `3.5`). `//` is floor division toward −∞ for ints (`7 // 2` → `3`). Use `/` for real averages; `//` for whole groups (e.g. how many full dozens).

2. What is dynamic typing? Is Python strongly typed? (Yes — no implicit str+int.)

   **Model answer:** **Dynamic typing:** you do not declare types; a name can hold an `int` then later a `str`. **Strongly typed:** incompatible operations fail — `"5" + 5` raises `TypeError`; you must cast explicitly (`int("5") + 5`). So: dynamic *and* strong.

3. Explain `is` vs `==` with `None` example.

   **Model answer:** `==` compares **values**. `is` compares **object identity** (same object in memory). For `None`, the idiom is `x is None` / `x is not None`, not `x == None`, because there is only one `None` object and identity is the clear check.

4. Why does `0.1 + 0.2 == 0.3` evaluate False? (Float representation — mention rounding.)

   **Model answer:** Binary floating point cannot represent 0.1 and 0.2 exactly, so their sum is a tiny bit off from 0.3. Compare with rounding or a tolerance: `round(0.1 + 0.2, 10) == 0.3`, or use `decimal.Decimal` for money later. Never assume float equality for currency without care.

---

## Mini-Project: CLI Canteen Calculator

**Title:** One-session calculator with GST + validation  
**Lab kit (build here):** [15_Lab_Assets/06_cli_calculator/](../15_Lab_Assets/06_cli_calculator/)  
**Also use:** [07_casting_bugs](../15_Lab_Assets/07_casting_bugs/)  
**Later (files module):** [01_python_expense_tracker](../15_Lab_Assets/01_python_expense_tracker/) — CSV export after you learn file handling

### What to build

1. Read item **price** and **qty** from the user (floats / ints via casting)  
2. Compute `subtotal = price * qty`, then **GST 5%**, then grand total  
3. If price or qty `<= 0`, print an error and do not compute  
4. Print a ₹ receipt line with 2 decimal places  
5. Loop for **3** items in one run; keep `day_total` with `+=`  

**Sample run:**

```
--- Canteen Calculator ---
Price: 40
Qty: 2
✓ Item: ₹80.00 + GST ₹4.00 = ₹84.00
...
Day total: ₹210.00
```

### Stretch

- Reject non-numeric input without crashing (reuse casting-bugs ideas).  
- Print a mini table of all three items with grand total.  

### Done when

- [ ] Lab kit canteen calculator ticket passes  
- [ ] Three valid items update `day_total` correctly  
- [ ] Amount/`qty` `<= 0` prints an error and is not added  
- [ ] Output uses `₹` and two decimal places  

---

## Revision Map — Memorize / Understand / Practise / Build

| Topic | Memorize | Understand | Practise | Build |
|-------|----------|------------|----------|-------|
| Variables | Assignment `=` | Name binds to object | 20 assignment drills | — |
| Datatypes | int, float, str, bool, None | Dynamic typing | `type()` checks | — |
| Type conversion | `int()`, `float()`, `str()` | Invalid conversion errors | Cast user input | Safe parsing |
| Arithmetic ops | `+ - * / // % **` | `/` vs `//`, `%` modulo | Calculator lines | CLI calculator |
| Comparison | `== != < > <= >=` | Boolean result | Compare marks | Pass/fail logic prep |
| Logical | `and or not` | Truth tables | Combine conditions | Login validation prep |
| Assignment ops | `+=`, `-=` | Shorthand update | Loop counters later | Balance updates |
| Membership | `in`, `not in` | Works on strings/lists later | `"@" in email` | Email check |
| Identity | `is`, `is not` | `None` checks | `x is None` | Optional fields |
| I/O | `input()`, f-strings | input returns str always | Forms in CLI | Employee data entry |

---

## Interview & Discussion Q&A

Shared with students after concepts and the mini-project. Use for review and interview prep — questions and model answers are included.

1. Should employee ID be stored as `int` or `str`? When does leading zero matter?
2. Why do banking apps show ₹ symbols in UI but store numbers as float/decimal in backend?
3. What happens if a user presses Enter without typing anything in `input()`?
4. Is `not in` the opposite of `in`? Give example with email domain check.
5. where have you used variables in Excel formulas — same idea?

**Q1. Name Python's basic data types.**  
**A:** int, float, str, bool, NoneType; plus list, dict, tuple, set at collection level.

**Q2. What is an f-string?**  
**A:** Literal prefixed with `f` allowing embedded expressions `{expr}` evaluated and formatted in string.

**Q3. Difference between `and` and `or`?**  
**A:** `and` true only if both operands true; `or` true if at least one true.

**Q4. What does `%` operator do?**  
**A:** Modulo — remainder of division; used for even/odd, cycles, hash buckets.

**Q5. Is Python strongly typed?**  
**A:** Yes — does not silently convert incompatible types (no automatic str+int); dynamic means types not declared upfront.

---

