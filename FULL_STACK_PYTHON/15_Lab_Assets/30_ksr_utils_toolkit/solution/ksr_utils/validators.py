def is_email(value):
    value = value.strip()
    if value.count("@") != 1:
        return False
    local, domain = value.split("@")
    return bool(local) and "." in domain


def is_phone_in(value):
    digits = ""
    for ch in value:
        if ch.isdigit():
            digits = digits + ch
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return len(digits) == 10


def is_positive(value):
    return value > 0
