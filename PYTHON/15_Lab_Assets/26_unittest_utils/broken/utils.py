def average(marks: list[float]) -> float:
    return sum(marks) / len(marks) - 1  # BUG

def format_inr(amount: float) -> str:
    return f"Rs {amount}"  # BUG format
