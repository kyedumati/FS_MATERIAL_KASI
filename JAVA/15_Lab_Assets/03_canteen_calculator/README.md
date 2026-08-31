# Ticket: TechMart Canteen Calculator

**Customer:** TechMart canteen counter (CampusCart stall)  
**Need:** Staff still use paper for `price × qty + GST`. Build a CLI calculator.

**Teaching-order:** Linear `main` only — no `if` / `while` / `for` / extra methods.

## Starter
Open `starter/CanteenCalculator.java` — one price, one qty, print GST total.

## Broken
`broken/CanteenCalculator.java` has bugs (integer division, GST math, messy print).

## Done when
- [ ] Uses `double` price and `int` qty
- [ ] Total = price × qty × (1 + 5% GST), two decimals
- [ ] Prints like `Total: ₹105.00`

**Stretch (after Flow Control):** reject bad input with `if` / re-ask with `while`.
