# Lab 02 — AcmeHR Leave Policy Page

**Lesson:** [Lesson 2 — Content & Your First CSS](../../Lesson_02_Content_and_Your_First_CSS.md) · **Time:** 35 minutes

**Ticket:** ACME-102 · **Customer:** Acme HR team
**Need:** Employees must be able to read the leave policy in AcmeHR (requirement: *Employee Self-Service → Access policies*). The page must be reachable from the home page, have a correct heading outline, and use the AcmeHR stylesheet.

Keep this folder layout:

```text
acmehr/
├── index.html
├── css/
│   └── policy.css
└── policies/
    └── leave.html
```

## Part A — Fix the broken page (10 min)

Serve the [`broken/`](broken/) folder (`python3 -m http.server 8000`) and open `http://localhost:8000/policies/leave.html`. It has **6 bugs**:

1. The page has no styles at all. (Watch the terminal: which file gets a 404, and why?)
2. After you fix bug 1, the note under "Changing a request" is still not yellow. (Compare the HTML `class` with the CSS selector.)
3. The `h2` headings are neither navy nor in the Georgia font, although the `h2` rule sets both. (Read that rule character by character.)
4. One heading level is skipped. (Read only the headings.)
5. Space between two ideas is made with `<br>` tags.
6. One link says "click here".

## Part B — Build it yourself (20 min)

Start from [`starter/`](starter/):

1. `policies/leave.html` has the policy as plain text with `TODO` comments. Mark it up: one `h1`, `h2` sections with `id`s, a `ul` of leave types, an `ol` of steps, `strong` and `em`, a "Jump to" line with fragment links, and a `mailto:` link.
2. Link `../css/policy.css` from the page.
3. In `index.html`, link to `policies/leave.html`. In `leave.html`, link back to `../index.html`.
4. Complete the `TODO`s in `css/policy.css`.

## Part C — Prove it works (5 min)

- [ ] Both links (home → policy, policy → home) work when served.
- [ ] The terminal shows **200** for `leave.html` and for `policy.css`. (A 404 for `/favicon.ico` is harmless.)
- [ ] The heading outline has one `h1` and no skipped levels.
- [ ] Every "Jump to" link scrolls to its section.
- [ ] No `style="…"` attributes, no `<br>` for spacing, no `id` selectors in the CSS.
- [ ] The W3C validator shows **0 errors** for both pages.

## Stretch

Add a second page, `policies/attendance.html`, with the heading outline from *Try these* 1, using the **same** `policy.css`. Change one colour in the CSS and watch both pages update.

Compare with [`solution/`](solution/) only after you finish.
