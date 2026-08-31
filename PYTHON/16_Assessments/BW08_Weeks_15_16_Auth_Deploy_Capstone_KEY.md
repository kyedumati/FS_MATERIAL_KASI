# KEY — Biweekly Assessment BW08 — Weeks 15–16 (Trainer only)

**Do not share with students.** Excluded from student pack (`*_KEY.md`).

## A. MCQ answers

1. **a** — Force authentication on views
2. **d** — Server-side login state (via cookie id)
3. **c** — Security against cross-site posts
4. **b** — User only edits own rows
5. **a** — Hides detailed errors from users
6. **d** — Encrypts traffic
7. **c** — Gathering static files for deploy
8. **b** — Scope, users, milestones
9. **a** — One-time user feedback flashes
10. **d** — Store irreversible password digests
11. **c** — Limits which hosts Django serves
12. **b** — Create Read Update Delete

## B. Coding — model points

1. Sketch a Django view that lists Task objects filtered by `owner=request.user` (auth assumed).
   - Award marks for correctness + teaching-order constraints respected.

2. List 5 deployment checklist items before going live (settings, secrets, static, DB, HTTPS, …).
   - Award marks for correctness + teaching-order constraints respected.

## C. Short answer — model

Privacy/security — prevent IDOR; users must not see/edit others' data.

## Suggested scoring

| Section | Marks |
|---------|------:|
| A MCQ (1 each) | 12 |
| B Coding (6 each) | 12 |
| C Short | 6 |
| **Total** | **30** |
