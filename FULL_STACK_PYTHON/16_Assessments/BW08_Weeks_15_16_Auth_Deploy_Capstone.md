# Biweekly Assessment BW08 — Weeks 15–16

**Sessions covered:** S71–80  
**Topics:** Forms, sessions, auth, CRUD lab, security, deployment, capstone kickoff

**Timebox:** 45–60 minutes (homework or Friday of the even week).  
**Rules:** Closed notes unless your trainer allows open notes. No copying.  
**Coding constraint:** Django auth and deploy concepts.

---

## A. Multiple Choice (12)

Circle the best option.

1. `login_required` helps:
   a) Force authentication on views
   b) Speed CSS
   c) Create venv
   d) Write SQL JOINs

2. Sessions typically store:
   a) Only HTML
   b) Only React props
   c) Git objects
   d) Server-side login state (via cookie id)

3. CSRF token in Django forms:
   a) Replaces migrations
   b) Opens MySQL port
   c) Security against cross-site posts
   d) Makes CSS pretty

4. Object-level permission means:
   a) Only admin CSS
   b) User only edits own rows
   c) Anyone edits all
   d) No login ever

5. `DEBUG = False` in production:
   a) Hides detailed errors from users
   b) Enables debug toolbar for public
   c) Disables HTTPS need
   d) Deletes DB

6. HTTPS is important because:
   a) Makes SQL faster always
   b) Replaces backups
   c) Removes auth need
   d) Encrypts traffic

7. `collectstatic` is for:
   a) Writing tests
   b) npm start
   c) Gathering static files for deploy
   d) Creating models

8. Capstone kickoff should define:
   a) Only lorem ipsum
   b) Scope, users, milestones
   c) Only fonts
   d) Only git emoji

9. Django messages framework is for:
   a) One-time user feedback flashes
   b) SQL joins
   c) React state
   d) CSS grid

10. Password hashing means:
   a) Save plain text
   b) Email passwords publicly
   c) Skip auth
   d) Store irreversible password digests

11. `ALLOWED_HOSTS` in production:
   a) Lists SQL tables
   b) Lists CSS files
   c) Limits which hosts Django serves
   d) Lists npm packages

12. CRUD stands for:
   a) Class Return Use Def
   b) Create Read Update Delete
   c) CSS React Unity Django
   d) Commit Rebase Undo Drop

---

## B. Coding (2)

1. Sketch a Django view that lists Task objects filtered by `owner=request.user` (auth assumed).

```python
# your code
```

2. List 5 deployment checklist items before going live (settings, secrets, static, DB, HTTPS, …).

```python
# your code
```

---

## C. Short answer (1)

Why filter querysets by the logged-in user for a tasks app?

_(Write 3–6 sentences.)_
