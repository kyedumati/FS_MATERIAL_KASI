"""STRETCH after Session 31 — not part of core functions homework."""

SAMPLE_ROWS = [
    {"sku": "TEA", "qty": "2"},
    {"sku": "SAMOSA", "qty": "1"},
]


def read_rows(rows):
    for row in rows:
        yield row
