# Lab 09 — Final Project: The AcmeHR Portal

**Lesson:** [Lesson 9 — Polish, Accessibility & Final Project](../../09_Polish_Accessibility_and_Final_Project.md) · **Time:** session lab (35 min) + about 6 hours of homework · **Work:** individual

**Ticket:** ACME-109 · **Customer:** Acme HR team
**Need:** A first, static version of the AcmeHR employee portal for the Phase 1 demo. It will become the templates of the Django / Spring Boot application in the next phase, so the HTML must be clean, semantic and consistent.

## 1. What to build

Seven pages that share one header, one footer and **one stylesheet**:

```text
acmehr/
├── index.html            Home: welcome, leave balance, quick links, office picture
├── profile.html          Employee profile (Lesson 3)
├── directory.html        Employee directory, six or more people (Lesson 4)
├── dashboard.html        HR dashboard: tiles and two panels (Lesson 5)
├── apply-leave.html      Apply for leave form (Lesson 6)
├── attendance.html       Daily attendance report table (Lesson 7)
├── policies/
│   └── leave.html        Leave policy with an FAQ in details/summary (Lessons 2, 9)
├── css/
│   └── acmehr.css        The only stylesheet
└── images/
```

Start from [`starter/`](starter/): it has the images, the design tokens at the top of `css/acmehr.css`, and `_page-template.html` with the shared `head`, skip link, header and footer. Reuse and improve your own work from Labs 01–08.

## 2. Requirements

**HTML**

- Every page: correct skeleton, unique `title` in the form *Page — AcmeHR*, a `meta description`, `noindex`, the favicon.
- Every page: skip link, `header` with `nav aria-label="Main"`, one `main id="main"`, `footer`. The current page's link has `aria-current="page"`.
- One `h1` per page; no skipped heading levels.
- Images: `alt` (empty when decorative), `width` and `height`.
- The form: every field labelled, every field with a `name`, `method="post"`, `enctype="multipart/form-data"`, the six leave types from the BRD.
- The table: `caption`, `thead`, `tbody`, `tfoot`, `th` with `scope`.

**CSS**

- One file, `css/acmehr.css`, in the eight sections of the starter. No `style` attributes, no `<style>` blocks, no `!important`, no id selectors.
- Every colour comes from a token in `:root`.
- Mobile first: base styles for phones, `@media (min-width: …)` for wider screens.
- Every link, button and field has a visible `:focus-visible` style. Hover effects respect `prefers-reduced-motion`.

## 3. Acceptance criteria — the demo checklist

The project is accepted when **every** box can be ticked in front of the trainer:

- [ ] All 7 pages pass the [W3C validator](https://validator.w3.org/nu/) with **0 errors**.
- [ ] Every page link in the header works, including from `policies/leave.html`.
- [ ] At **320px, 375px, 768px and 1280px** wide: no page scrolls sideways (a table inside its own scroll box is allowed).
- [ ] The whole leave form can be completed with the keyboard only, and the focus is always visible.
- [ ] The first `Tab` on any page shows the skip link, and `Enter` moves to the main content.
- [ ] All text has a contrast of at least 4.5 : 1; field borders and the focus ring at least 3 : 1.
- [ ] With `method="get"` temporarily, submitting the form puts every field's `name` in the URL.
- [ ] Changing `--color-brand` in `:root` changes the brand colour on every page.
- [ ] Served with `python3 -m http.server 8000`, the terminal shows no 404 except `/favicon.ico` (or none at all, since the pages link their own icon).

## 4. Rubric (100 points)

| Area | Points | Full marks when |
|---|---:|---|
| Semantic HTML | 20 | Right element for every job: regions, headings, lists, `dl`, `article`, `figure`, `table`, `form`. No div soup. |
| Forms | 15 | Labels, names, types, validation attributes, `fieldset`, correct `method` and `enctype`. |
| Tables | 10 | Caption, sections, `scope`, numbers right-aligned with `tabular-nums`, scroll wrapper. |
| Layout | 15 | Flexbox and Grid used where each fits; no `position: absolute` for layout. |
| Responsive | 15 | Mobile first; works from 320px to 1280px; fluid type; responsive images. |
| Accessibility | 15 | `alt`, contrast, keyboard, visible focus, skip link, `aria-current`, status shown with words. |
| Code quality | 10 | One organised stylesheet, tokens, meaningful class names, consistent indentation, validator clean. |

**Grades:** 85–100 Excellent · 70–84 Good · 50–69 Needs work (fix and resubmit) · below 50 Resubmit.

## 5. Stretch goals (bonus, up to +10)

- A dark theme by changing only the tokens (`body.theme-dark { … }`).
- A monthly attendance summary table on `attendance.html` with correct totals.
- An "error state" copy of the leave form, as the server would return it: error summary, `aria-invalid`, messages linked with `aria-describedby`.
- A `404.html` page in the same design.

## 6. How to submit

1. Put the `acmehr/` folder in a Git repository and push it to GitHub (Git Sessions 1–2).
2. Add a `README.md` with: your name, the list of pages, and anything you did beyond the requirements.
3. Share the repository link with your trainer before the next session.

The reference solution is in [`solution/`](solution/). Open it only after you submit.
