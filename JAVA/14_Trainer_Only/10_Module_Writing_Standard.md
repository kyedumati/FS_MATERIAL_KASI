# Module Writing Standard — Definition / Purpose Before Syntax

**Purpose:** Keep `JAVA/` teachable for live class — Definition/Purpose, labs, and modern safe Java (without legacy note patterns).

**Reference:** Python FS [10_Module_Writing_Standard.md](../../PYTHON/14_Trainer_Only/10_Module_Writing_Standard.md) — same house style, Java code. Strong module target: Python `03_OOP_Part1_Classes_Encapsulation.md`.

---

## Required module section order

| # | Section | Notes |
|---|---------|--------|
| 1 | Title + Phase + Previous/Next | No Audience / Program / Duration — timing lives in Session Calendar only |
| 2 | **Module Outcome** | `**Module Outcome:**` + 3–5 lively can-do bullets (job scene, named product when business-shaped). Immediately after the header `---`. Not a Bloom “Learning Outcomes” list |
| 3 | Start with **Definition / Purpose** (or Motivation) | Definition + Purpose — no Classroom Ticket section |
| 4 | Important Concepts (+ **Try these** after each topic) | Definition/Purpose → syntax → **Note** → ≥2 programs per topic |
| 5 | Step-by-Step annotated code | Longer demos (Core often merges topics here) |
| 6 | Practice Exercises | Heading must be exactly `## Practice Exercises` (not `## Practice`). Basic → Intermediate → Interview; each item has **Model answer:** (shared — one material). **Before** Mini-Project |
| 7 | **Mini-Project (Assignment)** | Same section — take-home / homework. Heading: `## Mini-Project (Assignment): Title`. Lab kit + What to build + Stretch + **Done when** |
| 8 | Assignment (standalone) | Use `## Assignment` **only if** the module has no Mini-Project (e.g. some Spring lab days) |
| 9 | **Interview Q&A** | Shared with students (Q + A). Share with the module PDF after concepts + mini-project |

**Do not add** a standalone `## Common Mistakes` section. Put traps next to the sub-topic as **Note:** bullets (see below).

**Do not add** a **Revision Map** table — redundant with Key takeaways callouts, Practice, and Interview Q&A.

**Do not add** a **Classroom Ticket** section — lab kits are linked from the Session Calendar, Mini-Project, and `15_Lab_Assets/`.

**Graded tests** live only in [`16_Assessments/`](../16_Assessments/) (one paper every 2 weeks). Do **not** put `## Assessment` or `## Biweekly Assessment` inside modules — trainers assign papers from the calendar + assessments README.

**Do not add:** Discussion Questions (separate), Trainer Tips, Trainer Demo Plan, or large Real-World Use Cases **tables**. Prefer a short `**Where used?**` callout instead (see PDF markers above).

**Do not add** a Bloom-style **Learning Outcomes** list or a **Teaching note** paragraph. Use **Module Outcome** (can-do bullets) at the start instead.

**Delivery timing / session numbers (S01–S100)** live only in the [Session Calendar](../Session_Calendar_100.md) — **not** in module headers or learner-facing notes.

---

## Required teaching order (every concept block)

| Step | Section cue | Learner should leave knowing |
|------|-------------|------------------------------|
| 1 | **Definition:** | Plain-English definition + one job example |
| 2 | **Purpose:** | Pain without it vs win with it (why this idea exists) |
| 3 | **Kinds / cases** (if any) | primitive vs wrapper, checked vs unchecked, … |
| 4 | **How (syntax + small demo)** | Minimal modern Java (JDK 17) |
| 5 | **Note** (inline) | 1–3 bullets right after syntax or before Try these — interview traps for **this** topic only |
| 6 | **Table only after prose** | Tables summarise |

**Forbidden cold open:** parameter table / annotation matrix / bare `public class` with no Definition/Purpose.

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

```java
public class DemoOne {
    public static void main(String[] args) {
        System.out.println("Priya");
    }
}
```

**Program 2 — Short title**

```java
public class DemoTwo {
    public static void main(String[] args) {
        System.out.println("Ravi");
    }
}
```
```

- Short (typically 5–20 lines), copy-paste runnable **JDK 17**.
- Prefer `public class` + `main` unless the topic is Spring.
- India-relevant examples OK (INR, student marks, ATM, names like Priya/Ravi, UPI, campus).
- **Named products (soft-apply):** when the example is business-shaped, prefer **AcmeHR**, **TechMart**, **MedCare**, or **SecureBank** in `**Where used?**`, program titles, Interview Q&A, and mini-project tickets. Do not force syntax-only drills. See [12_Named_Product_Domains.md](12_Named_Product_Domains.md). Canonical schemas: [`MYSQL/12_Real_Time_Projects.md`](../../MYSQL/12_Real_Time_Projects.md). CampusCart stays the capstone (college TechMart-style storefront).
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
| `**Remember:**` | One-liner to keep (`this` = current object) |
| `**Interview:**` | Short interview cue |
| `**Common Error:**` | Classic trap (`==` on String, string-concat SQL, etc.) |
| `**Module Outcome:**` | 3–5 can-do bullets at the **module start** (after header). Lively — what you can *do* when class ends, not Bloom verbs |
| `**Where used?**` | 3–5 real domains that **name** AcmeHR / TechMart / MedCare / SecureBank when business-shaped — **not** a big Use Cases table |
| `**Icons:** Bank · UPI · Employee · Laptop · Order` | Optional chip strip (also Hospital · Payroll · CRM) |
| `**Key takeaways:**` | 2–4 bullets **immediately after** a Mermaid diagram (paired beside it in PDF). Major ideas only — not every sub-topic |

**Practice answers:** after `**Model answer:**` / `**Expected Output:**`, put a blank line then a fenced block at **column 0**. Do **not** indent `` ``` `` under the list item — Cursor/VS Code preview often renders indented fences as empty.

**Program titles** must be one bold line: `**Program 1 — Book with info()**` (do not split around inline code).

Core Java / OOP: avoid Spring/framework forward-selling; introduce Spring in `09_Spring_Boot/`. JDBC before JPA. Label any preview **Later — …**.

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

**Do not require Lombok** in learner Done when (optional Stretch). Prefer explicit getters or records where it helps juniors.

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
- Modern safe Java: try-with-resources, `PreparedStatement`, no raw passwords in git, no string-concat SQL.  
- Spring examples: Spring Boot 3 / `jakarta.*`; `application.yml`; `.env.example`; never commit secrets.  
- Absorb PDF pedagogy — not unsafe snippets.  
- Schedule follows the Session Calendar.

### Teaching-order rule (lab kits)

A kit attached to calendar session **S** may only require syntax/APIs taught in sessions **1…S**. This applies to **every** topic.

- **Core path** (`starter/`, `broken/` student work, `solution/`, Done when): prior concepts only.  
- **Stretch:** may preview later topics — label clearly (e.g. “Later — Collections week”).  
- **Before Flow Control:** no `if` / `while` / `for` / extra methods in core path — linear `main`.  
- **Before OOP:** no classes beyond the current topic (`public class` + `main` as the file container is OK from day 1).  
- **Before Exceptions:** no `throw` / `try` / `catch` in core path (validate with `print` + `return`).  
- **Before JDBC:** no Spring.  
- **Before JPA:** JDBC must already be taught.  
- **Do not require** Lombok, records-everywhere, or `var` in learner Done when (optional Stretch).  
- **From Exceptions week onward:** `try` / `catch` / `throw` / try-with-resources OK.

---

## Checklist — classroom-ready

- [ ] Section order matches the table above  
- [ ] No Classroom Ticket section (labs via calendar / Mini-Project / `15_Lab_Assets/`)  
- [ ] **Module Outcome:** (3–5 can-do bullets) immediately after the header  
- [ ] No Bloom Learning Outcomes list and no Teaching note paragraph  
- [ ] Ticket / lab starter+solution stay within calendar teaching order (no forward concepts)  
- [ ] Definition/Purpose before first big table  
- [ ] **Try these (2 programs)** after each topic / Step — complete runnable Java  
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
- [ ] No Spring forward-selling in Core Java / OOP weeks  
- [ ] Private only: `14_Trainer_Only/` · `solution/` · `*_KEY.md` (never share those)
