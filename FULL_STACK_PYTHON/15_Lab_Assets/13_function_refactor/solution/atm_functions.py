"""SOLUTION — functions + if/print (no type hints / exceptions)."""


def show_menu():
    print("1) Balance  2) Deposit  3) Withdraw  4) Quit")


def looks_like_number(text):
    text = text.strip()
    if not text or text.count(".") > 1:
        return False
    return text.replace(".", "", 1).isdigit()


def deposit(balance, amount):
    if amount <= 0:
        print("amount must be positive")
        return balance
    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        print("amount must be positive")
        return balance
    if amount > balance:
        print("insufficient funds")
        return balance
    return balance - amount


def main():
    balance = 1000.0
    while True:
        show_menu()
        choice = input("> ").strip()
        if choice == "1":
            print(f"₹{balance:.2f}")
        elif choice == "2":
            raw = input("amt: ").strip()
            if not looks_like_number(raw):
                print("Enter a number")
                continue
            balance = deposit(balance, float(raw))
        elif choice == "3":
            raw = input("amt: ").strip()
            if not looks_like_number(raw):
                print("Enter a number")
                continue
            balance = withdraw(balance, float(raw))
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
