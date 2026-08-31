"""BROKEN — returns a list instead of yielding."""

SAMPLE_ROWS = [
    {"sku": "TEA", "qty": "2"},
]


def read_rows(rows):
    # Bug: loads everything into a list
    return list(rows)
