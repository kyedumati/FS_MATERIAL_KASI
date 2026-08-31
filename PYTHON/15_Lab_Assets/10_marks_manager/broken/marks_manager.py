"""BROKEN marks manager — fix bugs (no def)."""

marks = [95, 88]

# Bug 1: average crashes conceptually when empty — try printing avg after clearing
marks.clear()
# Bug 1: ZeroDivision when empty
print("avg", sum(marks) / len(marks))

marks = [95, 88, 90]
# Bug 2: toppers uses > instead of >= (90 should count)
toppers = []
for m in marks:
    if m > 90:
        toppers.append(m)
print("toppers", toppers)

# Bug 3: remove missing value crashes
marks.remove(70)
