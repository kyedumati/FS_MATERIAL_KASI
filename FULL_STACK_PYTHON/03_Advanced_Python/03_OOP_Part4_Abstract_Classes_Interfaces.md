# Module 03d — OOP Part 4: Abstract Classes, Abstract Methods & Interfaces

**Phase:** Advanced Python

**Previous module:** [OOP Part 3 — Polymorphism & Project](03_OOP_Part3_Polymorphism_Project.md)  
**Next module:** [Exception Handling](04_Exception_Handling.md)

**Series:** [OOP overview](03_OOP.md) · [Part 1](03_OOP_Part1_Classes_Encapsulation.md) · [Part 2](03_OOP_Part2_Inheritance.md) · [Part 3](03_OOP_Part3_Polymorphism_Project.md) · Part 4 (this file)

**Lab kit:** [15_Lab_Assets/32_campus_wallet_abc/](../15_Lab_Assets/32_campus_wallet_abc/)

---

## 1. Abstract method

**Real-world analogy:** A **job posting** says “must be able to treat patients.” It does not write the treatment. Each hired doctor fills that in — cardiology vs paediatrics. An **abstract method** is that must-have skill with **no recipe yet** (`pass`). **SecureBank** declares `kind()` before savings or wallet exists. **AcmeHR** declares `net()` before intern vs faculty. **TechMart** declares `pay()` before UPI vs card.

**Icons:** Bank · Employee · Order

**Where used?** **SecureBank** does not know `kind()` until savings or wallet exists. **AcmeHR** does not know `net()` until intern vs faculty. **TechMart** does not know `pay()` until UPI vs card.

**Definition:** Sometimes we don't know the implementation yet, but we still want to declare the method. Such a method is an **abstract method**. It has only a **declaration**, not the real code.

**Purpose:** The parent says “every child must have this method.” The child writes the actual body.

In Python we declare it with the `@abstractmethod` decorator:

```python
@abstractmethod
def m1(self):
    pass
```

`pass` means “no algorithm yet.” It does **not** mean the method does nothing useful forever.

`@abstractmethod` lives in the `abc` module (`abc` = abstract base class). We must import it. If we forget the import, Python does not know the name.

**Case — forgot the import:**

```python
class Test:
    @abstractmethod
    def m1(self):
        pass
```

**Expected Output:**

```
NameError: name 'abstractmethod' is not defined
```

Correct import:

```python
from abc import ABC, abstractmethod


class Test:
    @abstractmethod
    def m1(self):
        pass
```

This file now runs. Creating `Test()` is a **different** question — that is the abstract **class** topic next.

Child classes are responsible for providing the implementation of the parent’s abstract methods.

**Remember:** Abstract method = “I know the name. I do not know the body yet.”

**Common Error:** writing a fake body like `return "account"` and skipping `@abstractmethod`. Then a child can forget to override, and the fake value ships.

**Note:**

- Do not use `raise NotImplementedError` this week. Exceptions come next. Use `@abstractmethod` + `pass`.
- Import from `abc`. `from abc import *` works in old notes; we import the two names we need.

**Try these (3 project examples):**

**Program 1 — AcmeHR job role:** `net_pay()` **declared, body later**

```python
from abc import ABC, abstractmethod


class JobRole:
    @abstractmethod
    def net_pay(self):
        pass


print("JobRole created. Intern and Faculty will write net_pay().")
```

**Expected Output:**

```
JobRole created. Intern and Faculty will write net_pay().
```

**Program 2 — SecureBank children fill** `kind()`

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder):
        self.holder = holder

    @abstractmethod
    def kind(self):
        pass


class SavingsAccount(Account):
    def kind(self):
        return "savings"


class WalletAccount(Account):
    def kind(self):
        return "wallet"


print(SavingsAccount("Priya").kind())
print(WalletAccount("Ravi").kind())
```

**Expected Output:**

```
savings
wallet
```

**Program 3 — TechMart children fill** `pay()`

```python
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        return f"UPI ₹{amount}"


class CardPayment(Payment):
    def pay(self, amount):
        return f"Card ₹{amount}"


print(UpiPayment().pay(250))
print(CardPayment().pay(999))
```

**Expected Output:**

```
UPI ₹250
Card ₹999
```

---



## 2. Abstract class

**Real-world analogy:** An **incomplete house plan**. Rooms are named. The kitchen is not drawn. You cannot *live* in the plan — you can only live in a finished house. The plan still shares plumbing rules (deposit, holder, header). Children finish the missing room (`kind()`, `title()`, `no_of_wheels()`). **SecureBank** `Account` is that plan. **MedCare** `Report` is that plan. Walk the `Test` cases below the way the classic notes do — then the project programs show the same rule in a product.

**Icons:** Bank · Employee · Laptop

**Where used?** **SecureBank** `Account` (savings vs wallet), **MedCare** `Report` (lab vs invoice), vehicle types (`no_of_wheels`).

**Definition:** Sometimes the implementation of a class is **not complete**. Such a partially implemented class is an **abstract class**.

**Purpose:** Share the parts we already know (`deposit`, holder, balance) and force children to finish the missing part (`kind()`, `no_of_wheels()`).

Every abstract class in Python should extend `ABC`, which is also in the `abc` module.

Whether we can create an object depends on **two** things together: did we extend `ABC`, and does the class contain at least one `@abstractmethod`? Walk the cases in order.

### Case-1 — Normal class, no abstract method

```python
from abc import ABC, abstractmethod


class Test:
    pass


t = Test()
print("object created")
```

**Expected Output:**

```
object created
```

We can create an object. `Test` is a **concrete** class. It does not contain any abstract method.

### Case-2 — Extends `ABC`, but no abstract method

```python
from abc import ABC, abstractmethod


class Test(ABC):
    pass


t = Test()
print("object created")
```

**Expected Output:**

```
object created
```

We can still create an object. Extending `ABC` alone is not enough. There is no abstract method, so Python treats it as complete.

### Case-3 — Extends `ABC` **and** has an abstract method

```python
from abc import ABC, abstractmethod


class Test(ABC):
    @abstractmethod
    def m1(self):
        pass


t = Test()
```

**Expected Output:**

```
TypeError: Can't instantiate abstract class Test ... m1
```

(The exact wording changes slightly by Python version. The idea is the same: instantiation is not possible.)

### Case-4 — Abstract method, but does **not** extend `ABC`

```python
from abc import ABC, abstractmethod


class Test:
    @abstractmethod
    def m1(self):
        pass


t = Test()
print("object created")
```

**Expected Output:**

```
object created
```

We can create an object even though the class contains an abstract method, because we did **not** extend `ABC`. The decorator is then only documentation. It does not block `Test()`.

### Case-5 — Abstract method with a real body, still not extending `ABC`

```python
from abc import ABC, abstractmethod


class Test:
    @abstractmethod
    def m1(self):
        print("Hello")


t = Test()
t.m1()
```

**Expected Output:**

```
Hello
```

Without `ABC`, `@abstractmethod` does not stop construction. The method runs like a normal method.

**Conclusion:** If a class contains **at least one abstract method** **and** we are extending `ABC`, instantiation is not possible.

**Remember:** abstract class + abstract method → instantiation is not possible.

Parent abstract methods should be implemented in the child classes. Otherwise we cannot instantiate the **child** either. If we never create the child object, we will not see the error.

**Child Case-1 — class is incomplete, but we never construct it:**

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass


class Bus(Vehicle):
    pass


print("Bus class exists. No object yet — no error.")
```

**Expected Output:**

```
Bus class exists. No object yet — no error.
```

This is valid, because we did not create a `Bus` object.

**Child Case-2 — same** `Bus`**, now we construct it:**

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass


class Bus(Vehicle):
    pass


b = Bus()
```

**Expected Output:**

```
TypeError: Can't instantiate abstract class Bus ... no_of_wheels
```

**Note:** If we extend an abstract class and do not override its abstract method, the **child is also abstract**. Instantiation is not possible.

When children **do** implement the method:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self):
        pass


class Bus(Vehicle):
    def no_of_wheels(self):
        return 6


class Auto(Vehicle):
    def no_of_wheels(self):
        return 3


b = Bus()
a = Auto()
print(b.no_of_wheels())
print(a.no_of_wheels())
```

**Expected Output:**

```
6
3
```

**Note:** An abstract class can contain **both** abstract and non-abstract (normal) methods. The normal methods are the shared implementation. The abstract methods are the holes.

```mermaid
classDiagram
  class Vehicle {
    <<ABC>>
    +no_of_wheels()*
  }
  class Bus {
    +no_of_wheels()
  }
  class Auto {
    +no_of_wheels()
  }
  Vehicle <|-- Bus
  Vehicle <|-- Auto
```



**Key takeaways:**

- `ABC` alone does not block objects
- `@abstractmethod` alone does not block objects
- **Both together** block objects
- A child that skips the abstract method is still abstract

**Interview:** Can an abstract class have a constructor? **Yes.** `__init__` runs when we construct the **child**, via `super()`. We never construct the abstract parent.

**Common Error:** `class Account(ABC):` with no `@abstractmethod`. Then `Account("Campus")` still works — Case-2.

**Try these (3 project examples):**

**Program 1 — Shared** `deposit`**, abstract** `kind()` **(SecureBank)**

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder, balance=0):
        self.holder = holder
        self._balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self._balance += amount

    def get_balance(self):
        return self._balance

    @abstractmethod
    def kind(self):
        pass


class SavingsAccount(Account):
    def kind(self):
        return "savings"


acct = SavingsAccount("Priya", 1000)
acct.deposit(200)
print(acct.kind(), acct.holder, int(acct.get_balance()))
# Account("Campus", 0)  # TypeError — Case-3
```

**Expected Output:**

```
savings Priya 1200
```

**Program 2 — MedCare abstract report + shared header**

```python
from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, patient):
        self.patient = patient

    def header(self):
        return "MedCare | " + self.patient

    @abstractmethod
    def title(self):
        pass


class LabReport(Report):
    def title(self):
        return "Blood test"


class InvoiceReport(Report):
    def title(self):
        return "Pharmacy bill"


lab = LabReport("Anita")
inv = InvoiceReport("Ravi")
print(lab.header(), "-", lab.title())
print(inv.header(), "-", inv.title())
```

**Expected Output:**

```
MedCare | Anita - Blood test
MedCare | Ravi - Pharmacy bill
```

**Program 3 — TechMart abstract shipment + shared tracking id**

```python
from abc import ABC, abstractmethod


class Shipment(ABC):
    def __init__(self, order_id):
        self.order_id = order_id

    def tracking(self):
        return "TRK-" + self.order_id

    @abstractmethod
    def eta_days(self):
        pass


class StandardShip(Shipment):
    def eta_days(self):
        return 5


class ExpressShip(Shipment):
    def eta_days(self):
        return 1


s = StandardShip("101")
e = ExpressShip("102")
print(s.tracking(), "ETA", s.eta_days(), "days")
print(e.tracking(), "ETA", e.eta_days(), "days")
```

**Expected Output:**

```
TRK-101 ETA 5 days
TRK-102 ETA 1 days
```

---



## 3. Interface in Python

**Real-world analogy:** A **wall socket**. Any appliance with the same pins works — fan, charger, induction stove. The socket does not know *how* the appliance uses power. An **interface** is that socket: only method names (`connect`, `pay`, `send`), no business body. **SecureBank** swaps MySQL vs Postgres behind `DBInterface`. **TechMart** swaps UPI vs card behind `Payable`. **MedCare** swaps SMS vs email behind `Notifier`. Python has no `interface` keyword — we simulate it with `ABC` + only abstract methods.

**Icons:** Bank · UPI · Order

**Where used?** Database drivers (**MySQL** vs **Postgres**), **TechMart** pay methods (UPI vs card), printers (EPSON vs HP). Same method names, different products.

**Definition:** In general, if an abstract class contains **only abstract methods**, we consider that abstract class an **interface**.

Python has **no** `interface` keyword (Java does). We still use the word in interviews: “interface” means **requirement only** — we know *what* must exist (`connect`, `pay`), we do not know *how* yet.

**Purpose:** Write business code against the contract. Swap the real class later (MySQL today, Postgres tomorrow) without rewriting the caller.

**Demo — pick the database engine at runtime:**

```python
from abc import ABC, abstractmethod


class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class MySQL(DBInterface):
    def connect(self):
        print("Connecting to MySQL...")

    def disconnect(self):
        print("Disconnecting MySQL...")


class Postgres(DBInterface):
    def connect(self):
        print("Connecting to Postgres...")

    def disconnect(self):
        print("Disconnecting Postgres...")


engines = {"MySQL": MySQL, "Postgres": Postgres}
name = "MySQL"            # later this can come from input() or a config file
db = engines[name]()
db.connect()
db.disconnect()
```

**Expected Output:**

```
Connecting to MySQL...
Disconnecting MySQL...
```

Change `name = "Postgres"` and the **same** `db.connect()` / `db.disconnect()` lines talk to a different engine. That is the point of an interface.

**Later — Files week:** the old notes read the class name from `config.txt`. Same idea — do not use `open` until that module.

**Demo — TechMart checkout against** `Payable`**:**

```python
from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Upi(Payable):
    def pay(self, amount):
        print("UPI paid ₹" + str(int(amount)))
        return True


class CardPay(Payable):
    def pay(self, amount):
        if amount > 50000:
            print("Card limit exceeded")
            return False
        print("Card paid ₹" + str(int(amount)))
        return True


def checkout(method, amount):
    ok = method.pay(amount)
    print("ok?", ok)


checkout(Upi(), 250)
checkout(CardPay(), 999)
checkout(CardPay(), 60000)
```

**Expected Output:**

```
UPI paid ₹250
ok? True
Card paid ₹999
ok? True
Card limit exceeded
ok? False
```

A class may take **two** interface-style parents (Python already allows multiple inheritance from Part 2):

```python
class WalletAccount(Account, Payable):
    def kind(self):
        return "wallet"

    def pay(self, amount):
        ...
```

Savings **is an** account. A wallet **can** pay. Do not put `pay` on `Account`, or every savings account is forced to fake a payment.

**Interview:** `typing.Protocol` is another way to describe an interface **without** inheriting `ABC` (“if it has `pay`, it counts”). Classroom labs use `ABC`. Protocol is the interview name for a structural interface.

**Remember:** Interface = only abstract methods = specification. The child writes the service.

**Common Error:** storing `holder` / `_balance` on `Payable`. That is account **state**. Keep state on the abstract **class** `Account`. Keep `Payable` as methods only.

**Note:**

- Duck typing (Part 3) is an **informal** interface. ABC makes a missing method fail when we **construct** the object, not later in a loop.
- Wrong: `DBInterface()` — that is Case-3. Construct `MySQL()` or `Postgres()`.

**Try these (3 project examples):**

**Program 1 —** `Notifier` **interface, SMS vs email**

```python
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, msg):
        pass


class Sms(Notifier):
    def send(self, msg):
        print("SMS:", msg)


class Email(Notifier):
    def send(self, msg):
        print("EMAIL:", msg)


for n in (Sms(), Email()):
    n.send("Order shipped")
```

**Expected Output:**

```
SMS: Order shipped
EMAIL: Order shipped
```

**Program 2 — Two contracts on one wallet**

```python
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_slip(self):
        pass


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CampusWallet(Printable, Payable):
    def __init__(self, holder, balance):
        self.holder = holder
        self._balance = balance

    def print_slip(self):
        print(self.holder, "₹" + str(int(self._balance)))

    def pay(self, amount):
        if amount <= 0 or amount > self._balance:
            print("pay failed")
            return False
        self._balance -= amount
        print("paid ₹" + str(int(amount)))
        return True


w = CampusWallet("Ravi", 500)
w.print_slip()
w.pay(120)
w.print_slip()
```

**Expected Output:**

```
Ravi ₹500
paid ₹120
Ravi ₹380
```

**Program 3 — TechMart** `PaymentGateway` **interface (UPI vs card)**

```python
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, amount):
        pass


class UpiGateway(PaymentGateway):
    def charge(self, amount):
        print("UPI charged ₹" + str(amount))


class CardGateway(PaymentGateway):
    def charge(self, amount):
        print("Card charged ₹" + str(amount))


for g in (UpiGateway(), CardGateway()):
    g.charge(199)
```

**Expected Output:**

```
UPI charged ₹199
Card charged ₹199
```

---



## 4. Concrete class vs abstract class vs interface

**Real-world analogy:** Three documents on a campus project. The **requirement PDF** lists steps only (`register`, `verify_kyc`, `activate`) — **interface**. The **half-built floor** already has wiring and plumbing, but the shop shutter is not fitted — **abstract class**. The **open canteen** is ready to serve — **concrete class**. **SecureBank** `Payable` is the PDF. `Account` (deposit + hole `kind`) is the half-built floor. `SavingsAccount` is the open branch. **AcmeHR** onboarding uses the same three layers.

**Icons:** Bank · Employee · UPI

**Where used?** Every interview: “When interface, when abstract class?” **SecureBank** `Payable` vs `Account` is the stock example.

Do not memorise a big table first. Use this three-line rule:

1. If we don't know **anything** about implementation — we only have the requirement — go for an **interface**.
2. If we are talking about implementation, but **not completely** — go for an **abstract class** (partially implemented class).
3. If we are talking about implementation **completely** and we are ready to provide the service — go for a **concrete class**.


|              | Interface                          | Abstract class                                   | Concrete class                                 |
| ------------ | ---------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
| What we know | Only method names                  | Some real code + some holes                      | Full service                                   |
| Python       | `ABC` + **only** `@abstractmethod` | `ABC` + mix of real methods and abstract methods | Normal class (or child that filled every hole) |
| Construct?   | No                                 | No                                               | Yes                                            |
| Example      | `Payable`, `DBInterface`           | `Account` with `deposit` + abstract `kind`       | `SavingsAccount`, `MySQL`                      |


**Remember:** specification → interface. Partial code → abstract class. Ready to use → concrete class.

The three layers can sit in a chain. The top class is only requirements. The middle class implements some methods. The bottom class finishes the last method — only then can we create an object.

```python
from abc import ABC, abstractmethod


class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    @abstractmethod
    def m3(self):
        pass


class AbsCls(CollegeAutomation):
    def m1(self):
        print("m1 method implementation")

    def m2(self):
        print("m2 method implementation")


class ConcreteCls(AbsCls):
    def m3(self):
        print("m3 method implementation")


c = ConcreteCls()
c.m1()
c.m2()
c.m3()
```

**Expected Output:**

```
m1 method implementation
m2 method implementation
m3 method implementation
```

`CollegeAutomation` is an interface (only abstract methods). `AbsCls` is still abstract (`m3` missing). `ConcreteCls` is complete — now `ConcreteCls()` is legal.

Same pattern in a job story: **AcmeHR** onboarding.

- Interface: `register`, `verify_kyc`, `activate` — we only know the steps.
- Abstract class: `register` and `verify_kyc` are written; `activate` is still different for intern vs faculty.
- Concrete class: intern activation vs faculty activation.

**Interview:** Why not put `pay` on abstract `Account`? Because we are **not** talking about payment for every account. Savings may only deposit / withdraw / add interest. `Payable` is the requirement for types that **can** pay.

**Common Error:** calling `ABC` “Python’s interface keyword.” `ABC` is the abstract-class tool. Using it with **only** abstract methods is how we **simulate** an interface.

**Try these (3 project examples):**

**Program 1 — Keep** `pay` **off** `Account`**; only wallet is** `Payable`

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder, balance):
        self.holder = holder
        self._balance = float(balance)

    def get_balance(self):
        return self._balance

    @abstractmethod
    def kind(self):
        pass


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class SavingsAccount(Account):
    def kind(self):
        return "savings"


class WalletAccount(Account, Payable):
    def kind(self):
        return "wallet"

    def pay(self, amount):
        print(self.kind(), "pays ₹" + str(int(amount)))
        return True


print(SavingsAccount("Priya", 1000).kind())
WalletAccount("Ravi", 500).pay(50)
```

**Expected Output:**

```
savings
wallet pays ₹50
```

**Program 2 — One loop; pay only if** `Payable`

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder):
        self.holder = holder

    @abstractmethod
    def kind(self):
        pass


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class SavingsAccount(Account):
    def kind(self):
        return "savings"


class WalletAccount(Account, Payable):
    def kind(self):
        return "wallet"

    def pay(self, amount):
        print("pay ₹" + str(int(amount)), "from", self.holder)
        return True


accounts = [SavingsAccount("Priya"), WalletAccount("Ravi")]
for a in accounts:
    print(a.kind(), a.holder)
    if isinstance(a, Payable):
        a.pay(80)
```

**Expected Output:**

```
savings Priya
wallet Ravi
pay ₹80 from Ravi
```

**Program 3 — AcmeHR: interface + abstract class + concrete intern**

```python
from abc import ABC, abstractmethod


class Onboarding(ABC):           # interface — steps only
    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def activate(self):
        pass


class StaffOnboarding(Onboarding):  # abstract — register done, activate open
    def __init__(self, name):
        self.name = name

    def register(self):
        print("KYC done for", self.name)


class InternOnboarding(StaffOnboarding):  # concrete
    def activate(self):
        print(self.name, "activated as intern")


intern = InternOnboarding("Anita")
intern.register()
intern.activate()
```

**Expected Output:**

```
KYC done for Anita
Anita activated as intern
```

---



## Step-by-Step: SecureBank campus wallet

**Icons:** Bank · UPI · Order

**Where used?** Same ticket as the [lab kit](../15_Lab_Assets/32_campus_wallet_abc/).

`Account` is an **abstract class** (shared deposit / withdraw + hole `kind()`). `Payable` is an **interface** (only `pay`). `SavingsAccount` and `WalletAccount` are **concrete**.

### Step 1 — Abstract `Account`

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder, opening):
        self.holder = holder
        self._balance = float(opening)

    def deposit(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        if amount > self._balance:
            print("insufficient funds")
            return
        self._balance -= amount

    def get_balance(self):
        return self._balance

    @abstractmethod
    def kind(self):
        pass

    def print_slip(self):
        print(self.kind(), "|", self.holder, "₹" + str(int(self._balance)))
```



### Step 2 — Interface `Payable` and two concrete children

```python
class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class SavingsAccount(Account):
    def __init__(self, holder, opening, rate=0.04):
        super().__init__(holder, opening)
        self.rate = rate

    def kind(self):
        return "savings"

    def add_interest(self):
        self.deposit(self.get_balance() * self.rate)


class WalletAccount(Account, Payable):
    def kind(self):
        return "wallet"

    def pay(self, amount):
        before = self.get_balance()
        self.withdraw(amount)
        if self.get_balance() == before:
            return False
        print("Paid ₹" + str(int(amount)), "from wallet")
        return True
```



### Step 3 — One loop

```python
accounts = [
    SavingsAccount("Priya", 1000, 0.04),
    WalletAccount("Ravi", 500),
]
for a in accounts:
    a.print_slip()

ok = accounts[1].pay(120)
print("pay ok?", ok)
accounts[1].print_slip()

accounts[0].add_interest()
accounts[0].print_slip()
```

**Expected Output:**

```
savings | Priya ₹1000
wallet | Ravi ₹500
Paid ₹120 from wallet
pay ok? True
wallet | Ravi ₹380
savings | Priya ₹1040
```

**Note:** Do not write `if a.kind() == "wallet"` to call `pay`. Use `isinstance(a, Payable)` or hold the wallet as `Payable`. `print_slip` is a **normal** method on the abstract class — that is why `Account` is not an interface.

**Try these (3 project examples):**

**Program 1 — Two slips through the parent type**

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder, opening):
        self.holder = holder
        self._balance = float(opening)

    @abstractmethod
    def kind(self):
        pass

    def print_slip(self):
        print(self.kind(), "|", self.holder, "₹" + str(int(self._balance)))


class SavingsAccount(Account):
    def kind(self):
        return "savings"


class WalletAccount(Account):
    def kind(self):
        return "wallet"


for a in (SavingsAccount("Priya", 1000), WalletAccount("Ravi", 500)):
    a.print_slip()
```

**Expected Output:**

```
savings | Priya ₹1000
wallet | Ravi ₹500
```

**Program 2 — Wallet pay rejected (print + return)**

```python
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder, opening):
        self.holder = holder
        self._balance = float(opening)

    def withdraw(self, amount):
        if amount <= 0:
            print("amount must be positive")
            return
        if amount > self._balance:
            print("insufficient funds")
            return
        self._balance -= amount

    def get_balance(self):
        return self._balance

    @abstractmethod
    def kind(self):
        pass


class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class WalletAccount(Account, Payable):
    def kind(self):
        return "wallet"

    def pay(self, amount):
        before = self.get_balance()
        self.withdraw(amount)
        if self.get_balance() == before:
            return False
        print("Paid ₹" + str(int(amount)))
        return True


w = WalletAccount("Ravi", 50)
print("ok?", w.pay(120))
print("balance", int(w.get_balance()))
```

**Expected Output:**

```
insufficient funds
ok? False
balance 50
```

**Program 3 — MedCare lab vs invoice through one report list**

```python
from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, patient):
        self.patient = patient

    @abstractmethod
    def title(self):
        pass

    def print_slip(self):
        print(self.title(), "|", self.patient)


class LabReport(Report):
    def title(self):
        return "Lab"


class InvoiceReport(Report):
    def title(self):
        return "Invoice"


for r in (LabReport("Anita"), InvoiceReport("Ravi")):
    r.print_slip()
```

**Expected Output:**

```
Lab | Anita
Invoice | Ravi
```

---



## Practice Exercises



### Basic

1. What is an abstract method in one or two sentences?
  **Model answer:**  
   A method we declare even though we do not know the implementation yet. In Python: `@abstractmethod` with `pass`. Child classes write the real body.
2. Why do we import from `abc`? What error do we get if we skip it?
  **Model answer:**  
   `@abstractmethod` and `ABC` live in the `abc` module. Skip the import → `NameError: name 'abstractmethod' is not defined`.
3. Write the conclusion of Cases 1–5 in one line.
  **Model answer:**  
   If a class contains at least one abstract method **and** extends `ABC`, instantiation is not possible.



### Intermediate

1. `class Bus(Vehicle): pass` when `Vehicle` is `ABC` with abstract `no_of_wheels`. Is the `class` line legal? Is `Bus()` legal?
  **Model answer:**  
   The class line is legal. `Bus()` is not — `Bus` did not override `no_of_wheels`, so it is still abstract (`TypeError`).
2. Create abstract `Shape` with `area()`, `Circle(r)` using `3.14 * r * r`, `Rect(w, h)` as `w * h`. Print both areas as integers.
  **Model answer:**

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


print(int(Circle(2).area()))
print(int(Rect(3, 4).area()))
```

**Expected Output:**

```
12
12
```

1. When do we pick interface vs abstract class vs concrete class?
  **Model answer:**  
   Interface: we know only the requirement (`connect` / `pay`). Abstract class: we have some real code and some holes (`deposit` written, `kind` missing). Concrete class: implementation is complete and we can create objects (`MySQL()`, `SavingsAccount(...)`).



### Interview

1. What is an interface in Python? Is there an `interface` keyword?
  **Model answer:**  
   No keyword. An abstract class that contains **only** abstract methods is treated as an interface. Children provide every method. `typing.Protocol` is the structural interview alternative; labs use `ABC`.
2. Why can we create an object of a class that has `@abstractmethod` but does **not** extend `ABC`?
  **Model answer:**  
   Case-4. The decorator only blocks construction when the class also extends `ABC`. Without `ABC`, it is a normal class.
3. Duck typing vs ABC — what extra do we get from `@abstractmethod`?
  **Model answer:**  
   Duck typing fails when we **call** a missing method. An ABC fails when we **construct** an incomplete child. Named contracts also let us write `isinstance(x, Payable)`.

---



## Mini-Project (Assignment): SecureBank Campus Wallet

**Lab kit:** [15_Lab_Assets/32_campus_wallet_abc/](../15_Lab_Assets/32_campus_wallet_abc/)

**Business request:** SecureBank campus desk needs savings and wallet on one slip loop. Wallet can **pay**. A generic `Account(...)` must not be allowed.

### What to build


| Piece            | Detail                                                                                                    |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| `Account(ABC)`   | abstract class: holder, balance, `deposit` / `withdraw` / `get_balance` / `print_slip`; abstract `kind()` |
| `Payable`        | interface: only `pay(amount)`                                                                             |
| `SavingsAccount` | concrete; `kind()` → `"savings"`; `add_interest()`                                                        |
| `WalletAccount`  | concrete; `Account` **and** `Payable`; `pay` uses `withdraw` (print + return)                             |
| Demo             | list of accounts; print slips; pay from wallet; add interest on savings                                   |


---



## Interview Q&A

Shared with students after concepts and the mini-project. Use for review and interview prep — questions and model answers are included.

**Q1. What is an abstract method?**  
**A:** A method with declaration only, no real implementation. Python: `@abstractmethod` and `pass`. Child classes write the body.

**Q2. What is an abstract class? Can we instantiate it?**  
**A:** A partially implemented class. Extend `ABC` and include at least one abstract method. Then we cannot create an object (`TypeError`). Construct the concrete child instead.

**Q3. Extending** `ABC` **with no abstract method — can we create an object?**  
**A:** Yes (Case-2). Both `ABC` **and** an abstract method are required to block instantiation.

**Q4. Child does not override the abstract method. What happens?**  
**A:** The child is also abstract. The `class` line is fine. Creating the child object raises `TypeError`.

**Q5. What is an interface in Python?**  
**A:** There is no `interface` keyword. An abstract class with **only** abstract methods is the interface. Example: `DBInterface` with `connect` / `disconnect`; `MySQL` and `Postgres` implement it.

**Q6. When interface, when abstract class, when concrete class?**  
**A:** Interface = we know only the requirement. Abstract class = partial implementation. Concrete class = complete implementation, ready to create objects.

**Q7. Why not put** `pay` **on** `Account`**?**  
**A:** Not every account pays a merchant. `Payable` is a separate requirement. Wallet opts in; savings does not fake `pay`.

**Q8. Can an abstract class contain normal methods?**  
**A:** Yes. That is the difference from an interface. `deposit` / `print_slip` on `Account` are normal; only `kind()` is abstract.

**Q9.** `ABC` **vs** `Protocol`**?**  
**A:** `ABC` — inherit the contract; missing methods fail at construction. `Protocol` — structural (“if it has `pay`, it counts”); mainly for type checkers. Labs use `ABC`.

**Q10. Why give an abstract class** `__init__`**?**  
**A:** Children still need holder and opening balance. `__init__` runs through `super()` when we construct the child — never as `Account(...)`.

---



## Next

Finish the [Campus Wallet lab kit](../15_Lab_Assets/32_campus_wallet_abc/), then continue with **[Exception Handling](04_Exception_Handling.md)**.