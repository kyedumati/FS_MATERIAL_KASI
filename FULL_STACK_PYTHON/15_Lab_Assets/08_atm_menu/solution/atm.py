"""SOLUTION ATM — while/if only (no def/global — Functions week later)."""

balance = 1000.0

while True:
    print("1) Balance  2) Deposit  3) Withdraw  4) Quit")
    choice = input("> ").strip()
    if choice == "1":
        print(f"Balance: ₹{balance:.2f}")
    elif choice == "2":
        amount_raw = input("Amount: ").strip()
        if not amount_raw.replace(".", "", 1).isdigit():
            print("Enter a number")
            continue
        amount = float(amount_raw)
        if amount <= 0:
            print("Amount must be positive")
            continue
        balance = balance + amount
    elif choice == "3":
        amount_raw = input("Amount: ").strip()
        if not amount_raw.replace(".", "", 1).isdigit():
            print("Enter a number")
            continue
        amount = float(amount_raw)
        if amount <= 0:
            print("Amount must be positive")
        elif amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - amount
            print(f"Balance: ₹{balance:.2f}")
    elif choice == "4":
        print("Bye")
        break
    else:
        print("Invalid choice")
