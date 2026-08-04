"""BROKEN: set loses order; empty tokens kept."""

print("=== Dedup Tool ===")
raw = input("Enter IDs: ")
# Bug 1: keeps empty / spaces
ids = raw.split(",")
# Bug 2: set loses first-seen order
clean = list(set(ids))
print(len(ids), clean)
