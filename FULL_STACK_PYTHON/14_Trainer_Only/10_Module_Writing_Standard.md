# Module Writing Standard — What / Why Before Syntax

**Purpose:** Keep `FULL_STACK_PYTHON/` teachable for live class — What/Why, labs, and modern safe Python (without legacy note patterns).

**Reference:** [01_Functions_Decorators_Generators.md](../03_Advanced_Python/01_Functions_Decorators_Generators.md) · Core modules with What/Why openings.

---

## Required module section order

| # | Section | Notes |
|---|---------|--------|
| 1 | Title + Duration (Session Calendar) + Previous/Next | No Audience / Program spam |
| 2 | Learning Outcomes | What they can do after the module |
| 3 | **Classroom Ticket** | Lab kit first |
| 4 | Start with **What / Why** (no “Beginner-Friendly” label) | What + Why |
| 5 | Important Concepts (+ **Try these** after each topic) | What/Why → syntax → **Note** → ≥2 programs per topic |
| 6 | Step-by-Step annotated code | Longer demos (Core often merges topics here) |
| 7 | Practice Exercises | Basic → Intermediate → Interview; each item has **Model answer:** (stripped in student pack). **Before** Mini-Project |
| 8 | Mini-Project | Lab kit link + What to build + Stretch + **Done when**. This **is** the homework |
| 9 | **Revision Map — Memorize / Understand / Practise / Build** | Near the end, not the open |
| 10 | Assignment | **Only if** there is no Mini-Project |
| 11 | **Interview & Discussion Q&A** | Discuss in class + interview answers |

**Do not add** a standalone `## Common Mistakes` section. Put traps next to the sub-topic as **Note:** bullets (see below).

**Graded tests** live only in [`16_Assessments/`](../16_Assessments/) (one paper every 2 weeks). Do **not** put `## Assessment` or `## Biweekly Assessment` inside modules — trainers assign papers from the calendar + assessments README.

**Do not add:** Discussion Questions (separate), Trainer Tips, Trainer Demo Plan, or Real-World Use Cases tables.

**Delivery timing** lives once in the [Session Calendar](../00_Course_Guide/11_Session_Calendar_100.md) and [Daily Lesson Plan Template](04_Daily_Lesson_Plan_Template.md) — not repeated in every module.

---

## Required teaching order (every concept block)

| Step | Section cue | Learner should leave knowing |
|------|-------------|------------------------------|
| 1 | **What is …?** | Plain-English definition + one job example |
| 2 | **Why do we need …?** | Pain without it vs win with it |
| 3 | **Kinds / cases** (if any) | Built-in vs user-defined, modes, arg types, … |
| 4 | **How (syntax + small demo)** | Minimal modern Python 3 |
| 5 | **Note** (inline) | 1–3 bullets right after syntax or before Try these — interview traps for **this** topic only |
| 6 | **Table only after prose** | Tables summarise |

**Forbidden cold open:** parameter table / mode matrix / bare `def` with no What/Why.

### Inline pitfalls (replaces Common Mistakes)

After teaching a concept (syntax + short demo), add a short note block — not a module-end dump:

```markdown
**Note:**
- Wrong: …
- Prefer: …
```

- Keep it local to the sub-topic so live class matches how you teach.
- Do **not** also maintain `## Common Mistakes` (or `## Common Mistakes and How to Fix Them`).
- Optional: one trap can sit under a Step-by-Step demo if that demo owns the concept.

---

## Try these (2 programs) — required after each topic

After every major concept block (`### 1. …` / `### Step N: …`), add **two complete runnable programs** (not prompts only):

```markdown
**Try these (2 programs):**

**Program 1 — Short title**

```python
# complete runnable Python 3
print(...)
```

**Program 2 — Short title**

```python
# complete runnable Python 3
print(...)
```
```

- Short (typically 5–20 lines), copy-paste runnable.
- India-relevant examples OK (INR, student marks, ATM, names like Priya/Ravi).
- Point to a lab kit when the exercise matches a ticket.
- **Practice Exercises:** every numbered item must include `**Model answer:**` (prose and/or a fenced code block). Student pack strips these via `strip_trainer_sections.py`.

---

## Mini-Project shape

| Piece | Required |
|-------|----------|
| Title | Portfolio-friendly name |
| Lab kit link | `15_Lab_Assets/…` when a kit exists |
| What to build | Table or bullets with acceptance detail |
| Stretch | 1–3 optional upgrades |
| Done when | Checkbox list learners can self-check |

**Order:** Practice Exercises → Mini-Project (never reverse). Practice = short drills; Mini-Project = homework / portfolio Done when.

Mini-Project **is** the homework when present — do not also add a separate Assignment.

---

## Do **not** repeat on every module

| Noise | Put it here instead |
|-------|---------------------|
| Audience labels (fresher / switcher / beginner) | Avoid in modules; one unified learner voice |
| Full Prerequisites list | Session Calendar; Previous/Next in header |
| Absolute week numbers / old hour clocks | [11_Session_Calendar_100.md](../00_Course_Guide/11_Session_Calendar_100.md) |
| Memorize table at the top | Revision Map before Assessment |
| Trainer Demo Plan | Calendar + Daily Lesson Plan Template |

### When Prerequisites **are** allowed

Phase jumps / external tooling only — **2 bullets max** (GitHub, MySQL, Node, optional AI, placement readiness).

---

## Tone and safety

- Short sentences; **one voice for all learners** — never “fresher vs experienced” tracks.  
- Modern safe patterns (`int(input)`, named `except` after Exceptions week, no `eval`).  
- Absorb PDF pedagogy — not unsafe snippets.  
- Schedule follows the Session Calendar.

### Teaching-order rule (Classroom Ticket / lab kits)

A kit attached to calendar session **S** may only require syntax/APIs taught in sessions **1…S**. This applies to **every** topic — not only exceptions.

- **Core path** (`starter/`, `broken/` student work, `solution/`, Done when): prior concepts only.  
- **Stretch:** may preview later topics — label clearly (e.g. “Later — Files week”).  
- **Before Flow Control (S11):** no `if` / `while` / `for` / `def` in core path — linear scripts.  
- **Before Functions (S28):** no `def` / `global` / type hints in Core kits — menu scripts and top-level statements.  
- **Before Exceptions (S40):** no `try` / `except` / `raise` (including `raise NotImplementedError` stubs — use `pass` / `return` / `if False: yield`).  
- **Before Files (S42):** no `open` / `with` / `csv` / `pathlib` in generator labs — yield in-memory rows; CSV is Stretch.  
- **Do not require** type hints, `X | Y` unions, `dataclass`, or `assert` in learner Done when (optional trainer smoke only).  
- **From S40 onward:** `try`/`except`/`raise` OK (`18_safe_input_exceptions` and later).

---

## Checklist — classroom-ready

- [ ] Section order matches the table above  
- [ ] Classroom Ticket → lab kit  
- [ ] Ticket / lab starter+solution stay within calendar teaching order (no forward concepts)  
- [ ] What/Why before first big table (no “Beginner-Friendly” heading)  
- [ ] **Try these (2 programs)** after each topic / Step  
- [ ] **Note** next to each major sub-topic (no standalone Common Mistakes)  
- [ ] Practice Exercises include **Model answer:** under each item (trainer copy)  
- [ ] Practice appears **before** Mini-Project  
- [ ] Mini-Project: lab kit + Done when (+ Stretch)  
- [ ] Revision Map near the end  
- [ ] No Biweekly/Assessment MCQ block in the module (use `16_Assessments/`)  
- [ ] No Demo Plan / Tips / Discussion / Real-World appendix  
- [ ] No fresher / switcher / beginner audience splits in learner text  
- [ ] Student pack strips interview answers / `solution/` / `*_KEY.md`
