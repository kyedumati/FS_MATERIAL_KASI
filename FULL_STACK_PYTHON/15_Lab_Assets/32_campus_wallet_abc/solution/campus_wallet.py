"""SOLUTION — abstract Account + Payable wallet. print+return only."""

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder, opening):
        self.holder = holder
        self._balance = float(opening)

    def deposit(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        if amount > self._balance:
            print("insufficient funds")
            return
        self._balance -= amount

    def get_balance(self):
        return self._balance

    @abstractmethod
    def kind(self):
        pass

    def print_slip(self):
        print(self.kind(), "|", self.holder, "₹" + str(int(self._balance)))


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class SavingsAccount(Account):
    def __init__(self, holder, opening, rate=0.04):
        super().__init__(holder, opening)
        self.rate = rate

    def kind(self):
        return "savings"

    def add_interest(self):
        self.deposit(self.get_balance() * self.rate)


class WalletAccount(Account, Payable):
    def kind(self):
        return "wallet"

    def pay(self, amount):
        before = self.get_balance()
        self.withdraw(amount)
        if self.get_balance() == before:
            return False
        print("Paid ₹" + str(int(amount)), "from wallet")
        return True


if __name__ == "__main__":
    accounts = [
        SavingsAccount("Priya", 1000, 0.04),
        WalletAccount("Ravi", 500),
    ]
    for a in accounts:
        a.print_slip()

    ok = accounts[1].pay(120)
    print("pay ok?", ok)
    accounts[1].print_slip()

    accounts[0].add_interest()
    accounts[0].print_slip()
