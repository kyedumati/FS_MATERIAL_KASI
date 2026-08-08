# Tested Toolchain Guide

Pin these versions for the batch. Update this file when you re-test.

**Last verified profile:** Python Full Stack batch kit (macOS + Windows learners)

## Required versions

| Tool | Version target | Check command |
|------|----------------|---------------|
| Python | **3.11 or 3.12** (prefer 3.12) | `python3 --version` |
| pip | bundled with Python | `python3 -m pip --version` |
| Git | 2.40+ | `git --version` |
| MySQL Server | **8.0+** | `mysql --version` |
| Node.js | **20 LTS** (or 22 LTS) | `node --version` |
| npm | comes with Node | `npm --version` |
| Django | **5.x** (`django>=5.0,<6.0`) | `python -c "import django; print(django.get_version())"` |
| djangorestframework | current stable for Django 5 | in `requirements.txt` |
| Vite / React | Vite 5/6 + React 18+ | `npm create vite@latest` |
| VS Code | latest stable | Help → About |

## Python packages (typical project)

```text
django>=5.0,<6.0
djangorestframework
mysqlclient
# or PyMySQL if mysqlclient build fails on Windows
python-dotenv
whitenoise
gunicorn
requests
pytest
```

React app: create with Vite; add `axios` only if the batch prefers it over `fetch`.

## VS Code extensions

- Python (Microsoft)
- Pylance
- Django (optional)
- ESLint / Prettier (React weeks)
- MySQL (optional GUI) — Workbench is fine without it
- GitLens (optional)

## Install cheat sheet

### macOS (Homebrew)

```bash
brew install python@3.12 git mysql node@20
brew services start mysql
```

### Windows

1. python.org installer — tick **Add to PATH**  
2. Git for Windows  
3. MySQL Installer (Server + Workbench)  
4. Node LTS MSI  

If `mysqlclient` fails: `pip install PyMySQL` and add `import PyMySQL; PyMySQL.install_as_MySQLdb()` in Django `__init__.py` (document in project README).

## Known fixes

| Symptom | Fix |
|---------|-----|
| `python` not found on Mac | Use `python3` |
| Django MySQL encode errors | Install/upgrade `mysqlclient` or use PyMySQL bridge |
| `node` / `npm` missing | Reinstall Node LTS; restart terminal |
| Port 8000 in use | `python manage.py runserver 8001` |
| Vite CORS to Django | `django-cors-headers` + `CORS_ALLOWED_ORIGINS` |
| WhiteNoise 404 static | `collectstatic` + middleware order after SecurityMiddleware |

## Day-0 checklist

- [ ] Paste version outputs (`python3`, `git`, `mysql`, `node`) in the shared sheet  
- [ ] One sample Django+MySQL project migrates on your laptop  
- [ ] One Vite app starts with `npm run dev`  
- [ ] GitHub account + SSH/HTTPS push works  

Lab assets assume this toolchain: [`15_Lab_Assets/`](15_Lab_Assets/).
