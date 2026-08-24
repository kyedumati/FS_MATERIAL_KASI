"""BROKEN — concrete Account; wallet pay is a typo; checkout is a type switch."""

from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Account:  # Bug 1: not ABC — Account(...) still works
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

    def kind(self):
        return "account"  # Bug 2: fake kind — children can skip a real override

    def print_slip(self):
        print(self.kind(), "|", self.holder, "₹" + str(int(self._balance)))


class SavingsAccount(Account):
    def __init__(self, holder, opening, rate=0.04):
        super().__init__(holder, opening)
        self.rate = rate

    def kind(self):
        return "savings"

    def add_interest(self):
        self.deposit(self.get_balance() * self.rate)


class WalletAccount(Account):  # Bug 3: does not inherit Payable
    def kind(self):
        return "wallet"

    def paay(self, amount):  # Bug 4: misspelled — not Payable.pay
        self.withdraw(amount)
        return True


def checkout(account, amount):
    if account.kind() == "savings":  # Bug 5: type switch instead of Payable
        print("savings cannot pay here")
    elif account.kind() == "wallet":
        account.paay(amount)
    else:
        print("unknown account")


if __name__ == "__main__":
    generic = Account("Campus", 0)  # Bug 1 visible: should not be constructible
    s = SavingsAccount("Priya", 1000, 0.04)
    w = WalletAccount("Ravi", 500)
    checkout(s, 50)
    checkout(w, 120)
    generic.print_slip()
    s.print_slip()
    w.print_slip()
