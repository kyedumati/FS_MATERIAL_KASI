# Lab 09 — code folder

**Lesson:** [Lesson 9 — Frontend and CORS](../../09_Frontend_and_CORS.md), section **Lab**

The steps and the checklist are in the lesson. This folder is the code.

```text
L09_frontend/
├── broken/      ← Part A
├── starter/     ← Part B
└── solution/    ← after the checklist passes
```

Each folder has the API and `register.html`. From inside it, in two terminals:

```bash
cp .env.example .env
fastapi dev main.py
```

```bash
python3 -m http.server 5500
```

Open `http://127.0.0.1:5500/register.html`, not the file itself.
