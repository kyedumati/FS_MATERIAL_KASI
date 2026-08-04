# Ticket: Stop SQL Injection

**Customer:** Security review  
**Need:** Replace string-built SQL with parameterized query.

## Broken
`broken/login_query.py` is injectable. Fix like `solution/`.

**Sessions:** ~55
