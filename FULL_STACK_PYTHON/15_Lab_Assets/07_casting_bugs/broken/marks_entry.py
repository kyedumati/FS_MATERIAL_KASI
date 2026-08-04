"""BROKEN — casting bugs."""

# Bug 1: int() rejects 78.5
m1 = int(input("Subject 1: "))
m2 = int(input("Subject 2: "))
m3 = int(input("Subject 3: "))

# Bug 2: average truncated for display
avg = (m1 + m2 + m3) / 3
print("Average:", int(avg))  # Bug 3: hides decimals
