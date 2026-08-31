"""Reference solution — trainer only until lab ends."""

import csv
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")


class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


expenses = []


def add_expense(title, amount, category):
    if amount <= 0:
        logging.error("amount must be > 0, got %s", amount)
        raise ValueError("amount must be > 0")
    expenses.append(Expense(title.strip(), float(amount), category.strip()))
    logging.info("added %s", title)


def export_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "amount", "category"])
        writer.writeheader()
        for e in expenses:
            writer.writerow(
                {"title": e.title, "amount": e.amount, "category": e.category}
            )
    logging.info("exported %s rows to %s", len(expenses), path)


def main():
    add_expense("Tea", 20, "Food")
    add_expense("Bus", 40, "Travel")
    add_expense("Notebook", 80, "Stationery")
    export_csv("my_expenses.csv")
    print("Done → my_expenses.csv")


if __name__ == "__main__":
    main()
