# Accessibility & Responsiveness Checklist (Frontend + Django templates)

Use this on **every** UI mini-project (Week 10 portfolio, Django templates, React screens).  
Simple checks — high visibility on portfolio and in code reviews.

---

## Accessibility (a11y)

| Done | Check |
|:----:|-------|
| ☐ | One clear **`h1`** per page; heading levels do not skip (`h1` → `h2` → `h3`) |
| ☐ | Every input has a visible **`<label for="...">`** (or `aria-label`) |
| ☐ | Images that convey meaning have meaningful **`alt`**; decorative images use `alt=""` |
| ☐ | Buttons/links have clear text (not only “click here”) |
| ☐ | Color is not the only way to show errors (text message too) |
| ☐ | Focus order: can Tab through form controls; focus ring visible |
| ☐ | Keyboard: can submit form and open main nav without a mouse |
| ☐ | Contrast: text readable on background (avoid grey-on-grey) |
| ☐ | `lang` attribute on `<html>` (e.g. `lang="en"`) |

**Quick tool:** Chrome Lighthouse → Accessibility (aim to understand failures, not chase 100 blindly).

---

## Responsiveness

| Done | Check |
|:----:|-------|
| ☐ | Layout usable at **~375px** width (phone) without horizontal scroll |
| ☐ | Touch targets large enough (buttons not tiny) |
| ☐ | Nav does not overflow; wraps or collapses cleanly |
| ☐ | Images/cards scale (`max-width: 100%` where needed) |
| ☐ | Screenshot evidence: desktop **and** mobile in README |

---

## Where this is required

- Frontend modules `01`–`03` assignments  
- Django template UIs  
- Capstone CampusCart pages  
- React storefront (if built)

---

## Trainer Tips

- Deduct from UI project grade for missing labels/alt — same as a PR review.  
- Frame a11y as **respect for users**, not “extra theory.”
