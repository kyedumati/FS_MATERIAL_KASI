"""BROKEN — crashes on empty."""

def score_review(text: str) -> dict:
    text = text.lower()
    # Bug: no empty check
    words = text.split()
    pos = sum(w in {"good", "great", "love"} for w in words)
    neg = sum(w in {"bad", "slow", "hate"} for w in words)
    return {"label": "pos" if pos >= neg else "neg", "score": pos - neg}
