# Assessment & Practice Answer Keys (Trainer Only)

Teaching modules contain `**Answer:**` / `**Model answer:**` under **Practice Exercises** in the **teaching copy** (`FULL_STACK_PYTHON/`, `FRONTEND/`) for live drills.

**Interview & Discussion Q&A** (questions **and** model answers) is **shared** with students — material is handed out after concepts and the mini-project, so keys in that section stay in the student pack.

The **student pack** strips Practice `**Model answer:**` blocks automatically via `scripts/strip_trainer_sections.py`. Practice **prompts** remain; Practice model solutions do not ship to students.

## Graded tests (biweekly)

1. Use papers under [`../16_Assessments/`](../16_Assessments/) — not Practice items as scored exams.  
2. Keep `*_KEY.md` private (excluded from student pack).  
3. Do not reuse unchanged Practice Model answers as the biweekly key.

## Quick extract

From repo root:

```bash
rg -n "\*\*(Answer|Model answer|Model):\*\*" FULL_STACK_PYTHON/02_Core_Python/03_Flow_Control.md \
  > FULL_STACK_PYTHON/14_Trainer_Only/keys/flow_control_answers.txt
```

Student pack strips prose/code that follows `**Model answer:**` under Practice Exercises. It does **not** strip Interview & Discussion Q&A answers.

Create `keys/` as needed per batch; do not commit real exam papers with cohort names if your policy forbids it.
