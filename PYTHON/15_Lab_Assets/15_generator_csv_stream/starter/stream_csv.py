"""STARTER — yield dict rows from an in-memory list (CSV files come in Files week)."""

SAMPLE_ROWS = [
    {"name": "Anita", "city": "Hyderabad"},
    {"name": "Ravi", "city": "Chennai"},
    {"name": "Priya", "city": "Bengaluru"},
]


def iter_rows(rows):
    # TODO: for each row in rows: yield row
    if False:
        yield {}


if __name__ == "__main__":
    for row in iter_rows(SAMPLE_ROWS):
        print(row)
