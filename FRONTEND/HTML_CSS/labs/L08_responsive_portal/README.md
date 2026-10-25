# Lab 08 — Make AcmeHR Responsive

**Lesson:** [Lesson 8 — Responsive Design](../../08_Responsive_Design.md) · **Time:** 35 minutes

**Ticket:** ACME-108 · **Customer:** Acme HR team
**Need:** Managers check the dashboard on their phones. Today it only works on a desktop. Make it work from 320px phones to wide monitors (BRD success metric: more than 90% of employees use self-service).

```text
acmehr/
├── dashboard.html
├── css/
│   └── dashboard.css
└── images/
    ├── office-wide.png
    └── office-tall.png
```

## Part A — Fix the broken page (15 min)

Open [`broken/dashboard.html`](broken/dashboard.html) and make the window about 375px wide (or open it on your phone). It has **6 problems**:

1. On a phone, everything is tiny. (Which tag is missing in the `head`?)
2. The header links run off the screen.
3. The dashboard is always 960px wide.
4. The four tiles are always four columns of 200px.
5. The "requests" and "office" panels are always side by side.
6. The office picture is wider than the phone. Also give phones the taller crop, `office-tall.png`.

## Part B — Build it yourself (15 min)

Start from [`starter/`](starter/). Complete the `TODO`s in `dashboard.html` and `css/dashboard.css`, mobile first.

## Part C — Prove it works (5 min)

Narrow the window slowly from wide to 320px:

- [ ] No sideways scrolling at any width.
- [ ] Phones: header links wrap under the logo; panels are stacked; tiles are two per row or one per row.
- [ ] From 640px: logo and links on one line; the two panels side by side.
- [ ] The heading grows smoothly with the window, but stays between 1.5rem and 2.5rem.
- [ ] Phones show the tall office picture; wide screens show the wide one.
- [ ] All media queries use `min-width`.

## Stretch

Make your Lesson 4 directory, Lesson 6 leave form and Lesson 7 attendance report pass the same checks.

Compare with [`solution/`](solution/) only after you finish.
