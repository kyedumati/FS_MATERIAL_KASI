# Lab 06 — AcmeHR Apply for Leave

**Lesson:** [Lesson 6 — Forms](../../06_Forms.md) · **Time:** 35 minutes

**Ticket:** ACME-106 · **Customer:** Acme HR team
**Need:** Employees apply for leave online (requirements: *Leave Management → Apply leave*, *Employee Self-Service → Leave applications*). The form must send every field correctly to the server, upload an optional document, and be usable with the keyboard alone.

```text
acmehr/
├── apply-leave.html
└── css/
    └── form.css
```

## Part A — Fix the broken page (10 min)

Open [`broken/apply-leave.html`](broken/apply-leave.html). It has **6 bugs**:

1. Clicking the words "Leave type" does not put the focus in the select. (Compare `for` and `id`.)
2. Change the form to `method="get"`, serve the folder, and submit: the reason is missing from the URL.
3. You can select "Full day" **and** "First half" at the same time.
4. The supporting document would never reach the server — only its file name. (Which attribute is missing on `form`?)
5. Clicking "Save as draft" submits the leave request.
6. Press `Tab` through the form: you cannot see which field has the focus.

## Part B — Build it yourself (20 min)

Start from [`starter/`](starter/). Write the form in `apply-leave.html` from the `TODO` list, then complete the `TODO`s in `css/form.css`.

## Part C — Prove it works (5 min)

- [ ] Clicking every label focuses its field (or ticks its box).
- [ ] With `method="get"`, submitting shows every field in the URL, and `notify_team` only when ticked.
- [ ] Submitting with an empty leave type, date, or reason is blocked by the browser.
- [ ] You can complete the whole form using only `Tab`, the arrow keys, `Space` and `Enter`, and always see where the focus is.
- [ ] The `form` has `method="post"` and `enctype="multipart/form-data"`.
- [ ] The W3C validator shows **0 errors**.

## Stretch

Add a second version, `apply-leave-error.html`, showing the page the server would return when "To" is before "From": an error summary at the top, `aria-invalid` on the To field, and a message linked with `aria-describedby`.

Compare with [`solution/`](solution/) only after you finish.
