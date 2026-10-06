# Lab 03 — AcmeHR Employee Profile

**Lesson:** [Lesson 3 — Page Structure & the Box Model](../../Lesson_03_Page_Structure_and_the_Box_Model.md) · **Time:** 35 minutes

**Ticket:** ACME-103 · **Customer:** Acme HR team
**Need:** Employees can view their own profile (requirement: *Employee Management → Employee Profile*, *Employee Self-Service → View profile*). The page shows employment details and contact information, uses the AcmeHR header and navigation, and works in a narrow browser window.

```text
acmehr/
├── profile.html
└── css/
    └── profile.css
```

## Part A — Fix the broken page (10 min)

Open [`broken/profile.html`](broken/profile.html). It has **6 bugs**:

1. The page regions are all `div`s. Replace them with the right elements.
2. The employment details are lines of text with `<br>`. Use a description list.
3. The navigation is a vertical bulleted list, not a horizontal bar.
4. Make the browser window narrow (about 500px). The white card does not shrink and a horizontal scrollbar appears.
5. The white card has no space inside it, although the CSS sets `padding`. (Count the values.)
6. The footer is wider than the page, even in a wide window. (Which rule is missing at the top of the CSS?)

## Part B — Build it yourself (20 min)

Start from [`starter/`](starter/). Mark up `profile.html` (regions, `dl`s, a `span` for the status) and complete the `TODO`s in `css/profile.css`.

## Part C — Prove it works (5 min)

- [ ] The page has one `header`, one `nav`, one `main`, and one `footer`.
- [ ] Every `section` starts with an `h2`.
- [ ] All profile fields are in `dl` / `dt` / `dd`.
- [ ] Narrow the window to about 400px: no horizontal scrollbar, and the card shrinks.
- [ ] Font sizes use `rem`.
- [ ] The W3C validator shows **0 errors**.

## Stretch

Add an `aside` after `main` titled "Leave balance" with a `dl` of Casual 8, Sick 10, Earned 15 days. Style it as a second centred card.

Compare with [`solution/`](solution/) only after you finish.
