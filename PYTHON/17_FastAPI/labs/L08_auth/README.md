# Lab 08 — code folder

**Lesson:** [Lesson 8 — Authentication](../../Lesson_08_Authentication.md), section **Lab**

The steps and the checklist are in the lesson. This folder is the code.

```text
L08_auth/
├── broken/      ← Part A
├── starter/     ← Part B
└── solution/    ← after the checklist passes
```

Each folder is a whole project. From inside it:

```bash
cp .env.example .env
pip install -r requirements.txt
fastapi dev main.py
pytest test_employees.py
```

The app stops at startup if `.env` has no `SECRET_KEY`. The practice logins are in the lesson. Do not commit `.env`.
