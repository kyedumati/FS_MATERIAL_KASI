from ksr_utils import *
from ksr_utils.decorators import set_token

@timing
def slow_add(a, b):
    return a + b

@require_token
def secret_area():
    return "welcome"

print("email", is_email("ravi@ksr.com"))
print("phone", is_phone_in("+91-9876543210"))
print("inr", format_inr(10))
print("date", format_date(2, 1, 2026))
print(slow_add(1, 2))
print(secret_area())
set_token("x")
print(secret_area())
priced = with_gst([100, 40, 200])
print("gst", priced)
print("high", keep_high(priced, 50))
print("ok")
