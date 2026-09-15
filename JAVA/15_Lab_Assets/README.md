# Lab Assets (Runnable Classroom Kits)

Notes teach; **these folders run**. Start every major concept with a **customer ticket**, then `starter/` or `broken/`.

## Layout convention

```
15_Lab_Assets/
  <nn>_<name>/
    README.md     # ticket (start here)
    starter/      # incomplete — learners extend
    broken/       # intentional bugs — debug lab
    solution/     # reference answers (do not share; pack script excludes)
    seed/         # sample CSV/JSON/SQL when needed
```

## Index

| Kit | Sessions | Ticket | Status |
|-----|----------|--------|--------|
| [01_terminal_workspace](01_terminal_workspace/) | ~01–02 | Messy Desktop → Clean Workspace | **Ready** |
| [02_hello_javac](02_hello_javac/) | ~03–05 | First `HelloJava` compile/run | **Ready** |
| [03_canteen_calculator](03_canteen_calculator/) | ~06–10 | Campus Canteen Calculator | **Ready** |
| [04_casting_bugs](04_casting_bugs/) | ~09 | Marks Entry Keeps Crashing | **Ready** |
| [05_atm_menu](05_atm_menu/) | ~11–15 | Mini ATM Menu | **Ready** |
| [06_string_parser](06_string_parser/) | ~16–17 | Registration Field Cleaner | **Ready** |
| [07_marks_manager](07_marks_manager/) | ~18–20 | Student Marks Manager (arrays) | **Ready** |
| [08_methods_refactor](08_methods_refactor/) | ~21–23 | Refactor ATM Into Methods | **Ready** |
| [09_bank_account_oop](09_bank_account_oop/) | ~24–30 | BankAccount (private balance) | **Ready** |
| [10_employee_inheritance](10_employee_inheritance/) | ~31–33 | Staff hierarchy (`extends` / `super`) | **Ready** |
| [11_campus_wallet](11_campus_wallet/) | ~34–36 | Abstract `Account` + `Payable` + poly loop | **Ready** |
| [12_collections_inventory](12_collections_inventory/) | ~37–40 | Canteen inventory (`List` / `Set` / `Map`) | **Ready** |
| [13_safe_input_exceptions](13_safe_input_exceptions/) | ~41–42 | Never Crash on Bad Input | **Ready** |
| [14_expense_files](14_expense_files/) | ~43 | Expense CSV append | **Ready** |
| [15_git_portfolio_hygiene](15_git_portfolio_hygiene/) | ~44–45 | Pointer → [`GIT/labs/01_git_portfolio_hygiene`](../../GIT/labs/01_git_portfolio_hygiene/) | **Ready** |
| [16_jdbc_library_crud](16_jdbc_library_crud/) | ~55–58 | Library CRUD + no concat SQL | **Ready** |
| [17_spring_hello_rest](17_spring_hello_rest/) | ~66–70 | Two JSON endpoints + in-memory GET list | **Ready** |
| [18_jpa_product_crud](18_jpa_product_crud/) | ~71–74 | Product JPA catalog + DTO / `@Valid` / Postman v1 | **Ready** |
| [19_spring_auth_tasks](19_spring_auth_tasks/) | ~75–80 | JWT register/login + protect POST; Lab 06 freeze (400/404 + demo bundle); Lab 07 Actuator health + env / PaaS / M0 on the same API | **Ready** |
| `20_junit_utils` | ~91–92 | Tests Must Catch the Bug | Planned |
| `21_ai_review_stub` | optional after S95 | Optional AI recommend endpoint | Planned |

MySQL seed labs stay in [`MYSQL/`](../../MYSQL/) (required via the FS bridge). Git kits: [`GIT/labs/`](../../GIT/labs/). Frontend kits: [`FRONTEND/labs/`](../../FRONTEND/labs/) · [`FRONTEND/REACT/labs/`](../../FRONTEND/REACT/labs/).

Kits 20+ are created when that calendar phase is authored (teaching-order rule: session **S** kits may only use syntax from sessions **1…S**). Kit 19 core path is register / login (BCrypt + JWT), public GET `/products`, protected POST `/products`. Lab 06 freeze also requires GET by id 200/404, POST invalid with Bearer → 400, README/demo bundle, and peer break-auth on `broken/`. Lab 07 (same kit, later sessions) adds Actuator `/actuator/health`, host env, a PaaS attempt or blocked note, and capstone M0 — it does **not** change Lab 06 freeze Done when.

## How to use a kit

1. Open the kit folder (or copy `starter/` / `broken/` into your workspace).
2. Read the kit `README.md` ticket first — code before long theory.
3. Work the ticket solo or in pairs.
4. Compare with `solution/` only after you finish (or when told in class).

## Student pack policy

`solution/` folders are **excluded** by `scripts/pack_student_share.sh java` and should not be shared. Starter/broken/seed remain.

## Map to modules

Lab kits live under this folder. Session order stays in [Session_Calendar_100.md](../Session_Calendar_100.md). Modules link kits from **Mini-Project** (and practice) — there is no separate Classroom Ticket section.
