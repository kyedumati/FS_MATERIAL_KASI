# Ticket: HDFC Bank BankAccount Class

**Customer:** HDFC Bank campus branch  
**Need:** `BankAccount` with deposit / withdraw; balance **not** settable from outside.

**Teaching-order:** Classes, constructors, `this`, `private` + getters, instance methods. Validate with `print` + `return` — **no `throw` / `try` / `catch`**. **No `extends`** (inheritance is the next part). No `ArrayList`. No Lombok.

## Starter
Fill `deposit`, `withdraw`, and `getBalance` in `starter/BankAccount.java`. Keep `balance` **private**.

## Broken
Public `balance` and unguarded withdraw in `broken/`. Anyone can set `-99999`.

## Done when
- [ ] `balance` is `private` (no assignment from `main`)
- [ ] Deposit / withdraw reject `amount <= 0` with a message
- [ ] Overdraft prints a message and leaves balance unchanged
- [ ] `getBalance()` / `getHolder()` work; there is **no** `setBalance`
- [ ] `main` constructs one account, deposits, withdraws, and prints the balance
