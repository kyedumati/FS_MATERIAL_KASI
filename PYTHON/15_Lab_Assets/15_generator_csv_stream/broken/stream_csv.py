"""BROKEN — returns a list instead of yielding."""

SAMPLE_ROWS = [
    {"name": "Anita", "city": "Hyderabad"},
]


def iter_rows(rows):
    # Bug: builds a full list instead of yielding one-by-one
    return list(rows)


if __name__ == "__main__":
    print(len(iter_rows(SAMPLE_ROWS)))
