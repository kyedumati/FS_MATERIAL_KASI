# Assessment & Practice Answer Keys (Trainer Only)

Teaching modules contain `**Answer:**` / `**Model answer:**` under **Practice Exercises** and `### Interview answers` in the **teaching copy** (`FULL_STACK_PYTHON/`, `FRONTEND/`) for live discussion.

The **student pack** strips those automatically via `scripts/strip_trainer_sections.py`. Discuss-in-class questions and Practice **prompts** remain; model solutions do not ship to students.

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

Student pack also strips `### Interview answers` and prose/code that follows `**Model answer:**`.

Create `keys/` as needed per batch; do not commit real exam papers with cohort names if your policy forbids it.
