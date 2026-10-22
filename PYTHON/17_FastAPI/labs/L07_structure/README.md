# Lab 07 — code folder

**Lesson:** [Lesson 7 — Project structure](../../Lesson_07_Project_Structure.md), section **Lab**

The steps and the checklist are in the lesson. This folder is the code.

```text
L07_structure/
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

The tests use a SQLite file, so they do not need MySQL. `fastapi dev` uses MySQL.
