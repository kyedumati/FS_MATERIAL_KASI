"""BROKEN OOP."""

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance  # Bug 1: public — anyone can set -99999

    def withdraw(self, amount):
        self.balance -= amount  # Bug 2: no checks


if __name__ == "__main__":
    a = BankAccount("Anita", 100)
    a.balance = -5000
    a.withdraw(99999)
    print(a.balance)
