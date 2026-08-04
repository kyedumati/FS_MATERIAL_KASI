"""BROKEN — scope and defaults."""

def withdraw(balance, amount, history=[]):  # Bug 1 mutable default
    history.append(amount)
    balance = balance - amount  # Bug 2: local only — caller balance unchanged
    return history


if __name__ == "__main__":
    bal = 1000
    withdraw(bal, 100)
    print("balance still", bal)  # expected 900 if fixed properly
    print(withdraw(bal, 50))
