# Lab 04 — AcmeHR Employee Directory

**Lesson:** [Lesson 4 — Images, Navigation & Flexbox](../../04_Images_Navigation_and_Flexbox.md) · **Time:** 35 minutes

**Ticket:** ACME-104 · **Customer:** Acme HR team
**Need:** Employees can browse a contact directory of colleagues (requirement: *Employee Management → Employee Directory*). Each card shows a photo, name, designation and department. Cards wrap to fit the screen.

```text
acmehr/
├── directory.html
├── css/
│   └── directory.css
└── images/
    └── (six avatar images)
```

## Part A — Fix the broken page (10 min)

Open [`broken/directory.html`](broken/directory.html). It has **5 bugs**:

1. One avatar has no `alt` attribute at all.
2. Meera Iyer's photo does not load. (Compare the `src` path with the folder names.)
3. The navigation links are stacked, not in a row — although the CSS uses `display: flex`. (Which element is the flex container, and who are its direct children?)
4. All six cards are forced onto one line, and the page scrolls sideways.
5. One `img` has no `width` and `height`. The page looks fine — read the tags. Why does it still matter?

## Part B — Build it yourself (20 min)

Start from [`starter/`](starter/). Write the six cards in `directory.html`, then complete the `TODO`s in `css/directory.css`.

## Part C — Prove it works (5 min)

- [ ] Every `img` has `src`, `alt`, `width` and `height`.
- [ ] All six photos load (no broken image icons).
- [ ] Logo on the left, links on the right, on one line.
- [ ] Narrow the window to about 600px: the cards wrap to fewer per row, with no horizontal scrollbar.
- [ ] Each card is an `article`.
- [ ] The W3C validator shows **0 errors**.

## Stretch

Add a seventh employee using one of the existing images, with a different name. Then make the card for the current user (Ananya Rao) stand out with a 2px navy border, using a second class: `class="card card-me"`.

Compare with [`solution/`](solution/) only after you finish.
