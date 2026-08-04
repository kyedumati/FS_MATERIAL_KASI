def average(marks: list[float]) -> float:
    if not marks:
        raise ValueError("marks required")
    return sum(marks) / len(marks)


def format_inr(amount: float) -> str:
    return f"₹{amount:,.2f}"
