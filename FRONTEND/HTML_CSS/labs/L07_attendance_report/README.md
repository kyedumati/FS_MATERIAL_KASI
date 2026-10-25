# Lab 07 — AcmeHR Attendance Report

**Lesson:** [Lesson 7 — Tables](../../07_Tables.md) · **Time:** 35 minutes

**Ticket:** ACME-107 · **Customer:** Acme HR team
**Need:** Managers see each day's check-in and check-out times, hours, and late arrivals for their team (requirements: *Attendance Management → Daily reports*, *Reporting → Late arrivals*). The report must work with a screen reader and on a phone.

```text
acmehr/
├── attendance.html
└── css/
    └── report.css
```

## Part A — Fix the broken page (10 min)

Open [`broken/attendance.html`](broken/attendance.html). It has **6 bugs**:

1. The column headings are ordinary cells, not header cells.
2. The table has no title for screen readers.
3. In Arjun Reddy's row, the hours appear under "Check-out" and the status under "Hours". (Count the cells.)
4. The hours are left-aligned, so the decimal points do not line up.
5. One status pill is an empty coloured blob. What does it mean?
6. Make the window about 375px wide: the table pushes the whole report off the screen.

## Part B — Build it yourself (20 min)

Start from [`starter/`](starter/). Write the table from the `TODO` list in `attendance.html`, then complete the `TODO`s in `css/report.css`.

## Part C — Prove it works (5 min)

- [ ] The table has a `caption`, `thead`, `tbody` and `tfoot`.
- [ ] Every column header is a `th` with `scope="col"`; every employee name is a `th` with `scope="row"`.
- [ ] Every row covers 5 columns (count `colspan` too).
- [ ] Hours are right-aligned, and so is the "Hours" header.
- [ ] Every status shows a word, not only a colour.
- [ ] At about 375px wide, the report card stays inside the screen and only the table scrolls sideways. (The header links still overflow on a phone — you fix that in Lesson 8.)
- [ ] The W3C validator shows **0 errors**.

## Stretch

Below the daily table, add a monthly summary table for September 2026: one row per employee, columns Present, Late, On leave and Absent (right-aligned numbers), and team totals in `tfoot`. Make up the numbers, but make sure the totals add up.

Compare with [`solution/`](solution/) only after you finish.
