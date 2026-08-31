# Sample Answer Keys Index (Trainer)

Most module files embed **Answer:** under MCQs for rapid classroom use.  
Use this index when preparing **sealed** tests (shuffle options; remove answers from handouts).

## High-stakes topics — verify learners can do, not only pick MCQ

| Topic | Practical key (must demonstrate) |
|-------|----------------------------------|
| Flow control | Working ATM/menu without infinite loop bugs |
| Dicts/lists | Contact book / marks CRUD |
| SQL JOIN | INNER JOIN employees↔departments; explain LEFT JOIN NULLs |
| Django auth | `@login_required` + owner-scoped queryset |
| DRF Product API | Full CRUD from [APIs module Steps 3–5](../09_APIs_REST/01_APIs_JSON_Postman_DRF.md); 201 create JSON; 400 on negative price |
| Deploy | `load_dotenv` present; `STORAGES`; `check --deploy` run |

## Sample sealed MCQ set (Core Python — Flow)

1. `for i in range(3):` iterates how many times? → **3** (0,1,2)  
2. `break` exits… → **innermost loop**  
3. `elif` runs when… → **prior conditions false and its condition true**  
4. Infinite `while True` stopped by… → **`break` or kill process**  

## Sample sealed coding prompt (Django)

“Add `login_required` to create_task and ensure Task.owner is request.user. Write the view.”  

**Key points to award marks:** decorator or mixin; `form.instance.owner = request.user`; redirect; csrf in template (ask separately).

## Sample sealed SQL prompt

```sql
-- Expected shape (names may vary):
SELECT o.id, c.name, o.total
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id
WHERE o.total > 1000
ORDER BY o.total DESC;
```

## DRF expected responses

Documented in learner module (Steps 3–6). For sealed test: ask learners to write serializer Meta.fields from memory and predict status codes.
