"""BROKEN ATM — fix quit + overdraft (no def)."""

balance = 1000.0

while True:  # Bug 1/3: option 4 prints Bye but never breaks
    print("1) Balance  2) Deposit  3) Withdraw  4) Quit")
    choice = input("> ").strip()
    if choice == "1":
        print(balance)
    elif choice == "2":
        amount = float(input("Amount: "))
        balance = balance + amount
    elif choice == "3":
        amount = float(input("Amount: "))
        # Bug 2: allows overdraft
        balance = balance - amount
        print("New balance", balance)
    elif choice == "4":
        print("Bye")
        # Bug 3: forgot break
    else:
        print("Invalid")
