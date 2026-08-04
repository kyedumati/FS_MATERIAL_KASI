# Standard Project Deliverables Bundle

Every mini-project and the capstone use the **same submission checklist**. This turns class exercises into portfolio evidence hiring managers can trust.

---

## Required for grading

| # | Artefact | Notes |
|---|----------|-------|
| 1 | **Public GitHub repo** | No secrets; meaningful commit history |
| 2 | **README.md** | Problem, features, stack, setup, how to run, screenshots, demo link |
| 3 | **`requirements.txt`** and/or **`package.json`** | Pinned enough to install; list Python/Node version in README |
| 4 | **`.env.example`** | All keys documented; **never** commit `.env` |
| 5 | **Sample / seed data** | SQL dump, fixtures, or `seed` command / JSON |
| 6 | **Screenshots** | Happy path; for UI also **mobile width** (~375px) |
| 7 | **Demo video (2–5 min)** | Loom/Drive link in README — show run + one feature |
| 8 | **`.gitignore`** | Includes `venv/`, `.env`, `__pycache__/`, `node_modules/`, `staticfiles/` |

**Capstone extras:** deploy URL (or Lab 07 proof), ER diagram image, Postman collection if API exists.

---

## README template (copy)

```markdown
# Project title

## Problem
One paragraph.

## Features
- ...

## Stack
Python 3 · Django · MySQL · ...

## Setup
1. clone
2. python -m venv venv && source venv/bin/activate
3. pip install -r requirements.txt
4. cp .env.example .env  # fill values
5. python manage.py migrate
6. python manage.py runserver

## Demo
- Live: https://...
- Video: https://...

## Screenshots
(desktop / mobile)

## Sample credentials
- demo@example.com / (see mentor — not a real production password)
```

---

## Skill-level use

| Level | Deliverables expectation |
|-------|--------------------------|
| Guided | Repo exists; README partial; needs help to run |
| Independent | Peer can clone and run from README alone |
| Interview-ready | Learner narrates architecture in demo video clearly |

---

## Security note (submissions)

Never commit a real `.env` or live passwords. If that happens by mistake: remove the file from Git tracking, add it to `.gitignore`, commit the fix, and **rotate** the password (treat it as leaked).
