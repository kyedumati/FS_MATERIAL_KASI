"""SOLUTION — string cleaning without def (Functions week later)."""

raw_email = "  Ravi@Gmail.COM "
email = raw_email.strip().lower()
print(email)

raw_phone = "+91-98765-43210"
digits = ""
for ch in raw_phone:
    if ch.isdigit():
        digits = digits + ch
if digits.startswith("91") and len(digits) == 12:
    digits = digits[2:]
if len(digits) == 10:
    phone = digits
else:
    phone = ""
print(phone)

phone = "9876543210"
if len(phone) != 10:
    masked = "invalid"
else:
    masked = "*" * 6 + phone[-4:]
print(masked)
