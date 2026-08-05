# Optional Enrichment: Professional Python Design Choices

> **Not a standard teaching module.** Skip for Django path. Use after S45, Saturday enrichment, or interview prep only.  
> Does **not** follow full Classroom Ticket / Try these / Assessment shape — see [Writing Standard](../14_Trainer_Only/10_Module_Writing_Standard.md) for required modules.

**Duration:** Optional — Session Calendar lists this as enrichment, not a numbered live focus.  
**Previous:** [File Handling & Logging](05_File_Handling_and_Logging.md) (finish core Advanced first)  
**Next:** Continue calendar — [Git & GitHub](../04_Git_GitHub/01_Git_and_GitHub.md) or MySQL phase as scheduled

## Learning outcomes

By the end, learners can:

- Choose composition or inheritance for a small business feature.
- Use an abstract base class when a shared contract adds clarity.
- Explain `__str__` and `__repr__` through a useful debugging example.
- Avoid mutable default argument bugs.
- Write focused custom exceptions and preserve useful error context.
- Explain a package entry point using `if __name__ == "__main__"`.

## Classroom Ticket (optional)

Reuse kits you already know — this file is a **code-review / refactor** session:

- [17_bank_account_oop](../15_Lab_Assets/17_bank_account_oop/)
- [18_safe_input_exceptions](../15_Lab_Assets/18_safe_input_exceptions/)
- [30_ksr_utils_toolkit](../15_Lab_Assets/30_ksr_utils_toolkit/)

## 1. Function design: avoid the mutable default trap

This is more useful in real projects than memorising many argument varieties.

```python
# Wrong: the same list is reused between calls.
def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

# Correct: create a fresh list when no list was supplied.
def add_skill(skill, skills=None):
    if skills is None:
        skills = []
    skills.append(skill)
    return skills

print(add_skill("Python"))  # ['Python']
print(add_skill("SQL"))     # ['SQL'], not ['Python', 'SQL']
```

**Interview explanation:** Default argument values are evaluated once when the function is defined. A mutable default can therefore leak state into later calls.

**Try these (2 programs):**

**Program 1 — Prove the bug**

```python
def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

print(add_skill("Python"))
print(add_skill("SQL"))  # leaks prior call
```

**Program 2 — Fix with None**

```python
def add_skill(skill, skills=None):
    if skills is None:
        skills = []
    skills.append(skill)
    return skills

print(add_skill("Python"))
print(add_skill("SQL"))
```

## 2. Composition before inheritance

Use inheritance only when the child genuinely **is a** specialised version of the parent. Use composition when an object **has a** collaborator.

```python
class EmailNotifier:
    def send(self, message):
        print(f"EMAIL: {message}")

class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier  # OrderService HAS-A notifier

    def place_order(self, order_id):
        self.notifier.send(f"Order {order_id} placed")

service = OrderService(EmailNotifier())
service.place_order("ORD-101")
```

`OrderService` is not an `EmailNotifier`; it uses one. This design is easier to change later—for example, to SMS or WhatsApp notifications.

**Try these (2 programs):**

**Program 1 — SMS notifier composition**

```python
class SmsNotifier:
    def send(self, message):
        print(f"SMS: {message}")

class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier

    def place_order(self, order_id):
        self.notifier.send(f"Order {order_id} placed")

OrderService(SmsNotifier()).place_order("ORD-202")
```

**Program 2 — Swap notifier at runtime**

```python
class EmailNotifier:
    def send(self, message):
        print(f"EMAIL: {message}")

class OrderService:
    def __init__(self, notifier):
        self.notifier = notifier

    def place_order(self, order_id):
        self.notifier.send(f"Order {order_id} placed")

svc = OrderService(EmailNotifier())
svc.place_order("ORD-1")
svc.notifier = type("N", (), {"send": staticmethod(lambda m: print("LOG:", m))})()
svc.place_order("ORD-2")
```

## 3. Abstract base classes: a small, useful contract

Use an abstract base class only when multiple implementations must offer the same behaviour.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        """Return a payment result for the requested amount."""

class DemoGateway(PaymentGateway):
    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return {"status": "success", "amount": amount}

print(DemoGateway().pay(499))
```

## 4. `__str__` vs `__repr__`

```python
class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₹{self.price})"

    def __repr__(self):
        return f"Product({self.sku!r}, {self.name!r}, {self.price!r})"

p = Product("P1", "Mouse", 799)
print(str(p))
print(repr(p))
```

## 5. Custom exceptions with context

```python
class InsufficientStockError(Exception):
    def __init__(self, sku, requested, available):
        self.sku = sku
        self.requested = requested
        self.available = available
        super().__init__(
            f"{sku}: need {requested}, only {available} left"
        )

try:
    raise InsufficientStockError("P1", 5, 2)
except InsufficientStockError as e:
    print(e)
```

## Mini-Project: Stock reserve + notify

**Business request:** A shop needs to reserve stock and notify a customer after an order is accepted.

**Must build**

- `Product` with name, price, and stock.
- `reserve(quantity)` that rejects invalid or unavailable quantities.
- `InsufficientStockError` with a clear message.
- `ConsoleNotifier` used through composition by `OrderService`.
- `__str__` or `__repr__` useful during debugging.

### Done when

- [ ] Reserve two units from stock five; remaining stock is three  
- [ ] Reserve more than stock; clear message; stock unchanged  
- [ ] Reserve zero or negative; rejected  
- [ ] Run file directly; import without auto-placing an order  

### Stretch

- Add a `PaymentGateway` abstract base class and a `DemoGateway` implementation.
- Write two unit tests for `reserve` (kit [26_unittest_utils](../15_Lab_Assets/26_unittest_utils/) ideas).

## Revision Map — Memorize / Understand / Practise / Build

| Label | Focus |
|-------|--------|
| **Memorize** | Mutable default trap; `ABC` + `@abstractmethod`; `__str__` vs `__repr__` |
| **Understand** | Composition HAS-A vs inheritance IS-A |
| **Practise** | Refactor a long if/elif notifier into composition |
| **Build** | Stock reserve mini-project above |

## How to run this session

Show a long `if/elif` program first, then ask what breaks when the business adds a second payment method or notification channel — then refactor toward composition.
