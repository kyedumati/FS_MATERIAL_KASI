"""STARTER — optional AI lite."""

def score_review(text: str) -> dict:
    # TODO: if sklearn available, use a tiny pipeline; else rule-based stub
    # Positive words: good, great, love; negative: bad, slow, hate
    raise NotImplementedError


if __name__ == "__main__":
    print(score_review("Great food, love it"))
    print(score_review("Bad service, too slow"))
