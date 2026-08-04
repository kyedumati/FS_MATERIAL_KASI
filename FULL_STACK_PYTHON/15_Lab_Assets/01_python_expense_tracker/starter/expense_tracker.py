"""Campus expense tracker — STARTER (Files + logging week)."""

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
    # TODO: if amount <= 0: log error and raise ValueError; else append Expense
    pass


def export_csv(path):
    # TODO: write CSV with headers title,amount,category using csv.DictWriter
    pass


def main():
    print("Expense Tracker — implement add_expense & export_csv")
    # Demo once implemented:
    # add_expense("Tea", 20, "Food")
    # export_csv("my_expenses.csv")


if __name__ == "__main__":
    main()
