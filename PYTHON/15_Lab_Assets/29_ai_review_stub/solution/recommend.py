"""SOLUTION — rule-based stub (sklearn optional stretch)."""

def score_review(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("text required")
    words = text.lower().split()
    pos = sum(w in {"good", "great", "love", "excellent"} for w in words)
    neg = sum(w in {"bad", "slow", "hate", "poor"} for w in words)
    if pos == neg:
        label = "neu"
    elif pos > neg:
        label = "pos"
    else:
        label = "neg"
    return {"label": label, "score": float(pos - neg)}


if __name__ == "__main__":
    assert score_review("Great food, love it")["label"] == "pos"
    assert score_review("Bad service, too slow")["label"] == "neg"
    print("ok")
