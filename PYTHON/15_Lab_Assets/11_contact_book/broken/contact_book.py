"""BROKEN contact book — fix KeyError bugs (menu script, no def)."""

contacts = {"Anita": "9876543210"}

# Bug 1: lookup missing name crashes
print("lookup Ravi:", contacts["Ravi"])

# Bug 2: delete missing name crashes
del contacts["Ravi"]

# Bug 3: wrong key when listing
for name in contacts:
    print(name, contacts[name.upper()])
