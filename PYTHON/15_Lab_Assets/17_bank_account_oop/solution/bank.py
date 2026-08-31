"""SOLUTION — BankAccount (print + return; Exceptions week adds raise)."""


class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self.__balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        if amount > self.__balance:
            print("insufficient funds")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate=0.04):
        self.deposit(self.get_balance() * rate)


if __name__ == "__main__":
    a = BankAccount("Anita", 1000)
    a.deposit(200)
    a.withdraw(100)
    print("ok", a.get_balance())
