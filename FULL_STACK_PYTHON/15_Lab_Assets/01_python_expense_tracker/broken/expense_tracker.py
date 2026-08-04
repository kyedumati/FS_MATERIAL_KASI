"""BROKEN on purpose — find and fix 3 bugs."""

import csv


class Expense:
    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category


expenses = []


def add_expense(title, amount, category=[]):  # Bug 1: mutable default
    if amount < 0:  # Bug 2: should reject == 0 too
        print("bad amount")
        return
    expenses.append(Expense(title, amount, category))  # Bug 3 if category becomes a list


def export_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "amount", "category"])
        for e in expenses:
            writer.writerow([e.title, e.amount, e.category])


if __name__ == "__main__":
    add_expense("Bus", 40, "Travel")
    add_expense("Snack", 0, "Food")
    export_csv("out.csv")
    print("wrote out.csv — but check bugs above")
