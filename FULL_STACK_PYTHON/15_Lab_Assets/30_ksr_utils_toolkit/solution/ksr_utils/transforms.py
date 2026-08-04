"""map / filter helpers (functions homework — no yield)."""


def with_gst(prices, rate=0.05):
    return list(map(lambda p: round(p * (1 + rate), 2), prices))


def keep_high(prices, minimum=50):
    return list(filter(lambda p: p >= minimum, prices))
