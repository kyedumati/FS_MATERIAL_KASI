"""BROKEN — bare except; no range check. No type hints."""

def read_age(raw):
    # Bug 1: bare except
    try:
        age = int(raw)
    except:
        return -1
    # Bug 2: no range check
    return age
