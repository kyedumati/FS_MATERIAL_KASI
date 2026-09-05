# Named Product Domains — Teaching Bible

**Purpose:** Soft overlay so Java FS, Python FS, Frontend, and MySQL examples feel like the same four companies. Canonical schemas and sample people live in [`MYSQL/12_Real_Time_Projects.md`](../../MYSQL/12_Real_Time_Projects.md).

**Do not share this file with learners.** Point them at module notes and MYSQL projects.

CampusCart remains the **default capstone** (college storefront). Teaching examples may say: *CampusCart uses the same patterns as Swiggy (orders, cart, menu/catalog).*

---

## Soft-apply rule

Use a named product **when the example already models a business object** (employee, product, order, account, appointment, leave, salary, cart, GST bill).

Keep the example **generic or campus** when it only proves syntax (hello world, loop patterns, git hygiene, terminal workspace, casting, a 5-line `print`).

- Do **not** demo all four products in every topic. Pick the closest one. Rotate across a module so learners meet all four over a phase.
- Do **not** rename `15_Lab_Assets/` folders. Update lab README tickets / print text only when the domain already matches.
- Do **not** add Discussion Questions, Use Cases tables, Trainer Tips, or Demo Plans. Real-time discussion = `**Where used?**`, Purpose stories, program titles, Interview Q&A, mini-project tickets.
- Library JDBC may stay. Optional second story: Employee Management Portal employee CRUD.

---

## The four products

| Product | Domain | Core entities | Sample people / flavor |
|---------|--------|---------------|------------------------|
| **Employee Management Portal** | Employee management | `department`, `employee`, `leave_record` | Arun Kumar, Priya Shah, Ravi Menon, Sneha Rao, Kiran Das; Bangalore / Mumbai / Delhi |
| **Swiggy** | Food delivery | `customer`, `address`, `product` (menu item), `cart`, `cart_product`, `orders`, `order_item` | Restaurants / dishes; INR prices |
| **Apollo Hospitals** | Hospital | `doctor`, `patient`, `appointment`, `prescription` | Status: `scheduled` / `completed` / `cancelled` |
| **HDFC Bank** / **PhonePe** | Banking / UPI | `customer`, `account`, `transaction_log`, `loan` | HDFC Bank: savings/current, ATM, deposit / withdrawal / transfer. PhonePe: UPI / wallet pay |

MYSQL Project 3A / 3B: student picks **one** database. In Java/Python notes, use **whichever domain fits the concept** (ATM → HDFC Bank; UPI → PhonePe; appointment status → Apollo Hospitals).

---

## Concept → product (pick the closest)

| Concept family | Product |
|----------------|---------|
| Inheritance, salary, manager, leave, payroll, staff hierarchy | **Employee Management Portal** |
| Catalog, cart, GST/price, REST product list, React list, CSS product card | **Swiggy** (CampusCart = college skin) |
| Enums/status, dates, doctor/patient, booking | **Apollo Hospitals** |
| Balance, ATM menu, transfer, `CHECK (balance >= 0)`, BankAccount | **HDFC Bank** |
| UPI, wallet pay | **PhonePe** |
| Marks arrays, string trim, hello `javac`/`python`, git ignore, terminal | **Do not force** |

---

## Do-not-force examples

**Force (business-shaped):**

- `**Where used?**` Employee Management Portal — leave days per employee (JOIN `employee` to `leave_record`).
- Program title: **Program 1 — HDFC Bank savings deposit**.
- Mini-project ticket: Swiggy GST bill (canteen calculator kit folder name stays).

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
- Employee Management Portal — `manager_id` self-join (employee reports to employee)
- Swiggy — order total from `order_item` quantity × unit price
- Apollo Hospitals — appointment `status` enum (scheduled / completed / cancelled)
- HDFC Bank — transfer with `START TRANSACTION` then `COMMIT` / `ROLLBACK`
```

---

## Lab tickets (folder names stay)

| Kit theme | Product in ticket copy |
|-----------|------------------------|
| Canteen / GST calculator, inventory, catalog REST | **Swiggy** |
| ATM menu, BankAccount, campus wallet | **HDFC Bank** |
| UPI / wallet pay | **PhonePe** |
| Employee / staff inheritance | **Employee Management Portal** |
| Appointments / status / dates | **Apollo Hospitals** |
| Library JDBC, hello, git, terminal, marks | Keep as-is (optional Employee Management Portal CRUD stretch) |
