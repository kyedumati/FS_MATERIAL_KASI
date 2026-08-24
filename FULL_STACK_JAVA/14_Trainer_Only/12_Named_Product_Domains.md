# Named Product Domains — Teaching Bible

**Purpose:** Soft overlay so Java FS, Python FS, Frontend, and MySQL examples feel like the same four companies. Canonical schemas and sample people live in [`MYSQL/12_Real_Time_Projects.md`](../../MYSQL/12_Real_Time_Projects.md).

**Do not share this file with learners.** Point them at module notes and MYSQL projects.

CampusCart remains the **default capstone** (college storefront). Teaching examples may say: *CampusCart uses the same patterns as TechMart.*

---

## Soft-apply rule

Use a named product **when the example already models a business object** (employee, product, order, account, appointment, leave, salary, cart, GST bill).

Keep the example **generic or campus** when it only proves syntax (hello world, loop patterns, git hygiene, terminal workspace, casting, a 5-line `print`).

- Do **not** demo all four products in every topic. Pick the closest one. Rotate across a module so learners meet all four over a phase.
- Do **not** rename `15_Lab_Assets/` folders. Update lab README tickets / print text only when the domain already matches.
- Do **not** add Discussion Questions, Use Cases tables, Trainer Tips, or Demo Plans. Real-time discussion = `**Where used?**`, Purpose stories, program titles, Interview Q&A, mini-project tickets.
- Library JDBC may stay. Optional second story: AcmeHR employee CRUD.

---

## The four products

| Product | Domain | Core entities | Sample people / flavor |
|---------|--------|---------------|------------------------|
| **AcmeHR** | Employee management | `department`, `employee`, `leave_record` | Arun Kumar, Priya Shah, Ravi Menon, Sneha Rao, Kiran Das; Bangalore / Mumbai / Delhi |
| **TechMart** | E-commerce | `customer`, `address`, `product`, `cart`, `cart_product`, `orders`, `order_item` | Electronics / clothing / food; INR prices |
| **MedCare** | Hospital | `doctor`, `patient`, `appointment`, `prescription` | Status: `scheduled` / `completed` / `cancelled` |
| **SecureBank** | Banking | `customer`, `account`, `transaction_log`, `loan` | Savings/current; deposit / withdrawal / transfer; INR |

MYSQL Project 3A / 3B: student picks **one** database. In Java/Python notes, use **whichever domain fits the concept** (ATM → SecureBank; appointment status → MedCare).

---

## Concept → product (pick the closest)

| Concept family | Product |
|----------------|---------|
| Inheritance, salary, manager, leave, payroll, staff hierarchy | **AcmeHR** |
| Catalog, cart, GST/price, REST product list, React list, CSS product card | **TechMart** (CampusCart = college skin) |
| Enums/status, dates, doctor/patient, booking | **MedCare** |
| Balance, ATM menu, transfer, `CHECK (balance >= 0)`, BankAccount, wallet | **SecureBank** |
| Marks arrays, string trim, hello `javac`/`python`, git ignore, terminal | **Do not force** |

---

## Do-not-force examples

**Force (business-shaped):**

- `**Where used?**` AcmeHR — leave days per employee (JOIN `employee` to `leave_record`).
- Program title: **Program 1 — SecureBank savings deposit**.
- Mini-project ticket: TechMart GST bill (canteen calculator kit folder name stays).

**Do not force (syntax-only):**

- HelloJava / first `print("Priya")`.
- Star patterns and nested loops.
- Casting `double` marks to `int`.
- `.gitignore` hygiene.

---

## `Where used?` shape

Name the product, not only the industry (3–5 bullets):

```markdown
**Where used?**
- AcmeHR — `manager_id` self-join (employee reports to employee)
- TechMart — order total from `order_item` quantity × unit price
- MedCare — appointment `status` enum (scheduled / completed / cancelled)
- SecureBank — transfer with `START TRANSACTION` then `COMMIT` / `ROLLBACK`
```

---

## Lab tickets (folder names stay)

| Kit theme | Product in ticket copy |
|-----------|------------------------|
| Canteen / GST calculator, inventory, catalog REST | **TechMart** |
| ATM menu, BankAccount, campus wallet | **SecureBank** |
| Employee / staff inheritance | **AcmeHR** |
| Appointments / status / dates | **MedCare** |
| Library JDBC, hello, git, terminal, marks | Keep as-is (optional AcmeHR CRUD stretch) |
