# Ticket: Clean GitHub Repo Hygiene

**Customer:** Hiring manager  
**Need:** Fix `.gitignore` so secrets and generated folders are never committed; write a README a teammate can run.

**Teaching-order:** `git add` / `commit`, `.gitignore` for **both** Python and Java generated output, project README. No new language syntax. No Django. No Spring. `venv/` and `target/` are folder names you ignore.

## Starter

Complete `starter/.gitignore` and `starter/README.md`. Ignore `.env`, `venv/`, `.venv/`, `__pycache__/`, `*.pyc`, `target/`, `*.class`, `.idea/`, `.vscode/`, `.DS_Store`. Do **not** ignore `*.py` or `*.java`. README must name the project, say what it does, and show run steps for **this** batch (venv + Python **or** `javac` / `java`).

## Broken

`broken/.gitignore` is wrong — fix it. Do **not** commit `.env`. `broken/.env.example` is a dummy template (OK to commit). A real `.env` is not.

## Done when

- [ ] `.gitignore` ignores `.env`, `venv/`, `target/`, `__pycache__/`, `*.class`, `.idea/`, `.vscode/`, `.DS_Store`
- [ ] Source `*.py` / `*.java` are **not** ignored
- [ ] README names the project, what it does, and how to run
- [ ] `git status` does not list `.env`, `venv/`, or `target/` (create dummy files locally to prove it)
