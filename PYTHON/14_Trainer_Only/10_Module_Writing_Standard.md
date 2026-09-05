# Module Writing Standard — Definition / Purpose Before Syntax

**Purpose:** Keep `PYTHON/` teachable in a **75-minute** live class — Definition/Purpose, type-along code, one lab kit. Do not flatten notes into an outline.

**Reference (live type-along):** [01_Functions_Decorators_Generators.md](../03_Advanced_Python/01_Functions_Decorators_Generators.md)  
**Reference (one assemble, no triple demo):** [04_Exception_Handling.md](../03_Advanced_Python/04_Exception_Handling.md)

---

## Live class first (do not flatten)

Slimming means **stop repeating the same program**. It does **not** mean replacing runnable code with discussion prompts.

Keep:

- Short programs students type with you
- **Expected Output:** on the projector
- Named products, INR, ATM / UPI / canteen stories
- **Note:** traps next to the demo

Class shape (same as Session Calendar): 5 min kit → **25 min type-along** → **35 min lab** → 10 min exit.

Type **Try these** and the assemble into the **batch workspace** (running code). Use **OpenBoard** for running notes. Commit that workspace after class. Do not commit class scribbles into these module files.

| When | Open | Not in class |
|------|------|----------------|
| Live (25 min) | Concepts + **Try these** | Second copy of the same program |
| Live (35 min) | Lab `starter/` | Pasted `solution/` in the notes |
| Tonight | Mini-project = **that kit** | Practice that rebuilds the demo |
| Mocks | Interview Q&A | Interview-style items inside Practice |

---

## Required module section order

| # | Section | Notes |
|---|---------|--------|
| 1 | Title + Phase + Previous/Next | No Audience / Program / Duration — timing lives in Session Calendar only |
| 2 | **Module Outcome** | `**Module Outcome:**` + bullets that **name the high-level topics** taught in this module (match the `##` / `###` concept headings). Immediately after the header `---`. Not Bloom “can explain/apply” skills |
| 3 | Start with **Definition / Purpose** (or Motivation) | Definition + Purpose — no Classroom Ticket section |
| 4 | Important Concepts (+ **Try these**) | Definition/Purpose → syntax → **Note** → type-along (see below) |
| 5 | Step-by-Step annotated code | **One** assemble that stitches today’s ideas (Core may *be* the lesson spine) |
| 6 | Practice Exercises | Heading exactly `## Practice Exercises`. Transfer drills, **4–6 items**, each with **Model answer:**. **Before** Mini-Project |
| 7 | **Mini-Project (Assignment)** | Full take-home ticket (story, kit, what to build, sample run, Stretch, Done when). Do not paste the class assemble or `solution/` |
| 8 | Assignment (standalone) | Use `## Assignment` **only if** the module has no Mini-Project (e.g. some Django lab days) |
| 9 | **Interview Q&A** | Shared Q + A. Oral layer only — do not copy these items into Practice |

**Do not add** a standalone `## Common Mistakes` section. Put traps next to the sub-topic as **Note:** bullets (see below).

**Do not add** a **Revision Map** table — redundant with Key takeaways callouts, Practice, and Interview Q&A.

**Do not add** a **Classroom Ticket** section — lab kits are linked from the Session Calendar, Mini-Project, and `15_Lab_Assets/`.

**Graded tests** live only in [`16_Assessments/`](../16_Assessments/) (one paper every 2 weeks). Do **not** put `## Assessment` or `## Biweekly Assessment` inside modules — trainers assign papers from the calendar + assessments README.

**Do not add:** Discussion Questions (separate), Trainer Tips, Trainer Demo Plan, or large Real-World Use Cases **tables**. Prefer a short `**Where used?**` callout instead (see PDF markers above).

**Do not add** a Bloom-style **Learning Outcomes** list or a **Teaching note** paragraph. Use **Module Outcome** (high-level topic list) at the start instead.

**Delivery timing / session numbers (S01–S100)** live only in the [Session Calendar](../Session_Calendar_100.md) — **not** in module headers or learner-facing notes.

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

## Try these — live type-along (keep the energy)

After every major concept block (`### 1. …` / `### Step N: …`), students type **at least one** complete runnable program (not a prompt only).

Do **not** use a `**Try these:**` heading or `**Program N — Short title**` labels. Instead, write a **1–2 sentence requirement** immediately before each code fence — what the learner must build (imperative voice: *Print…*, *Store…*, *Write a function that…*).

```markdown
Store Ravi's roll number, name, and two subject marks, then print his average to two decimal places.

```python
# complete runnable Python 3
roll = "2026002"
name = "Ravi"
...
```
```

Add a **second** program only when it shows a *different* case (success vs fail, a second exception type, `finally` after `return`) — not Program 1 with new variable names. Put a separate requirement line before each program; no shared heading.

- Short (typically 5–20 lines), copy-paste runnable.
- India-relevant examples OK (INR, student marks, ATM, names like Priya/Ravi).
- **Named products (soft-apply):** when the example is business-shaped, prefer **Employee Management Portal**, **Swiggy**, **Apollo Hospitals**, **HDFC Bank**, or **PhonePe** in `**Where used?**`, program titles, Interview Q&A, and mini-project tickets. Do not force syntax-only drills. See [12_Named_Product_Domains.md](12_Named_Product_Domains.md). Canonical schemas: [`MYSQL/12_Real_Time_Projects.md`](../../MYSQL/12_Real_Time_Projects.md). CampusCart stays the capstone (college Swiggy-style storefront).
- Point to a lab kit when the exercise matches a ticket.
- After a program that prints, prefer an **Expected Output:** fence so PDF learners can self-check:

```markdown
**Expected Output:**

```
Priya
```
```

**Requirement lines** must stand alone as plain paragraphs (one or two sentences). Do not wrap them in bold labels.

Core/Advanced Python: avoid Django/framework forward-selling; introduce frameworks in their own phase modules.

---

## Step-by-Step — one assemble

This is the **live “now we put it together”** block — still typed, still with Expected Output. It is not a second textbook.

| Do | Do not |
|----|--------|
| **One** program (or 2–3 short steps of the *same* story) that stitches today’s ideas | Example 1…6 that replay each concept |
| Core: this section may *be* the lesson spine (one idea per Step + Try these inside) | A second gallery after that spine |
| If a lab kit exists: after the assemble, say what to open in `starter/` | Paste `solution/` or rebuild the mini-project here |

---

## Practice Exercises — transfer, not replay

Heading must be exactly `## Practice Exercises` (not `## Practice`).

- **4–6 items.** New domain, a twist, or two ideas combined.
- Every numbered item includes `**Model answer:**` (prose and/or a fenced code block). Same notes are shared with students (PDF after the module).
- **No** Basic / Intermediate / Interview subheadings. **No** Interview-style block (that is Interview Q&A).
- Must not be the class demo with renamed variables.

**Practice answers:** after `**Model answer:**` / `**Expected Output:**`, put a blank line then a fenced block at **column 0**. Do **not** indent `` ``` `` under the list item — Cursor/VS Code preview often renders indented fences as empty.

---

## PDF callout markers (styled by `scripts/build_pdfs.py`)

Use these exact bold labels (standalone paragraphs). They render as coloured boxes in student PDFs:

| Marker | Use for |
|--------|---------|
| `**Expected Output:**` + fence | Self-check prints after demos |
| `**Remember:**` | One-liner to keep (`self` = current object) |
| `**Interview:**` | Short interview cue |
| `**Common Error:**` | Classic trap (mutable class list, etc.) |
| `**Module Outcome:**` | High-level **topic list** at the **module start** (after header) — names of concepts inside this file, not Bloom “can do” skills |
| `**Where used?**` | 3–5 real domains that **name** Employee Management Portal / Swiggy / Apollo Hospitals / HDFC Bank / PhonePe when business-shaped — **not** a big Use Cases table |
| `**Icons:** Bank · UPI · Employee · Laptop · Order` | Optional chip strip (also Hospital · Payroll · CRM) |
| `**Key takeaways:**` | 2–4 bullets **immediately after** a Mermaid diagram (paired beside it in PDF). Major ideas only — not every sub-topic |

---

## Mini-Project (Assignment) shape

Use one heading so students always see the word **Assignment**:

```markdown
## Mini-Project (Assignment): Portfolio-Friendly Title
```

| Piece | Required |
|-------|----------|
| Heading | `## Mini-Project (Assignment): Portfolio-Friendly Title` |
| Story | Who needs this (named product) and what “never crash” looks like |
| Lab kit | `15_Lab_Assets/…` — `starter/` and `broken/` when they exist. Tell them not to paste `solution/` |
| What to build | Table or bullets with acceptance detail (functions, exceptions, demo loop) |
| Sample run | Expected prints for the happy path and the failure cases |
| Stretch | 1–3 optional upgrades |
| Done when | Checkbox list learners can self-check |

Do **not** paste the Step-by-Step assemble or the kit `solution/` here. The ticket should be complete enough to build from — not a one-line link.

**Order:** Practice Exercises → Mini-Project (Assignment) (never reverse).  
Practice = gym on a *different* ticket. **Mini-Project** = tonight’s product (usually the lab kit).

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
- **Before Exceptions (S41):** no `try` / `except` / `raise` (including `raise NotImplementedError` stubs — use `pass` / `return` / `if False: yield`).  
- **Before Files (S42):** no `open` / `with` / `csv` / `pathlib` in generator labs — yield in-memory rows; CSV is Stretch.  
- **Do not require** type hints, `X | Y` unions, `dataclass`, or `assert` in learner Done when (optional trainer smoke only).  
- **From S41 onward:** `try`/`except`/`raise` OK (`18_safe_input_exceptions` and later).

---

## Checklist — classroom-ready

- [ ] Section order matches the table above  
- [ ] Notes still type-along (runnable programs + Expected Output) — not an outline  
- [ ] No Classroom Ticket section (labs via calendar / Mini-Project / `15_Lab_Assets/`)  
- [ ] **Module Outcome:** (high-level topics taught in this module) immediately after the header  
- [ ] No Bloom Learning Outcomes list and no Teaching note paragraph  
- [ ] Ticket / lab starter+solution stay within calendar teaching order (no forward concepts)  
- [ ] Definition/Purpose before first big table (no “Beginner-Friendly” heading)  
- [ ] After each topic / Step — one runnable program with a **requirement line** before the fence; two only when the case differs (no `Try these` heading or `Program N` titles)  
- [ ] Step-by-Step is **one assemble** (no Example 1–6 recap; no pasted `solution/`)  
- [ ] **Note** next to each major sub-topic (no standalone Common Mistakes)  
- [ ] Practice: 4–6 transfer items, **Model answer:** each; no Interview-style block  
- [ ] Practice appears **before** Mini-Project (Assignment)  
- [ ] Mini-Project is a full ticket (story, kit, what to build, sample run, Stretch, Done when) — not a one-line link and not the class assemble pasted again  
- [ ] No Revision Map table (redundant)  
- [ ] No Biweekly/Assessment MCQ block in the module (use `16_Assessments/`)  
- [ ] Interview Q&A: shared Q + A; share module PDF after concepts + mini-project  
- [ ] No Demo Plan / Tips / separate Discussion appendix / Real-World appendix  
- [ ] No fresher / switcher / beginner audience splits in learner text  
- [ ] No session numbers (S01–S100) in module notes — timing only in Session Calendar  
- [ ] Private only: `14_Trainer_Only/` · `solution/` · `*_KEY.md` (never share those)
