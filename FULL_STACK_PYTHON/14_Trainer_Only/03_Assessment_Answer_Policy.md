# Assessment & Practice Answer Keys (Trainer Only)

**One material:** Teaching modules share Practice `**Model answer:**` and Interview Q&A with students when you send that module’s PDF after teaching.

## What stays private

1. Biweekly papers under [`../16_Assessments/`](../16_Assessments/) — students get `BW##_….md` only.  
2. Keep `*_KEY.md` private (never share; excluded from optional pack scripts).  
3. Do not use unchanged Practice Model answers as the biweekly exam key.  
4. Assign the paper as homework after the even week (or Friday wrap-up).  
5. Mark with the matching `*_KEY.md`; spot-review weak MCQ topics next session.

## Quick extract (optional prep)

From repo root:

```bash
rg -n "\*\*(Answer|Model answer|Model):\*\*" FULL_STACK_PYTHON/02_Core_Python/03_Flow_Control.md \
  > FULL_STACK_PYTHON/14_Trainer_Only/keys/flow_control_answers.txt
```

Create `keys/` as needed per batch; do not commit real exam papers with cohort names if your policy forbids it.
