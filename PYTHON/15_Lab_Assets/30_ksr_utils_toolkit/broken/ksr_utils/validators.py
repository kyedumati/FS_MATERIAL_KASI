def is_phone_in(value: str) -> bool:
    # Bug: keeps country code; 12 digits still "pass"
    digits = "".join(ch for ch in value if ch.isdigit())
    return len(digits) >= 10
