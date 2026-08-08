# Lab Assets (Runnable Classroom Kits)

Notes teach; **these folders run**. Start every major concept with a **customer ticket**, then `starter/` or `broken/`.

## Layout convention

```
15_Lab_Assets/
  <nn>_<name>/
    README.md     # ticket (start here)
    starter/      # incomplete — learners extend
    broken/       # intentional bugs — debug lab
    solution/     # reference answers (not in the student pack)
    seed/         # sample CSV/JSON/SQL when needed
```

## Full index (all concepts)

| Kit | Sessions | Ticket |
|-----|----------|--------|
| [01_python_expense_tracker](01_python_expense_tracker/) | ~42–45 | Ticket: Expense Tracker CSV Export |
| [02_mysql_library_seed](02_mysql_library_seed/) | ~50–55 | Ticket: Library join report |
| [03_django_auth_tasks](03_django_auth_tasks/) | ~71–77 | Ticket: Private tasks per user |
| [04_drf_products](04_drf_products/) | ~82–85 | Ticket: Product JSON API for mobile |
| [06_cli_calculator](06_cli_calculator/) | ~06–10 | Ticket: Campus Canteen Calculator |
| [07_casting_bugs](07_casting_bugs/) | ~09 | Ticket: Marks Entry Keeps Crashing |
| [08_atm_menu](08_atm_menu/) | ~11–15 | Ticket: Mini ATM Menu |
| [09_string_parser](09_string_parser/) | ~16–17 | Ticket: Registration Field Cleaner |
| [10_marks_manager](10_marks_manager/) | ~18–20 | Ticket: Student Marks Manager (CLI) |
| [11_contact_book](11_contact_book/) | ~23–25 | Ticket: Contact Book |
| [12_structure_chooser](12_structure_chooser/) | ~26–27 | Ticket: Pick the Right Structure |
| [13_function_refactor](13_function_refactor/) | ~28–32 | Ticket: Refactor ATM Into Functions |
| [14_decorator_login_gate](14_decorator_login_gate/) | ~30–31 | Ticket: Login Gate Decorator |
| [15_generator_csv_stream](15_generator_csv_stream/) | ~31 | Ticket: Stream Large CSV |
| [16_venv_package_bootstrap](16_venv_package_bootstrap/) | ~33–35 | Ticket: Ship a Tiny Utils Package |
| [17_bank_account_oop](17_bank_account_oop/) | ~36–39 | Ticket: BankAccount Class |
| [18_safe_input_exceptions](18_safe_input_exceptions/) | ~40–41 | Ticket: Never Crash on Bad Input |
| [19_git_portfolio_hygiene](19_git_portfolio_hygiene/) | ~44–45 | Ticket: Clean GitHub Repo Hygiene |
| [20_sql_injection_demo](20_sql_injection_demo/) | ~55 | Ticket: Stop SQL Injection |
| [24_django_url_views_stub](24_django_url_views_stub/) | ~63–67 | Ticket: Two Pages With One Base Template |
| [25_flask_notes_api](25_flask_notes_api/) | ~81 | Ticket: Tiny Notes JSON API |
| [26_unittest_utils](26_unittest_utils/) | ~91–92 | Ticket: Tests Must Catch the Bug |
| [27_terminal_workspace](27_terminal_workspace/) | ~01–02 | Ticket: Messy Desktop → Clean Workspace |
| [29_ai_review_stub](29_ai_review_stub/) | optional after S95 | Ticket: Optional AI Recommend Endpoint |
| [30_ksr_utils_toolkit](30_ksr_utils_toolkit/) | ~28–35 | Ticket: Ship `ksr_utils` (validators, formatters, decorators, generators) |
| [31_email_id_dedup](31_email_id_dedup/) | ~21–22 | Ticket: Clean Duplicate IDs Before Import |

### Shared topic labs (outside this folder)

| Kit | Location |
|-----|----------|
| HTML / CSS / JS labs | [`FRONTEND/labs/`](../../FRONTEND/labs/) |
| React labs | [`FRONTEND/REACT/labs/`](../../FRONTEND/REACT/labs/) |

## How to use a kit

1. Open the kit folder (or copy `starter/` / `broken/` into your workspace).
2. Read the kit `README.md` ticket first — code before long theory.
3. Work the ticket solo or in pairs.
4. Compare with `solution/` only after you finish (or when told in class).

## Student pack policy

`solution/` folders are **stripped** by `scripts/pack_student_share.sh`. Starter/broken/seed remain.

## Map to modules

Each teaching module has a **Classroom Ticket** section linking here. Session order stays in [Session_Calendar_100.md](../Session_Calendar_100.md).
