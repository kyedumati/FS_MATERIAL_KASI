"""BROKEN string cleaners — fix bugs (no def)."""

raw_email = "  Ravi@Gmail.COM "
# Bug 1: no strip
email = raw_email.lower()
print(email)

raw_phone = "+91-98765-43210"
digits = ""
for ch in raw_phone:
    if ch.isdigit():
        digits = digits + ch
# Bug 2: keeps country code 91 → 12 digits still printed
print(digits)

phone = "9876543210"
# Bug 3: wrong slice for mask
masked = "*" * 6 + phone[0:4]
print(masked)
