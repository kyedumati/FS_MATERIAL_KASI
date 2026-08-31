"""BROKEN — fix 3 bugs. Script only."""

GST_RATE = 0.05

price = float(input("Price: ").strip())
qty = int(input("Qty: ").strip())
# Bug 1: uses // instead of *
subtotal = price // qty
# Bug 2: adds GST_RATE as rupees, not percent
total = subtotal + GST_RATE
# Bug 3: should print 2 decimals with f-string ₹
print("Total:", total)
