"""SOLUTION — generator over rows (no csv/open yet — Files week later)."""

SAMPLE_ROWS = [
    {"name": "Anita", "city": "Hyderabad"},
    {"name": "Ravi", "city": "Chennai"},
    {"name": "Priya", "city": "Bengaluru"},
]


def iter_rows(rows):
    for row in rows:
        yield row


if __name__ == "__main__":
    for i, row in enumerate(iter_rows(SAMPLE_ROWS)):
        print(row)
        if i >= 2:
            break
