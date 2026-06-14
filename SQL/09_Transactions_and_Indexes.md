# Transactions and Indexes

## Transactions

A transaction is a logical group of one or more SQL statements. Transactions are used in various scenarios such as banking, ecommerce, social networks, booking tickets, etc.

A transaction has four important properties:

1. Atomicity
2. Consistency
3. Isolation
4. Durability

## Atomicity

Either all SQL statements or none are applied to database.

```
✓ Transaction: Debit ✓ → Credit ✓ → ...  (all succeed)
✗ Transaction: Debit ✓ → Credit ✗ → ...  (rollback all)
```

## Consistency

Transactions always leave the database in a consistent state.

**Example:** Transfer of funds between Sam and David.

| State | Sam | David | Total |
|-------|-----|-------|-------|
| Before | 10,000 | 5,000 | 15,000 |
| Success | 9,000 | 6,000 | 15,000 |
| Failure | 10,000 | 5,000 | 15,000 |

## Isolation

Multiple transactions can occur at the same time without adversely affecting the other.

**Example:** Concurrent operations on Sam's account:

- Starting balance: **10,000**
- Operations: Debit 1k, Credit 25k, Debit 9k
- Final balance: **25,000** (correct outcome when transactions are isolated)

## Durability

Changes of a successful transaction persist even after a system crash.

**Example:** David's balance is **10,000**. A successful transaction credits **5,000**, bringing the balance to **15,000**. Even if a system failure occurs afterward, the balance remains **15,000**.

These four properties are commonly acronymed **ACID**:

- **A**tomicity
- **C**onsistency
- **I**solation
- **D**urability

## Indexes

In scenarios like searching for a word in a dictionary, we use an index to easily search for the word. Similarly, in databases, we maintain indexes to speed up the search for data in a table.

**Dictionary Index Example:**

| Section | Range | Page |
|---------|-------|------|
| A | ab... – az... | 02 – 23 |
| B | ba... – bz... | 24 – 32 |
| C | ca... – cz... | 33 – 43 |
