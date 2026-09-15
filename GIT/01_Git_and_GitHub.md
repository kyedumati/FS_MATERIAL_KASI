# Git and GitHub

**Shared topic** (Python FS + Java FS) · **5 sessions · about 6 hours**

**Previous (Python FS):** [Logging](../PYTHON/03_Advanced_Python/06_Logging_Module.md)  
**Previous (Java FS):** [File Handling](../JAVA/04_Collections_Exceptions_IO/03_File_Handling.md)  
**Next (Python FS):** [MySQL for Full Stack Developers](../PYTHON/05_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md)  
**Next (Java FS):** [MySQL for Full Stack Developers](../JAVA/06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md)

---

## Course Outcome

By the end of **five sessions**, a beginner can use Git and GitHub on a real software team.

That means:

- Put a project on GitHub
- Use the daily commands without guessing
- Work on a feature branch and open a Pull Request
- Sync with teammates, undo common mistakes, and resolve a simple conflict
- Repeat the same moves in the IDE

It does **not** mean every Git feature.

Start at **Session 1**. Do not skip ahead.

---

## Who this is for

You have never used Git. You may have heard of GitHub. You can write basic programs and use a terminal a little. Words like repository, commit, branch, and pull request are taught when the problem appears.

Running example: **KSR_MART**. Other people on the project are **teammates**.

---

## Teaching order

| Session | File | In this sitting (~70–75 min) |
|--------:|------|------------------------------|
| 1 | [01_Git_Session1.md](01_Git_Session1.md) | Why Git, Git vs GitHub, install, empty GitHub repo, first push |
| 2 | [02_Git_Session2.md](02_Git_Session2.md) | Daily loop: status / add / commit / log / diff, then clone an existing repo |
| 3 | [03_Git_Session3.md](03_Git_Session3.md) | Feature branches and Pull Requests (solo and team) |
| 4 | [04_Git_Session4.md](04_Git_Session4.md) | Pull and sync, safe undo, one merge conflict, a few team scenarios |
| 5 | [05_Git_Session5.md](05_Git_Session5.md) | Same operations in VS Code and PyCharm (IntelliJ map for Java batches) |

If the batch has only **four** live slots, run Sessions 1–4 in class. Session 5 is homework. The IDE does not replace Git knowledge — that is why it is last.

**Labs:** [labs/01_git_portfolio_hygiene](labs/01_git_portfolio_hygiene/) (after Session 2) · [labs/02_git_desk_incidents](labs/02_git_desk_incidents/) (after Session 4)

**Calendar note:** Python FS and Java FS currently list Git on S44–S45. This pack is five sittings. Map 1–2 to those live sessions and 3–5 to extra lab, or run a Git block. Calendars: [Python](../PYTHON/Session_Calendar_100.md) · [Java](../JAVA/Session_Calendar_100.md)

---

## Not in this 6-hour course

Do not spend class time on these. They belong in a later Advanced Git sitting if the batch needs them.

- Git internals (objects, how Git stores files)
- Advanced `reset`, rebase, cherry-pick, reflog, detached HEAD
- Submodules and hooks
- Advanced GitHub administration
- Several branching strategies (we use **main + feature branch + Pull Request** only)
- A 30-command reference

Safe undo in Session 4 is enough: unstage, discard local edits, fix the last *local* commit, revert a commit that was already pushed. We will not drill dangerous history rewriting.

---

## Why this pack is shared

Git does not care whether the file is `.py` or `.java`. The history, the branch, and GitHub are the same.

The only stack-specific list is **what to ignore** later: Python regenerates `venv/` and `__pycache__/`; Java regenerates `target/` and `*.class`.
