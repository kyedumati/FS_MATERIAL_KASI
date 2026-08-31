"""SOLUTION — canteen calc for Variables/IO week (no if/while/def yet)."""

GST_RATE = 0.05

price = float(input("Price: ").strip())
qty = int(input("Qty: ").strip())
subtotal = price * qty
total = round(subtotal * (1 + GST_RATE), 2)
print(f"Total: ₹{total:.2f}")
