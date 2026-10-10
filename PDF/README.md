# Generated PDFs

**Kasi Yedumati · Full Stack Training**

This folder is **auto-generated**. Do not edit files here.

**Git:** student PDFs **are committed and pushed** to origin with the matching markdown. After you change a module `.md`, rebuild that PDF and include `PDF/**` in the same commit. Temporary preview folders (`.pdf_pages/`, `.cache/`) stay gitignored.

**Requirements:** Python (`markdown`, `pygments`), Google Chrome, and **Node.js (`npx`)** so Mermaid diagrams render as SVG (not raw ```mermaid code).

Every student PDF gets a masthead brand line: **Kasi Yedumati · Full Stack Training** (from `scripts/build_pdfs.py` + `pdf-style.css`).

## PDF visual conventions (in Markdown)

Authors can use these markers — `scripts/build_pdfs.py` styles them automatically:

| Marker | Renders as |
|--------|------------|
| `**Expected Output:**` + fence | Green output callout |
| `**Remember:**` / `**Interview:**` / `**Common Error:**` | Margin-style callouts |
| `**Where used?**` / `**When will I use this?**` | Green “real world” box |
| `**Key takeaways:**` (right after a Mermaid diagram) | Paired beside the diagram; use sparingly (major ideas only) |
| `**Icons:** Bank · UPI · Employee · Laptop · Order` | Icon chip strip |
| Inline `` `class` `` / `` `object` `` / `` `inheritance` `` | Blue / green / purple keywords |

## Full Stack courses (teach + share same content)

From the repo root:

```bash
./scripts/build.sh python             # → PDF/PYTHON/
./scripts/build.sh java               # → PDF/JAVA/
./scripts/build.sh git                # → PDF/GIT/ (shared Git and GitHub)
./scripts/build.sh frontend           # → PDF/FRONTEND/ (shared HTML/CSS/JS + React)
# rebuild one module after Mermaid/CSS changes:
python3 scripts/build_pdfs.py --force --file PYTHON/03_Advanced_Python/01_Functions_Decorators_Generators.md
python3 scripts/build_pdfs.py --force --file JAVA/06_Database_MySQL/01_MySQL_for_Full_Stack_Developers.md
```

PDFs are written to `PDF/PYTHON/`, `PDF/JAVA/`, `PDF/GIT/`, or `PDF/FRONTEND/` mirroring the source tree.

(`14_Trainer_Only` is excluded automatically.)

**One material:** these PDFs match the teaching markdown (Practice Model answers included). After each module, share **that module’s PDF** only.

Optional full markdown mirror (still excludes `14_Trainer_Only/`, `solution/`, `*_KEY.md`):

```bash
./scripts/pack_student_share.sh         # → dist/PYTHON_STUDENT/
./scripts/pack_student_share.sh java    # → dist/JAVA_STUDENT/
```

Also share sibling **`GIT/`** and **`MYSQL/`** (or build those PDFs) for Git and SQL weeks.

## Other builds

```bash
./scripts/build.sh mysql    # → PDF/MYSQL/ (nested: notes, homework/, labs/)
```
