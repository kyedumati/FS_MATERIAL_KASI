# Ticket: Git desk incidents

**Customer:** Batch lead (demo in ten minutes)  
**Need:** Three planted messes — ignore/secret, conflicted README, dirty feature work. Fix them with Session 4 moves.

Copy `broken/` to a throwaway folder and `git init` if you want real `status`. Conflict markers in `README.md` are already in the file (simulated merge). Dummy secrets must never be committed.

## Ticket A — secret and ignore

`broken/.gitignore` is wrong. `broken/leaked.env` is a dummy password file (stands in for `.env`). Ignore `.env` and `leaked.env`. Keep `broken/.env.example` (template is OK).

## Ticket B — README conflict

`broken/README.md` still has `<<<<<<<` markers. Leave one sensible title and body. No markers in the final file.

## Ticket C — hotfix while dirty

`broken/NOTES.txt` is WIP on a feature. `broken/HABIT.md` is the demo file. Practise: stash (or commit WIP on a feature branch), switch mindset to "hotfix HABIT.md", then restore WIP. You do not need two real branches if you talk through the commands; stronger students `git init` and run stash for real.

## Done when

- [ ] Dummy `leaked.env` / `.env` is not tracked; `.gitignore` covers `.env`, `leaked.env`, `venv/`, `target/`, `*.class`
- [ ] README has no conflict markers
- [ ] You can say when you would `stash` vs commit on `feature/...`
