# Lab Day: Django CRUD + Auth Consolidation

**Phase:** Backend — Django  
**Prerequisites:** Django modules `01`–`05` started (at least through auth forms)  
**Goal:** Every learner finishes an **independent**, login-protected CRUD feature they can demo

**Previous module:** Security and Deployment
**Next module:** Lab Deploy Capstone Debug

---

## Learning Outcomes

- Complete end-to-end Django flow independently
- Fix common auth and form bugs independently
- Push a working CRUD+auth app with the [standard deliverables bundle](../Standard_Project_Deliverables.md)

---

## Lab brief (pick one track)

**Track A — Task Manager:** Task model (`title`, `is_done`, `owner` FK to User). List/create/toggle/delete only for logged-in owner.  
**Track B — Mini Blog:** Post model (`title`, `body`, `author`). List/detail/create/edit; edit only if author.  
**Track C — CampusCart seed:** Product list + “save favorite” for logged-in user (simpler than full cart).

**Where used?** Campus portal tasks/blog, CampusCart favorites, and any login-protected CRUD you will demo in placement.

**Remember:** Filter querysets by `owner=request.user` (or author) — otherwise every user sees everyone’s data.

---

## Must-pass checklist (exit criteria)

### Done when

All boxes below must be checked before demo day.

- [ ] `runserver` works; migrations applied
- [ ] Register → login → logout works
- [ ] Anonymous user redirected from create/edit
- [ ] CRUD works for own records; no crash on empty list
- [ ] CSRF on all POST forms
- [ ] Flash messages on success
- [ ] Admin can view models
- [ ] GitHub push with standard deliverables (README, requirements, `.env.example`, screenshots)

---

## Common stuck points

| Symptom | Hint |
|---------|------|
| 404 on `/tasks/` | App urls included in project urls? trailing slash? |
| Form saves but blank owner | Set `form.instance.owner = request.user` before save |
| Everyone sees all tasks | Filter queryset by `owner=request.user` |
| CSRF 403 | `{% csrf_token %}` inside `<form method="post">` |
| Redirect loop | LOGIN_URL / login_required mismatch |

---

## Skill-level rubric (today)

| Level | Evidence |
|-------|----------|
| Not started | No runnable app |
| Guided | Works only with help |
| Independent | Completes must-pass checklist alone |
| Interview-ready | Explains owner filtering, CSRF, and session in plain English |

---

## Assignment

Finish any incomplete checklist items + push repo. Demo video 2–3 min.

**Expected:** README shows login screenshot + task list screenshot; clone instructions work for a peer.
