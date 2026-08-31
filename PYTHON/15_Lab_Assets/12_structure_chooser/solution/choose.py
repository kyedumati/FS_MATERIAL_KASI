"""SOLUTION — structure choices + list stack (no def)."""

ANSWERS = {
    "shopping cart ordered items": "list",
    "RGB color fixed 3 numbers": "tuple",
    "unique employee IDs": "set",
    "roll_no → student name": "dict",
}

stack = []
stack.append("type")
stack.append("save")
last = stack.pop()
print(last)
print(ANSWERS)
