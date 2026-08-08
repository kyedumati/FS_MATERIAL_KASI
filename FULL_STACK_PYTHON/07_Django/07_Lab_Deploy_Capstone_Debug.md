# Lab Day: Deploy + Capstone Debug

**Phase:** Backend — Django  
**Prerequisites:** Django `05_Security_and_Deployment.md`; a CRUD+auth app from Lab `06` or CampusCart MVP slice  
**Goal:** Production-like config verified + at least one **live or staging URL** (or documented blocked-by-platform note with local `check --deploy` green)

**Previous module:** Lab CRUD Auth Consolidation
**Next module:** Flask Overview

---

## Learning Outcomes

- Apply `load_dotenv()`, `DEBUG=False` simulation, and WhiteNoise/`STORAGES` from Module 05
- Run and interpret `python manage.py check --deploy`
- Debug static files, ALLOWED_HOSTS, and database connection failures calmly
- Update README with deploy steps and env var list

---

## Classroom Ticket

Open the lab kit **before** long notes. Read the ticket → code in `starter/` or fix `broken/`.

- **[Deploy hygiene checklist (.env, README)](../15_Lab_Assets/19_git_portfolio_hygiene/)**

Finish the ticket in class; compare with the official solution only when your trainer says so.

## Must-pass checklist

### Done when

All boxes below must be checked before you submit the deploy tag.

- [ ] `.env` gitignored; `.env.example` committed
- [ ] `load_dotenv(BASE_DIR / ".env")` present in settings
- [ ] `STORAGES["staticfiles"]` configured (Django 5.x pattern)
- [ ] `python manage.py check --deploy` run with `DJANGO_DEBUG=False`
- [ ] `collectstatic` succeeds
- [ ] Gunicorn smoke test **or** platform deploy started
- [ ] README: env vars table + demo accounts (non-production passwords)
- [ ] Screenshots of live/staging **or** local production-mode proof

---

## Session plan (trainer) — 1h 15m × 2–3 days + homework

| Session | Focus (75 min) |
|---------|----------------|
| Lab day 1 | Recap secrets/DEBUG/hosts (15) → wire `load_dotenv` + `STORAGES` (55) → homework: run `check --deploy` |
| Lab day 2 | Fix `check --deploy` warnings (30) → collectstatic/Gunicorn or PaaS start (40) → blockers board (5) |
| Lab day 3 (optional) | Deploy attempt / capstone bug bash → README env table → skill-level rating |

**Grade the process** (env hygiene + `check --deploy`), not only a public URL.

---

## Debug playbook

| Problem | First checks |
|---------|----------------|
| DisallowedHost | ALLOWED_HOSTS includes platform hostname |
| CSS missing on deploy | WhiteNoise middleware order; collectstatic in build |
| DB connection refused | Host/user/password; PaaS IP allowlist |
| 500 with DEBUG=False | Check logs; temporary logging; never turn DEBUG=True on public URL long-term |
| Secret key warning | Generate new key; set env; rotate if leaked |

---

## Skill-level rubric (today)

| Level | Evidence |
|-------|----------|
| Not started | No check --deploy attempt |
| Guided | Passes checks only with trainer |
| Independent | check --deploy clean + collectstatic + README env table |
| Interview-ready | Explains why DEBUG=False and env secrets matter in interviews |

---

## Assignment

Submit deploy checklist filled + repo tag `lab07-deploy`. Capstone M4 advanced if URL live.

---

## Revision Map — Memorize / Understand / Practise / Build

| Topic | Memorize | Understand | Practise | Build |
|-------|----------|------------|----------|-------|
| check --deploy | Command | Why warnings matter | Run & fix | Checklist doc |
| Env config | Keys in `.env.example` | Shell vs file vs PaaS | Break DEBUG | Staging settings |
| Static | collectstatic | WhiteNoise role | Broken CSS fix | Admin CSS live |

---

