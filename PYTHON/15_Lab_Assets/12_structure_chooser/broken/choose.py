"""BROKEN stack — should be LIFO (no def)."""

stack = []
stack.append("a")
stack.append("b")
# Bug: index 0 removes oldest (queue) not LIFO
print(stack.pop(0))  # should be b for a stack — fix to pop()
