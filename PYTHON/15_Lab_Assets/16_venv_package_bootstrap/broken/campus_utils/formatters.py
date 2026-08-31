def format_inr(amount: float) -> str:
    return "Rs." + str(amount)  # Bug: no 2-decimal, no rupee symbol consistency
