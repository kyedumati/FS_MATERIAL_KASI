# Module Writing Standard — Definition / Purpose Before Syntax

**Purpose:** Keep `FULL_STACK_PYTHON/` teachable for live class — Definition/Purpose, labs, and modern safe Python (without legacy note patterns).

**Reference:** [01_Functions_Decorators_Generators.md](../03_Advanced_Python/01_Functions_Decorators_Generators.md) · Core modules with Definition/Purpose openings.

---

## Required module section order

| # | Section | Notes |
|---|---------|--------|
| 1 | Title + Phase + Previous/Next | No Audience / Program / Duration — timing lives in Session Calendar only |
| 2 | Learning Outcomes | What they can do after the module |
| 3 | Start with **Definition / Purpose** (or Motivation) | Definition + Purpose — no Classroom Ticket section |
| 4 | Important Concepts (+ **Try these** after each topic) | Definition/Purpose → syntax → **Note** → ≥2 programs per topic |
| 5 | Step-by-Step annotated code | Longer demos (Core often merges topics here) |
| 6 | Practice Exercises | Heading must be exactly `## Practice Exercises` (not `## Practice`). Basic → Intermediate → Interview; each item has **Model answer:** (shared — one material). **Before** Mini-Project |
| 7 | **Mini-Project (Assignment)** | Same section — take-home / homework. Heading: `## Mini-Project (Assignment): Title`. Lab kit + What to build + Stretch + **Done when** |
| 8 | Assignment (standalone) | Use `## Assignment` **only if** the module has no Mini-Project (e.g. some Django lab days) |
| 9 | **Interview Q&A** | Shared with students (Q + A). Share with the module PDF after concepts + mini-project |

**Do not add** a standalone `## Common Mistakes` section. Put traps next to the sub-topic as **Note:** bullets (see below).

**Do not add** a **Revision Map** table — redundant with Key takeaways callouts, Practice, and Interview Q&A.

**Do not add** a **Classroom Ticket** section — lab kits are linked from the Session Calendar, Mini-Project, and `15_Lab_Assets/`.

**Graded tests** live only in [`16_Assessments/`](../16_Assessments/) (one paper every 2 weeks). Do **not** put `## Assessment` or `## Biweekly Assessment` inside modules — trainers assign papers from the calendar + assessments README.

**Do not add:** Discussion Questions (separate), Trainer Tips, Trainer Demo Plan, or large Real-World Use Cases **tables**. Prefer a short `**Where used?**` callout instead (see PDF markers above).

**Delivery timing / session numbers (S01–S100)** live only in the [Session Calendar](../Session_Calendar_100.md) — **not** in module headers, Learning Outcomes, or learner-facing notes.

---

## Required teaching order (every concept block)

| Step | Section cue | Learner should leave knowing |
|------|-------------|------------------------------|
| 1 | **Definition:** | Plain-English definition + one job example |
| 2 | **Purpose:** | Pain without it vs win with it (why this idea exists) |
| 3 | **Kinds / cases** (if any) | Built-in vs user-defined, modes, arg types, … |
| 4 | **How (syntax + small demo)** | Minimal modern Python 3 |
| 5 | **Note** (inline) | 1–3 bullets right after syntax or before Try these — interview traps for **this** topic only |
| 6 | **Table only after prose** | Tables summarise |

**Forbidden cold open:** parameter table / mode matrix / bare `def` with no Definition/Purpose.

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
- **Practice Exercises:** every numbered item must include `**Model answer:**` (prose and/or a fenced code block). Same notes are shared with students (PDF after the module).
- After a program that prints, prefer an **Expected Output:** fence so PDF learners can self-check:

```markdown
**Expected Output:**

```
Priya
```
```

---

## PDF callout markers (styled by `scripts/build_pdfs.py`)

Use these exact bold labels (standalone paragraphs). They render as coloured boxes in student PDFs:

| Marker | Use for |
|--------|---------|
| `**Expected Output:**` + fence | Self-check prints after demos |
| `**Remember:**` | One-liner to keep (`self` = current object) |
| `**Interview:**` | Short interview cue |
| `**Common Error:**` | Classic trap (mutable class list, etc.) |
| `**Where used?**` | 3–5 real domains (Banking, Ecommerce, …) — **not** a big Use Cases table |
| `**Icons:** Bank · UPI · Employee · Laptop · Order` | Optional chip strip (also Hospital · Payroll · CRM) |
| `**Key takeaways:**` | 2–4 bullets **immediately after** a Mermaid diagram (paired beside it in PDF). Major ideas only — not every sub-topic |

**Practice answers:** after `**Model answer:**` / `**Expected Output:**`, put a blank line then a fenced block at **column 0**. Do **not** indent `` ``` `` under the list item — Cursor/VS Code preview often renders indented fences as empty.

**Program titles** must be one bold line: `**Program 1 — Book with info()**` (do not split around inline code).

Core/Advanced Python: avoid Django/framework forward-selling; introduce frameworks in their own phase modules.

---

## Mini-Project (Assignment) shape

Use one heading so students always see the word **Assignment**:

```markdown
## Mini-Project (Assignment): Portfolio-Friendly Title
```

| Piece | Required |
|-------|----------|
| Title | Portfolio-friendly name (in the heading) |
| Lab kit link | `15_Lab_Assets/…` when a kit exists |
| What to build | Table or bullets with acceptance detail |
| Stretch | 1–3 optional upgrades |
| Done when | Checkbox list learners can self-check |

**Order:** Practice Exercises → Mini-Project (Assignment) (never reverse).  
Practice = short drills. **Mini-Project (Assignment)** = take-home homework / portfolio **Done when**.

Do **not** add a second `## Assignment` section when a Mini-Project already exists — they are the same deliverable.

---

## Interview Q&A shape

One shared section (no separate Discuss / Interview-answers headings):

```markdown
## Interview Q&A

Shared with students after concepts and the mini-project. Use for review and interview prep — questions and model answers are included.

**Q1. …?**  
**A:** …

**Q2. …?**  
**A:** …
```

- Hand out **after** teaching concepts + mini-project.
- **Q + A are part of the same shared notes** (PDF after the module). Practice **Model answer** blocks are shared too (one material).

---

## Do **not** repeat on every module

| Noise | Put it here instead |
|-------|---------------------|
| Audience labels (fresher / switcher / beginner) | Avoid in modules; one unified learner voice |
| Full Prerequisites list | Session Calendar; Previous/Next in header |
| Absolute week numbers / old hour clocks | [Session_Calendar_100.md](../Session_Calendar_100.md) |
| Memorize / revision tables at module end | Dropped — use Key takeaways (after diagrams) + Practice + Interview Q&A |
| Trainer Demo Plan | Calendar + Daily Lesson Plan Template |

### When Prerequisites **are** allowed

Phase jumps / external tooling only — **2 bullets max** (GitHub, MySQL, Node, optional AI, placement readiness).

---

## Tone and safety

- Short sentences; **one voice for all learners** — never “fresher vs experienced” tracks.  
- Modern safe patterns (`int(input)`, named `except` after Exceptions week, no `eval`).  
- Absorb PDF pedagogy — not unsafe snippets.  
- Schedule follows the Session Calendar.

### Teaching-order rule (lab kits)

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
- [ ] No Classroom Ticket section (labs via calendar / Mini-Project / `15_Lab_Assets/`)  
- [ ] Ticket / lab starter+solution stay within calendar teaching order (no forward concepts)  
- [ ] Definition/Purpose before first big table (no “Beginner-Friendly” heading)  
- [ ] **Try these (2 programs)** after each topic / Step  
- [ ] **Note** next to each major sub-topic (no standalone Common Mistakes)  
- [ ] Practice Exercises include **Model answer:** under each item  
- [ ] Practice appears **before** Mini-Project (Assignment)  
- [ ] Mini-Project (Assignment): lab kit + Done when (+ Stretch) — or standalone `## Assignment` if no mini-project  
- [ ] No Revision Map table (redundant)  
- [ ] No Biweekly/Assessment MCQ block in the module (use `16_Assessments/`)  
- [ ] Interview Q&A: shared Q + A; share module PDF after concepts + mini-project  
- [ ] No Demo Plan / Tips / separate Discussion appendix / Real-World appendix  
- [ ] No fresher / switcher / beginner audience splits in learner text  
- [ ] No session numbers (S01–S100) in module notes — timing only in Session Calendar  
- [ ] Private only: `14_Trainer_Only/` · `solution/` · `*_KEY.md` (never share those)
