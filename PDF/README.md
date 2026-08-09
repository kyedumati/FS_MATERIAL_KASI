# Generated PDFs

This folder is **auto-generated**. Do not edit files here.

**Requirements:** Python (`markdown`, `pygments`), Google Chrome, and **Node.js (`npx`)** so Mermaid diagrams render as SVG (not raw ```mermaid code).

## Primary Full Stack course (teach + share same content)

From the repo root:

```bash
./scripts/build.sh fullstack
# rebuild one module after Mermaid/CSS changes:
python3 scripts/build_pdfs.py --force --file FULL_STACK_PYTHON/03_Advanced_Python/01_Functions_Decorators_Generators.md
```

PDFs are written to:

```
PDF/FULL_STACK_PYTHON/
├── Session_Calendar_100.pdf
├── Capstone_CampusCart_One_Pager.pdf
├── Standard_Project_Deliverables.pdf
├── Tested_Toolchain.pdf
├── 01_Foundations/
├── 02_Core_Python/
└── ...
```
(`14_Trainer_Only` is excluded automatically.)

Student markdown pack (no PDFs required):

```bash
./scripts/pack_student_share.sh
# → dist/FULL_STACK_PYTHON_STUDENT/
```

Also share sibling **`MYSQL/`** (or build MySQL PDFs below) for Weeks 10–11.

## Other builds

```bash
./scripts/build.sh mysql    # → PDF/MYSQL/
```

Legacy `PDF/PYTHON/` was **removed** — do not rebuild a parallel Python-only pack.
