"""STARTER — refactor into functions (Functions week — def OK; no type hints required)."""


def show_menu():
    print("1) Balance  2) Deposit  3) Withdraw  4) Quit")


def deposit(balance, amount):
    # TODO: if amount <= 0: print message; return balance unchanged
    # TODO: else return balance + amount
    return balance


def withdraw(balance, amount):
    # TODO: if amount <= 0 or amount > balance: print message; return balance
    # TODO: else return balance - amount
    return balance


def main():
    balance = 1000.0
    # TODO: loop calling helpers; check amount text before float()
    print(balance)


if __name__ == "__main__":
    main()
