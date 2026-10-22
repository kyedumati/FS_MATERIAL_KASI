# Lab 01 — code folder

**Lesson:** [Lesson 1 — Introduction to FastAPI](../../Lesson_01_Introduction_to_FastAPI.md), section **Lab**

The steps and the checklist are in the lesson. This folder is the code.

```text
L01_health/
├── broken/main.py      ← Part A
├── starter/main.py     ← Part B
└── solution/main.py    ← after the checklist passes
```

Copy `starter/` into your `acmehr-api` folder, or work inside `starter/` with its own venv.

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
fastapi dev main.py
```

Open `solution/main.py` only after every box in the lesson checklist is ticked.