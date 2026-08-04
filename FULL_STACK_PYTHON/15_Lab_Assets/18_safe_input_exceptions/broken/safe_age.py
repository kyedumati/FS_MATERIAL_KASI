"""BROKEN."""

def read_age(raw: str) -> int:
    # Bug 1: bare except
    try:
        age = int(raw)
    except:
        return -1
    # Bug 2: no range check
    return age
