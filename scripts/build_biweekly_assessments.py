#!/usr/bin/env python3
"""One-shot: build 16_Assessments + strip module Assessment sections."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FS = ROOT / "PYTHON"
ASSESS = FS / "16_Assessments"
FRONTEND = ROOT / "FRONTEND"

# Module relative path -> (BW id, weeks label for pointer)
# Modules do not get Biweekly Assessment sections — calendar + 16_Assessments/README are SoT.
MODULE_BW: dict[str, tuple[str, str]] = {}
FRONTEND_BW: dict[str, tuple[str, str]] = {}

BW_META = {
    "BW01": {
        "file": "BW01_Weeks_01_02_Foundations_Setup.md",
        "title": "Biweekly Assessment BW01 — Weeks 1–2",
        "sessions": "S01–10",
        "topics": "Computer foundations, terminal, Python setup, variables, operators, I/O, f-strings, casting, canteen calculator",
        "coding_note": "Linear scripts only — no `if` / `while` / `for` / `def` (those start Week 3).",
    },
    "BW02": {
        "file": "BW02_Weeks_03_04_Flow_Strings_Lists.md",
        "title": "Biweekly Assessment BW02 — Weeks 3–4",
        "sessions": "S11–20",
        "topics": "if/elif/else, for/while, break/continue, menus, strings, lists, marks manager",
        "coding_note": "Loops and lists OK. No `def` yet (Functions start Week 6).",
    },
    "BW03": {
        "file": "BW03_Weeks_05_06_Collections_Functions.md",
        "title": "Biweekly Assessment BW03 — Weeks 5–6",
        "sessions": "S21–30",
        "topics": "Tuples, sets, dicts, structure choice, stacks, functions intro (def/return/params), scope intro",
        "coding_note": "Dicts/sets OK. Simple `def` OK for Week-6 topics. No decorators/generators yet (Week 7).",
    },
    "BW04": {
        "file": "BW04_Weeks_07_08_Advanced_OOP_Exceptions.md",
        "title": "Biweekly Assessment BW04 — Weeks 7–8",
        "sessions": "S31–40",
        "topics": "Generators, ksr_utils, modules/venv, OOP (including ABC / interface)",
        "coding_note": "Classes and ABC OK. Use print+return for bad amounts — no try/except (exceptions are Week 9).",
    },
    "BW05": {
        "file": "BW05_Weeks_09_10_Files_Git_MySQL.md",
        "title": "Biweekly Assessment BW05 — Weeks 9–10",
        "sessions": "S41–50",
        "topics": "Exception handling (try/except + custom), files/CSV/logging, Git/GitHub, MySQL setup and SELECT intro",
        "coding_note": "Files + SQL concepts OK.",
    },
    "BW06": {
        "file": "BW06_Weeks_11_12_SQL_Frontend.md",
        "title": "Biweekly Assessment BW06 — Weeks 11–12",
        "sessions": "S51–60",
        "topics": "MySQL finish, Python DB bridge, HTML, CSS responsive start",
        "coding_note": "SQL + HTML/CSS. No Django yet.",
    },
    "BW07": {
        "file": "BW07_Weeks_13_14_JS_Django_Core.md",
        "title": "Biweekly Assessment BW07 — Weeks 13–14",
        "sessions": "S61–70",
        "topics": "JavaScript DOM/forms, Django setup, URLs/views/templates, models/ORM/admin",
        "coding_note": "JS + Django MTV/ORM. Auth is next biweekly.",
    },
    "BW08": {
        "file": "BW08_Weeks_15_16_Auth_Deploy_Capstone.md",
        "title": "Biweekly Assessment BW08 — Weeks 15–16",
        "sessions": "S71–80",
        "topics": "Forms, sessions, auth, CRUD lab, security, deployment, capstone kickoff",
        "coding_note": "Django auth and deploy concepts.",
    },
    "BW09": {
        "file": "BW09_Weeks_17_18_APIs_React.md",
        "title": "Biweekly Assessment BW09 — Weeks 17–18",
        "sessions": "S81–90",
        "topics": "Flask overview, REST/JSON/Postman/DRF, React fundamentals, hooks/routing/CORS",
        "coding_note": "API + React concepts.",
    },
    "BW10": {
        "file": "BW10_Weeks_19_20_Testing_Placement.md",
        "title": "Biweekly Assessment BW10 — Weeks 19–20",
        "sessions": "S91–100",
        "topics": "Testing/debugging/clean code, AI integration lite, resume/interview/placement mocks",
        "coding_note": "Testing + career readiness.",
    },
}

# Curated papers: 12 MCQs (q, options dict a-d, answer letter), 2 coding prompts, 1 short answer
# Built for teaching-order correctness rather than blind harvest.

PAPERS: dict[str, dict] = {}


def mcq(q: str, a: str, b: str, c: str, d: str, ans: str) -> dict:
    return {"q": q, "opts": {"a": a, "b": b, "c": c, "d": d}, "ans": ans}


PAPERS["BW01"] = {
    "mcqs": [
        mcq("A computer mainly follows which pattern?", "Input → Process → Output", "Output → Input only", "Process without input", "Hardware only", "a"),
        mcq("Which extension is a Python source file?", ".txt", ".py", ".exe", ".md", "b"),
        mcq("In the terminal, which command lists files (Unix/macOS)?", "dir", "ls", "show", "list", "b"),
        mcq("REPL means you type Python and see results:", "Only after saving a .py file", "Immediately, line by line", "Only on GitHub", "Only in MySQL", "b"),
        mcq("Which is a valid variable name in Python?", "2marks", "student_name", "student-name", "class", "b"),
        mcq("What does `type(3.5)` return?", "int", "float", "str", "bool", "b"),
        mcq("f-strings start with:", "f before the quotes", "F after the quotes", "`format:` keyword", "%s only", "a"),
        mcq("`int(\"78.5\")` typically:", "Returns 78", "Raises an error", "Returns 78.5", "Returns None", "b"),
        mcq("GST 5% on subtotal uses which idea?", "subtotal + 5", "subtotal * 0.05 added to subtotal", "subtotal // 5", "subtotal - 0.05", "b"),
        mcq("`print` is used to:", "Read keyboard input", "Show output to the screen", "Create folders", "Install packages", "b"),
        mcq("`input()` always gives you a:", "int", "float", "str", "bool", "c"),
        mcq("VS Code is mainly a:", "Database server", "Code editor / IDE", "Operating system", "Web browser only", "b"),
    ],
    "coding": [
        "Ask for a canteen item **price** and **qty** (use `float` and `int`). Compute total with **5% GST** and print `Total: ₹…` with 2 decimals. Linear script only (no `if`/`def`).",
        "Read three subject marks with `float(input(...))` and print their average with 2 decimals (f-string). No loops/`def`.",
    ],
    "short": "In 3–4 sentences, explain the difference between an **algorithm** and a **program**, with one India campus example.",
    "short_key": "Algorithm = steps in English/logic; program = those steps written in a language the computer runs (e.g. Python). Example: steps to compute GST vs a `.py` file that prints the total.",
}

PAPERS["BW02"] = {
    "mcqs": [
        mcq("`elif` means:", "else if", "end if", "error if", "empty if", "a"),
        mcq("`range(1, 5)` yields:", "1 2 3 4 5", "1 2 3 4", "0 1 2 3 4", "5 4 3 2 1", "b"),
        mcq("`break` in a loop:", "Skips one iteration", "Exits the loop immediately", "Restarts Python", "Deletes variables", "b"),
        mcq("`continue` in a loop:", "Exits the program", "Skips the rest of this iteration", "Pauses forever", "Creates a new loop", "b"),
        mcq("A `while True` menu needs:", "No exit path", "A `break` (or return later) when user quits", "Only `for`", "Only `print`", "b"),
        mcq("Strings are:", "Mutable", "Immutable", "Always integers", "Only uppercase", "b"),
        mcq("`\"Hello\"[1:4]` is:", "Hel", "ell", "ello", "H", "b"),
        mcq("Lists use which brackets?", "()", "{}", "[]", "<>", "c"),
        mcq("`marks.append(90)`:", "Removes 90", "Adds 90 at the end", "Sorts the list", "Clears the list", "b"),
        mcq("Empty list average should:", "Divide by zero quietly", "Be guarded (message / skip)", "Always be 100", "Crash intentionally in production", "b"),
        mcq("Nested `if` means:", "if inside another if", "Two files", "Only loops", "Only strings", "a"),
        mcq("`\"  Hi \".strip()` returns:", "`\"  Hi \"`", "`\"Hi\"`", "`\"Hi \"`", "`\"  Hi\"`", "b"),
    ],
    "coding": [
        "Write a mini ATM menu (balance starts 1000): options Balance / Deposit / Withdraw / Quit. Block overdraft. Use `while`/`if` only — **no `def`**.",
        "Keep a list of marks. Menu: add mark (0–100), list, average (safe if empty), toppers (≥90), quit. No `def`.",
    ],
    "short": "When do you choose `for` vs `while`? Give one example of each from a student-portal style app.",
    "short_key": "`for` when count/items known (print 1–10 tables); `while` when repeat until condition (menu until Quit).",
}

PAPERS["BW03"] = {
    "mcqs": [
        mcq("Tuples are:", "Mutable", "Immutable", "Always empty", "Same as sets", "b"),
        mcq("Sets store:", "Duplicates kept", "Unique elements", "Only strings", "Ordered always (guarantee)", "b"),
        mcq("`dict.fromkeys` is useful for:", "Sorting ints", "Order-preserving unique keys", "Opening files", "Installing pip", "b"),
        mcq("Dict lookup uses:", "Indexes only", "Keys", "Only loops", "SQL", "b"),
        mcq("`contacts.get(\"Ravi\")` if missing:", "KeyError", "None (default)", "0", "False always", "b"),
        mcq("A stack is typically:", "FIFO", "LIFO", "Random", "Sorted tree", "b"),
        mcq("`list.pop()` without index removes:", "First item", "Last item", "Middle item", "Nothing", "b"),
        mcq("A function starts with:", "func", "def", "function", "method", "b"),
        mcq("Function with no `return` returns:", "0", "None", "Empty string", "Error always", "b"),
        mcq("Parameter vs argument:", "Same word always", "Parameter in def; argument in call", "Argument in def only", "Neither used in Python", "b"),
        mcq("Best structure for roll_no → name:", "list", "tuple", "set", "dict", "d"),
        mcq("Best structure for unique IDs:", "list with duplicates", "set", "int only", "float", "b"),
    ],
    "coding": [
        "Build a contact-book **menu** with a dict (add / lookup / delete / list / quit). Missing lookup must not crash. Script style or simple functions OK.",
        "Write `def deposit(balance, amount)` and `def withdraw(balance, amount)` that print a message and return unchanged balance on bad amount/overdraft; otherwise return new balance.",
    ],
    "short": "Why wrap ATM logic in functions instead of one giant script? Two concrete benefits.",
    "short_key": "Reuse (call deposit many times); clearer testing/debugging; fix once vs many copy-paste places.",
}

PAPERS["BW04"] = {
    "mcqs": [
        mcq("`yield` makes a function a:", "List", "Generator", "Class", "Module", "b"),
        mcq("Importing your package usually needs:", "__init__.py (package marker)", "Only .txt files", "MySQL running", "React", "a"),
        mcq("`venv` is for:", "Virtual environment / dependencies", "Version control", "HTML templates", "CSS", "a"),
        mcq("`__init__` in a class:", "Deletes the object", "Runs when instance is created", "Is required for print", "Imports pip", "b"),
        mcq("Encapsulation often uses:", "Public DB passwords in code", "Private-ish attributes + methods", "Only global variables", "No methods", "b"),
        mcq("`super()` is used in:", "Generators only", "Inheritance to call parent", "CSS", "Git merge", "b"),
        mcq("`try`/`except` is for:", "Styling pages", "Handling runtime errors", "Creating tables", "Naming folders", "b"),
        mcq("`raise ValueError(\"msg\")`:", "Ignores errors", "Signals an error intentionally", "Prints only", "Installs packages", "b"),
        mcq("Decorator `@f` above `def g` means:", "g = f(g)", "f = g(f)", "Delete g", "Run MySQL", "a"),
        mcq("`*args` collects extra positional args as a:", "dict", "tuple", "set", "str", "b"),
        mcq("Instance method first parameter is usually:", "self", "cls only", "this", "args", "a"),
        mcq("Polymorphism means:", "One name, different behaviours", "One database", "No classes", "Only inheritance", "a"),
    ],
    "coding": [
        "Write a generator `read_rows(rows)` that `yield`s each dict from an in-memory list (do not return a full new list).",
        "Create `BankAccount` with `__balance`, `deposit`, `withdraw`, `get_balance`. Reject bad amounts with print+return (or raise if you already prefer exceptions).",
    ],
    "short": "Why prefer generators for large row streams instead of `return list(...)`?",
    "short_key": "Memory: yield one row at a time; list loads everything into RAM.",
}

PAPERS["BW05"] = {
    "mcqs": [
        mcq("`with open(...) as f:` mainly helps:", "Faster CPU always", "Auto-close the file", "Skip encoding", "Avoid Python", "b"),
        mcq("CSV rows are often read with:", "csv.DictReader", "django only", "React", "pip freeze", "a"),
        mcq("Logging levels include:", "DEBUG/INFO/WARNING/ERROR", "Only PRINT", "HTML/CSS", "SELECT/INSERT", "a"),
        mcq("`git add` then `git commit`:", "Stages then records a snapshot", "Deletes repo", "Deploys to AWS", "Runs tests only", "a"),
        mcq("`git push` sends commits to:", "Local only", "Remote (e.g. GitHub)", "MySQL", "VS Code theme", "b"),
        mcq("Primary key in SQL uniquely identifies:", "A column type", "A row", "A CSS class", "A React prop", "b"),
        mcq("JOIN is used to:", "Combine related tables", "Style HTML", "Commit git", "Create venv", "a"),
        mcq("Parameterized queries help prevent:", "Slow CSS", "SQL injection", "Git conflicts", "f-string typos", "b"),
        mcq("Custom exception classes usually inherit from:", "str", "Exception", "list", "dict", "b"),
        mcq("`README.md` on GitHub should:", "Be empty", "Explain how to run the project", "Store passwords", "Replace git", "b"),
        mcq("`finally` block runs:", "Only on success", "Only on error", "Usually always after try", "Never", "c"),
        mcq("Foreign key links:", "Two unrelated files", "A column to another table's key", "CSS to HTML only", "Git branches only", "b"),
    ],
    "coding": [
        "Write `add_expense(title, amount, category)` that raises `ValueError` if amount ≤ 0, else appends to a list of simple objects/dicts. Then sketch `export_csv(path)` using `csv.DictWriter`.",
        "Write a safe age reader: convert input to int; if out of 1–120 raise a custom `InvalidAgeError`. Show try/except in a tiny demo loop.",
    ],
    "short": "Why commit often with clear messages during training?",
    "short_key": "History of working states; easy rollback; portfolio proof; collaboration habit for jobs.",
}

PAPERS["BW06"] = {
    "mcqs": [
        mcq("GROUP BY is used with:", "Aggregate functions (COUNT/SUM)", "Only INSERT", "CSS flex", "git rebase", "a"),
        mcq("Python talks to MySQL often via:", "A DB connector / driver", "Only print", "Only HTML", "Only React", "a"),
        mcq("HTML `<form>` usually needs:", "action/method + inputs", "Only CSS", "Only Python classes", "Git tags", "a"),
        mcq("Semantic tag for main page content:", "<div> only forever", "<main>", "<script>", "<style>", "b"),
        mcq("CSS class selector starts with:", "#", ".", "@", "$", "b"),
        mcq("Responsive layouts often use:", "Flexbox / media queries", "Only tables forever", "Git LFS", "SQL JOIN", "a"),
        mcq("`cursor.execute` with `%s` placeholders is:", "Unsafe string build", "Safer parameterization", "CSS", "HTML entity", "b"),
        mcq("HTTP GET vs POST (forms):", "GET for password always", "POST better for sensitive/create data", "Same always", "POST cannot send data", "b"),
        mcq("An ER diagram shows:", "Tables/entities and relationships", "Only CSS colors", "Only git graph", "Only React state", "a"),
        mcq("`alt` on `<img>` is for:", "Decoration only", "Accessibility / when image fails", "SQL keys", "Python imports", "b"),
        mcq("CSS `min-width` media query helps:", "Mobile/desktop layout switches", "Commit messages", "ORM migrations", "venv create", "a"),
        mcq("SQL `WHERE` filters:", "Rows", "Git branches", "CSS files", "JS events", "a"),
    ],
    "coding": [
        "Write an HTML profile page with a form: name, email, phone; labels associated with inputs; submit button.",
        "Write a SQL JOIN query (library style): list member name + book title for active loans (invent sensible table/column names).",
    ],
    "short": "Why keep SQL credentials out of committed code?",
    "short_key": "Security — repos leak; use env vars / secrets; rotate if exposed.",
}

PAPERS["BW07"] = {
    "mcqs": [
        mcq("DOM stands for:", "Document Object Model", "Data Object MySQL", "Django Object Mapper", "Deploy On Main", "a"),
        mcq("`document.querySelector` selects:", "SQL rows", "DOM elements", "Git commits", "venv packages", "b"),
        mcq("Client-side form validation helps:", "Replace all server checks", "Catch bad input early UX", "Deploy Django", "Create migrations", "b"),
        mcq("Django MTV: T is:", "Transaction", "Template", "Terminal", "Tuple", "b"),
        mcq("`python manage.py runserver`:", "Starts Django dev server", "Creates React app", "Drops MySQL", "Pushes git", "a"),
        mcq("URL pattern maps to a:", "View function/class", "CSS file only", "Git hook", "npm package", "a"),
        mcq("`{% extends \"base.html\" %}`:", "Inheritance for templates", "SQL join", "React router", "pip install", "a"),
        mcq("Django model field maps roughly to:", "A DB column", "A CSS class", "A git branch", "An npm script", "a"),
        mcq("`makemigrations` then `migrate`:", "Creates/applies schema changes", "Only collects static", "Only runs tests", "Only opens admin", "a"),
        mcq("Django admin is useful to:", "Quickly CRUD model data", "Replace React", "Host MySQL", "Write CSS", "a"),
        mcq("`HttpResponse` / `render` live in:", "Views", "Settings only", "Gitignore", "Postman only", "a"),
        mcq("Static files are typically:", "CSS/JS/images", "Only migrations", "Only secrets", "Only SQL dumps", "a"),
    ],
    "coding": [
        "Write a tiny JS snippet: on button click, read an input value and show it in a `<p>` (DOM).",
        "Sketch Django: `urlpatterns` for home + about, and two view functions that render templates extending `base.html`.",
    ],
    "short": "Why is server-side validation still required if JS validates the form?",
    "short_key": "JS can be bypassed; attackers POST directly; server is source of truth.",
}

PAPERS["BW08"] = {
    "mcqs": [
        mcq("`login_required` helps:", "Force authentication on views", "Speed CSS", "Create venv", "Write SQL JOINs", "a"),
        mcq("Sessions typically store:", "Server-side login state (via cookie id)", "Only HTML", "Only React props", "Git objects", "a"),
        mcq("CSRF token in Django forms:", "Security against cross-site posts", "Makes CSS pretty", "Replaces migrations", "Opens MySQL port", "a"),
        mcq("Object-level permission means:", "User only edits own rows", "Anyone edits all", "No login ever", "Only admin CSS", "a"),
        mcq("`DEBUG = False` in production:", "Hides detailed errors from users", "Enables debug toolbar for public", "Disables HTTPS need", "Deletes DB", "a"),
        mcq("HTTPS is important because:", "Encrypts traffic", "Makes SQL faster always", "Replaces backups", "Removes auth need", "a"),
        mcq("`collectstatic` is for:", "Gathering static files for deploy", "Creating models", "Writing tests", "npm start", "a"),
        mcq("Capstone kickoff should define:", "Scope, users, milestones", "Only fonts", "Only git emoji", "Only lorem ipsum", "a"),
        mcq("Django messages framework is for:", "One-time user feedback flashes", "SQL joins", "React state", "CSS grid", "a"),
        mcq("Password hashing means:", "Store irreversible password digests", "Save plain text", "Email passwords publicly", "Skip auth", "a"),
        mcq("`ALLOWED_HOSTS` in production:", "Limits which hosts Django serves", "Lists npm packages", "Lists SQL tables", "Lists CSS files", "a"),
        mcq("CRUD stands for:", "Create Read Update Delete", "CSS React Unity Django", "Commit Rebase Undo Drop", "Class Return Use Def", "a"),
    ],
    "coding": [
        "Sketch a Django view that lists Task objects filtered by `owner=request.user` (auth assumed).",
        "List 5 deployment checklist items before going live (settings, secrets, static, DB, HTTPS, …).",
    ],
    "short": "Why filter querysets by the logged-in user for a tasks app?",
    "short_key": "Privacy/security — prevent IDOR; users must not see/edit others' data.",
}

PAPERS["BW09"] = {
    "mcqs": [
        mcq("REST APIs often exchange:", "JSON", "Only CSS", "Only WAV audio", "Git packs", "a"),
        mcq("HTTP 201 usually means:", "Created", "Not found", "Server error", "Redirect forever", "a"),
        mcq("Postman is used to:", "Manually test API requests", "Replace MySQL", "Compile C", "Design only logos", "a"),
        mcq("DRF serializers mainly:", "Validate/convert data", "Style HTML", "Commit git", "Run npm", "a"),
        mcq("Flask is:", "A lightweight Python web framework", "A CSS framework", "A database", "A React hook", "a"),
        mcq("React component state updates should:", "Use setState/useState", "Edit DOM with innerHTML always", "Restart MySQL", "Change git remote", "a"),
        mcq("`useEffect` often handles:", "Side effects / fetch on mount", "SQL indexes", "CSS only", "pip install", "a"),
        mcq("CORS errors appear when:", "Browser blocks cross-origin API calls", "Python syntax wrong", "Git not installed", "f-string missing", "a"),
        mcq("React Router is for:", "Client-side page routes", "MySQL routing", "Django admin only", "Logging levels", "a"),
        mcq("JWT/token APIs usually send token in:", "Authorization header (common pattern)", "CSS file", "Git tag", "HTML comment only", "a"),
        mcq("Idempotent GET means:", "Safe to repeat without changing server state", "Always deletes data", "Only works offline", "Requires CSS", "a"),
        mcq("Props in React are:", "Inputs from parent to child", "SQL primary keys", "Git remotes", "venv names", "a"),
    ],
    "coding": [
        "Write a minimal Flask (or sketch) JSON endpoint `GET /notes` returning a list of note dicts.",
        "Write a React function component that shows a product name from props and a quantity in `useState`, with + button.",
    ],
    "short": "Why is CORS a browser rule, and what must the API allow for a Vite React app on another port?",
    "short_key": "Browsers enforce same-origin; API must send Access-Control-Allow-Origin (and methods/headers) for the frontend origin.",
}

PAPERS["BW10"] = {
    "mcqs": [
        mcq("`unittest` assertions check:", "Expected vs actual behaviour", "CSS colors", "Git blame", "SQL charset only", "a"),
        mcq("A good unit test is:", "Fast, focused, repeatable", "Needs production DB always", "Manual only", "One giant test for whole app only", "a"),
        mcq("Clean code prefers:", "Clear names + small functions", "One 2000-line function", "Copy-paste everywhere", "No comments when complex forever", "a"),
        mcq("Debugging first step often is:", "Reproduce + read the error", "Rewrite entire app", "Delete git history", "Disable HTTPS", "a"),
        mcq("AI coding assistants are best used to:", "Accelerate with your review", "Blindly ship secrets", "Skip learning basics", "Replace code review forever", "a"),
        mcq("Resume bullet for projects should show:", "Impact + tech + your role", "Only course name", "Only soft skills adjectives", "Passwords", "a"),
        mcq("STAR method is for:", "Interview storytelling", "SQL joins", "CSS grid", "React keys", "a"),
        mcq("`assertRaises` tests:", "That code raises an expected exception", "That CSS loads", "That git pushes", "That npm builds", "a"),
        mcq("Technical interview prep should include:", "Explaining your project end-to-end", "Memorizing only buzzwords", "Avoiding GitHub", "Hiding bugs always", "a"),
        mcq("Logging in tests/prod helps:", "Diagnose failures", "Replace unit tests completely", "Style pages", "Create React apps", "a"),
        mcq("A portfolio README should include:", "Setup steps + screenshots/demo", "Only your photo", "API keys", "Unrelated memes only", "a"),
        mcq("Mock interviews help because:", "Practice under pressure + feedback", "Replace building projects", "Skip fundamentals", "Avoid speaking English", "a"),
    ],
    "coding": [
        "Write two `unittest` methods for a function `average(marks)`: one normal list, one empty list expecting `ValueError`.",
        "Write a 4-bullet project description for your full-stack capstone (problem, stack, your features, result).",
    ],
    "short": "Name three things you will demo in a placement mock for your capstone.",
    "short_key": "Login/auth path; core CRUD; one API or React screen; deploy URL or local run; what you learned / tradeoffs.",
}


def _diversify_answer_letters() -> None:
    """Rotate options so correct answers are not always letter a."""
    letters = "abcd"
    for paper in PAPERS.values():
        for i, item in enumerate(paper["mcqs"]):
            shift = i % 4
            if shift == 0:
                continue
            opts = item["opts"]
            vals = [opts[l] for l in letters]
            vals = vals[shift:] + vals[:shift]
            item["opts"] = {letters[j]: vals[j] for j in range(4)}
            old_idx = letters.index(item["ans"])
            item["ans"] = letters[(old_idx - shift) % 4]


_diversify_answer_letters()


def render_paper(bw_id: str) -> str:
    meta = BW_META[bw_id]
    paper = PAPERS[bw_id]
    lines = [
        f"# {meta['title']}",
        "",
        f"**Sessions covered:** {meta['sessions']}  ",
        f"**Topics:** {meta['topics']}",
        "",
        "**Timebox:** 45–60 minutes (homework or Friday of the even week).  ",
        "**Rules:** Closed notes unless your trainer allows open notes. No copying.  ",
        f"**Coding constraint:** {meta['coding_note']}",
        "",
        "---",
        "",
        "## A. Multiple Choice (12)",
        "",
        "Circle the best option.",
        "",
    ]
    for i, item in enumerate(paper["mcqs"], 1):
        lines.append(f"{i}. {item['q']}")
        for letter in "abcd":
            lines.append(f"   {letter}) {item['opts'][letter]}")
        lines.append("")
    lines += [
        "---",
        "",
        "## B. Coding (2)",
        "",
    ]
    for i, prompt in enumerate(paper["coding"], 1):
        lines.append(f"{i}. {prompt}")
        lines.append("")
        lines.append("```python")
        lines.append("# your code")
        lines.append("```")
        lines.append("")
    lines += [
        "---",
        "",
        "## C. Short answer (1)",
        "",
        paper["short"],
        "",
        "_(Write 3–6 sentences.)_",
        "",
    ]
    return "\n".join(lines)


def render_key(bw_id: str) -> str:
    meta = BW_META[bw_id]
    paper = PAPERS[bw_id]
    lines = [
        f"# KEY — {meta['title']} (Trainer only)",
        "",
        "**Do not share with students.** Excluded from student pack (`*_KEY.md`).",
        "",
        "## A. MCQ answers",
        "",
    ]
    for i, item in enumerate(paper["mcqs"], 1):
        letter = item["ans"]
        lines.append(f"{i}. **{letter}** — {item['opts'][letter]}")
    lines += [
        "",
        "## B. Coding — model points",
        "",
    ]
    for i, prompt in enumerate(paper["coding"], 1):
        lines.append(f"{i}. {prompt}")
        lines.append("   - Award marks for correctness + teaching-order constraints respected.")
        lines.append("")
    lines += [
        "## C. Short answer — model",
        "",
        paper["short_key"],
        "",
        "## Suggested scoring",
        "",
        "| Section | Marks |",
        "|---------|------:|",
        "| A MCQ (1 each) | 12 |",
        "| B Coding (6 each) | 12 |",
        "| C Short | 6 |",
        "| **Total** | **30** |",
        "",
    ]
    return "\n".join(lines)


def pointer_block(bw_id: str, when: str, rel_prefix: str) -> str:
    meta = BW_META[bw_id]
    return (
        f"## Biweekly Assessment\n\n"
        f"**Next graded check:** [{bw_id}]({rel_prefix}{meta['file']}) "
        f"({when} — sessions {meta['sessions']}).  \n"
        f"Interview practice stays in this module; graded MCQ/coding lives in "
        f"[16_Assessments]({rel_prefix}README.md).\n"
    )


ASSESSMENT_RE = re.compile(r"^## Assessment\s*\n.*?(?=^## |\Z)", re.M | re.S)


def strip_and_point(path: Path, bw_id: str, when: str, rel_prefix: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if "## Assessment" not in text and "## Biweekly Assessment" in text:
        return False
    new = ASSESSMENT_RE.sub(pointer_block(bw_id, when, rel_prefix), text)
    # If no Assessment section existed, insert before Interview
    if new == text and "## Biweekly Assessment" not in text:
        pointer = pointer_block(bw_id, when, rel_prefix)
        if re.search(r"^## Interview", text, re.M):
            new = re.sub(r"(^## Interview)", pointer + r"\n\1", text, count=1, flags=re.M)
        else:
            new = text.rstrip() + "\n\n" + pointer
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def rel_to_assessments(module_path: Path) -> str:
    # PYTHON/xx/yy.md -> ../16_Assessments/ or ../../ etc
    depth = len(module_path.relative_to(FS).parts) - 1
    return "../" * depth + "16_Assessments/"


def main() -> None:
    ASSESS.mkdir(parents=True, exist_ok=True)

    readme = """# Biweekly Assessments (Graded)

**Purpose:** One graded check every **2 weeks** covering topics taught in that window — instead of an Assessment section inside every module.

**How trainers run it**

1. Assign the paper as **homework** after the even week (or use Friday exit + finish at home).
2. Students get `BW##_….md` only (no `*_KEY.md`).
3. Mark with the matching `*_KEY.md` (trainer tree / private folder).
4. Review weak MCQ topics for 10 minutes next Monday.

**Cadence**

| ID | After week | Sessions | Paper |
|----|------------|----------|-------|
| BW01 | 2 | S01–10 | [BW01_Weeks_01_02_Foundations_Setup.md](BW01_Weeks_01_02_Foundations_Setup.md) |
| BW02 | 4 | S11–20 | [BW02_Weeks_03_04_Flow_Strings_Lists.md](BW02_Weeks_03_04_Flow_Strings_Lists.md) |
| BW03 | 6 | S21–30 | [BW03_Weeks_05_06_Collections_Functions.md](BW03_Weeks_05_06_Collections_Functions.md) |
| BW04 | 8 | S31–40 | [BW04_Weeks_07_08_Advanced_OOP_Exceptions.md](BW04_Weeks_07_08_Advanced_OOP_Exceptions.md) |
| BW05 | 10 | S41–50 | [BW05_Weeks_09_10_Files_Git_MySQL.md](BW05_Weeks_09_10_Files_Git_MySQL.md) |
| BW06 | 12 | S51–60 | [BW06_Weeks_11_12_SQL_Frontend.md](BW06_Weeks_11_12_SQL_Frontend.md) |
| BW07 | 14 | S61–70 | [BW07_Weeks_13_14_JS_Django_Core.md](BW07_Weeks_13_14_JS_Django_Core.md) |
| BW08 | 16 | S71–80 | [BW08_Weeks_15_16_Auth_Deploy_Capstone.md](BW08_Weeks_15_16_Auth_Deploy_Capstone.md) |
| BW09 | 18 | S81–90 | [BW09_Weeks_17_18_APIs_React.md](BW09_Weeks_17_18_APIs_React.md) |
| BW10 | 20 | S91–100 | [BW10_Weeks_19_20_Testing_Placement.md](BW10_Weeks_19_20_Testing_Placement.md) |

**Shape (every paper):** 12 MCQs + 2 coding tasks + 1 short answer (≈30 marks).

**Modules** keep Interview & Discussion for oral practice and link here via **Biweekly Assessment** pointers.
"""
    (ASSESS / "README.md").write_text(readme, encoding="utf-8")

    for bw_id in BW_META:
        meta = BW_META[bw_id]
        paper_path = ASSESS / meta["file"]
        key_path = ASSESS / meta["file"].replace(".md", "_KEY.md")
        paper_path.write_text(render_paper(bw_id), encoding="utf-8")
        key_path.write_text(render_key(bw_id), encoding="utf-8")
        print("wrote", paper_path.name, key_path.name)

    changed = 0
    for rel, (bw_id, when) in MODULE_BW.items():
        path = FS / rel
        if not path.exists():
            print("skip missing", rel)
            continue
        prefix = rel_to_assessments(path)
        if strip_and_point(path, bw_id, when, prefix):
            changed += 1
            print("updated", rel)

    for rel, (bw_id, when) in FRONTEND_BW.items():
        path = FRONTEND / rel
        if not path.exists():
            print("skip missing FRONTEND", rel)
            continue
        # FRONTEND/HTML_CSS/... -> ../PYTHON/16_Assessments/
        depth = len(Path(rel).parts) - 1
        prefix = "../" * (depth + 1) + "PYTHON/16_Assessments/"
        if strip_and_point(path, bw_id, when, prefix):
            changed += 1
            print("updated FRONTEND/" + rel)

    print(f"modules_updated={changed}")


if __name__ == "__main__":
    main()
