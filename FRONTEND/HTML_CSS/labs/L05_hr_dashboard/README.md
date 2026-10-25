# Lab 05 — AcmeHR HR Dashboard

**Lesson:** [Lesson 5 — Grid & Positioning](../../05_Grid_and_Positioning.md) · **Time:** 35 minutes

**Ticket:** ACME-105 · **Customer:** Acme HR team
**Need:** HR managers see today's workforce figures and the leave requests waiting for them on one dashboard (requirements: *Reporting & Analytics → HR dashboards*, *Leave Management → Leave approval*).

```text
acmehr/
├── dashboard.html
└── css/
    └── dashboard.css
```

## Part A — Fix the broken page (10 min)

Open [`broken/dashboard.html`](broken/dashboard.html). The HTML is correct; all **5 bugs** are in the CSS:

1. Scroll down: the header scrolls away instead of sticking.
2. The four tiles are stacked in one column. (Read the property name letter by letter.)
3. The "Leave requests" panel is not next to the "Headcount by department" panel. (Compare the area names.)
4. The red "3 new" badge is at the top-right corner of the **page**, not the tile.
5. The department numbers sit under the names instead of on the right.

## Part B — Build it yourself (20 min)

Start from [`starter/`](starter/). The HTML is complete. Complete the 6 `TODO`s in `css/dashboard.css`.

## Part C — Prove it works (5 min)

- [ ] Four tiles in one row at full width; fewer per row when you narrow the window.
- [ ] The two panels sit side by side, requests wider (2 : 1).
- [ ] The badge hangs off the corner of its own tile.
- [ ] The header stays visible when you scroll.
- [ ] Department numbers line up on the right.
- [ ] No `position: absolute` used for anything except the badge.

## Stretch

Add a "New joiners this month: 3" tile, and a full-width "Announcements" panel at the bottom using a new grid area.

Compare with [`solution/`](solution/) only after you finish.
