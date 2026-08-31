"""STARTER OOP — class/methods OK; no type hints / raise yet."""


class BankAccount:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        # TODO: store balance as __balance
        self.__balance = float(balance)

    def deposit(self, amount):
        # TODO: if amount <= 0: print and return; else add
        pass

    def withdraw(self, amount):
        # TODO: reject bad / overdraft with print; else subtract
        pass

    def get_balance(self):
        # TODO: return __balance
        return 0.0


if __name__ == "__main__":
    a = BankAccount("Anita", 1000)
    a.deposit(200)
    a.withdraw(100)
    print(a.get_balance())
