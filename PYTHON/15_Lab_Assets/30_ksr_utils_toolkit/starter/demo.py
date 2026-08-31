"""Run from starter/: python demo.py

Functions homework — no generators required.
Stretch after S31: finish ksr_utils/generators.py and import read_rows here.
"""

from ksr_utils import (
    is_email,
    is_phone_in,
    is_positive,
    format_inr,
    format_date,
    timing,
    require_token,
    set_token,
    with_gst,
    keep_high,
)


@timing
def slow_add(a, b):
    return a + b


@require_token
def secret_area():
    return "welcome"


def main():
    print("email", is_email("  ravi@ksr.com "))
    print("phone", is_phone_in("+91-98765-43210"))
    print("pos", is_positive(10), is_positive(0))
    print("inr", format_inr(1234.5))
    print("date", format_date(3, 8, 2026))
    print(slow_add(2, 3))
    print(secret_area())  # denied until token set
    set_token("demo")
    print(secret_area())
    priced = with_gst([100, 40, 200])
    print("gst", priced)
    print("high", keep_high(priced, 50))
    print("ksr_utils demo OK")


if __name__ == "__main__":
    main()
