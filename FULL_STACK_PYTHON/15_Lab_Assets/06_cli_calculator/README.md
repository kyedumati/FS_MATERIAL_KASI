# Ticket: Campus Canteen Calculator

**Customer:** Canteen counter staff  
**Bug/need:** Staff still use paper for `price × qty + GST`. Build a CLI calculator.

## Starter
Open `starter/calculator.py` — one price, one qty, print GST total.

## Broken
`broken/calculator.py` has bugs (integer division, GST math, messy print).

## Done when
- [ ] Uses `float` price and `int` qty
- [ ] Total = price × qty × (1 + 5% GST), rounded to 2 decimals
- [ ] Prints with f-string like `Total: ₹105.00`

**Stretch (after Flow Control):** reject bad input with `if` / re-ask with `while`.

**Sessions:** ~06–10
