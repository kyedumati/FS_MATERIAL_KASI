# Generated PDFs

This folder is **auto-generated**. Do not edit files here.

## Primary Full Stack course (teach + share same content)

From the repo root:

```bash
./scripts/build.sh fullstack
```

PDFs are written to:

```
PDF/FULL_STACK_PYTHON/
├── 00_Course_Guide/
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
