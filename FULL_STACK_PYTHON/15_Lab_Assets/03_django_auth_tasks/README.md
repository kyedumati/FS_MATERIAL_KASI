**Sessions:** ~71–77

# Ticket: Private tasks per user

**Bug report:** Any logged-in user can see everyone’s tasks.  
**Accept:** Each user sees only their own tasks; anonymous users redirected to login.

## Starter

Open `starter/views_snippet.py` — implement `task_list` / `task_create` (or paste into your Django app from Lab `06` / module `04`).

## Broken

`broken/views_snippet.py` — typical owner bug. Fix it.

## Done when

- [ ] `@login_required` on list/create  
- [ ] List filtered by `owner=request.user`  
- [ ] Create sets `owner` before save  
