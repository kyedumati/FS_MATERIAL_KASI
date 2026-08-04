"""SOLUTION: order-preserving dedupe (no def)."""

print("=== Dedup Tool ===")
raw = input("Enter IDs comma-separated: ")

ids = []
for part in raw.split(","):
    item = part.strip()
    if item != "":
        ids.append(item)

clean = list(dict.fromkeys(ids))
print("Original count:", len(ids))
print("Unique count:", len(clean))
print("Clean list:", clean)
