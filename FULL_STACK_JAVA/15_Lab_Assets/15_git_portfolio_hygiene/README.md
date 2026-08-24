# Ticket: Clean GitHub Repo Hygiene

**Customer:** Hiring manager  
**Need:** Fix `.gitignore` so bytecode, Maven `target/`, and secrets are never committed; write a README a classmate can run.

**Teaching-order:** Git add/commit, Java/Maven `.gitignore`, project README. No new Java. No JDBC. No Spring. No Lombok. No MySQL. `target/` is a folder name you ignore — you do not need a `pom.xml` this week.

## Starter
Complete `starter/.gitignore` and `starter/README.md`. Ignore `target/`, `*.class`, `.env`, `.idea/`, `.DS_Store`. Do **not** ignore `*.java`. README must name the project, say what it does, and show `javac` / `java` steps.

## Broken
`broken/.gitignore` is wrong — fix it. Do **not** commit `.env`. `broken/.env.example` is a dummy template (OK to commit). A real `.env` is not.

## Seed
`seed/commit_message_examples.txt` — imperative / conventional examples for the daily-commit habit.

## Done when
- [ ] `.gitignore` ignores `target/`, `*.class`, `.env`, `.idea/`, `.DS_Store`
- [ ] `*.java` is **not** ignored
- [ ] `!.env` (un-ignore) is **not** in the file
- [ ] README has title, one-line purpose, JDK 17, `javac …` and `java …` run steps, author line
- [ ] `git status` does not list `.env`, `*.class`, or `target/` (create dummy files locally to prove it)
- [ ] No JDBC / Spring / Lombok / MySQL

## Stretch
- Add `.env.example` with dummy keys only (no real PIN).
- Open a solo Pull Request on `feature/readme` after push.
- GitHub Topics: `java`, `jdk17`, `portfolio`.
- **Later — Maven week:** confirm `target/` still stays untracked after the first `mvn` build.
