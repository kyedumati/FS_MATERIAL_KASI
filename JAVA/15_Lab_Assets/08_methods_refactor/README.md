# Ticket: Refactor HDFC Bank ATM Into Methods

**Customer:** HDFC Bank tech lead  
**Need:** Same ATM behaviour, but logic in **static methods** (no giant `main`).

**Teaching-order:** One class. Static methods + `return`. Validate with `print` + `return` — **no `throw`**. No `new` account object.

## Starter
Fill `deposit`, `withdraw`, `showMenu` in starter.

## Broken
Ignored return value / overdraft still subtracts in `broken/`.

## Done when
- [ ] Deposit / withdraw logic lives in methods (not a giant `main`)
- [ ] Bad amount or overdraft prints a message and leaves balance unchanged
- [ ] Menu repeats until Quit
