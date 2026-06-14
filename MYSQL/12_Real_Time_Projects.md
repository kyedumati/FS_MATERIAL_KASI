# Real-Time Projects

Three end-to-end database projects for hands-on practice. Each project includes schema design, sample data, and query tasks. Use **MySQL 8+** and **MySQL Workbench**.

**Setup:** Create a separate database for each project.

```sql
CREATE DATABASE acmehr;
CREATE DATABASE techmart;
CREATE DATABASE medcare;   -- Hospital project
-- or
CREATE DATABASE securebank; -- Banking project
```

---

## Project 1: AcmeHR — Employee Management System

### Overview

AcmeHR manages employees, departments, salaries, and leave records for a mid-size company.

### Schema Design

**ER Relationships:**

| Relationship | Type |
|--------------|------|
| Department → Employee | 1:N |
| Employee → Leave | 1:N |
| Employee → Manager (self) | 1:N |

### CREATE TABLES

```sql
USE acmehr;

CREATE TABLE department (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100) DEFAULT 'Bangalore'
);

CREATE TABLE employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    department_id INT NOT NULL,
    manager_id INT NULL,
    salary DECIMAL(12,2) NOT NULL CHECK (salary > 0),
    hire_date DATE NOT NULL DEFAULT (CURDATE()),
    status ENUM('active', 'inactive') DEFAULT 'active',
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (manager_id) REFERENCES employee(id)
);

CREATE TABLE leave_record (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT NOT NULL,
    leave_type ENUM('sick', 'casual', 'annual') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    days INT GENERATED ALWAYS AS (DATEDIFF(end_date, start_date) + 1) STORED,
    FOREIGN KEY (employee_id) REFERENCES employee(id) ON DELETE CASCADE
);
```

### Sample Data

```sql
INSERT INTO department (name, location) VALUES
('Engineering', 'Bangalore'),
('HR', 'Mumbai'),
('Sales', 'Delhi');

INSERT INTO employee (name, email, department_id, manager_id, salary, hire_date) VALUES
('Arun Kumar', 'arun@acme.com', 1, NULL, 120000, '2020-01-15'),
('Priya Shah', 'priya@acme.com', 1, 1, 90000, '2021-06-01'),
('Ravi Menon', 'ravi@acme.com', 1, 1, 85000, '2022-03-10'),
('Sneha Rao', 'sneha@acme.com', 2, NULL, 75000, '2019-08-20'),
('Kiran Das', 'kiran@acme.com', 3, NULL, 80000, '2021-11-05');

INSERT INTO leave_record (employee_id, leave_type, start_date, end_date) VALUES
(2, 'casual', '2024-01-10', '2024-01-12'),
(2, 'sick', '2024-03-05', '2024-03-06'),
(3, 'annual', '2024-06-01', '2024-06-05');
```

### Practice Queries

1. List all employees with their department name (INNER JOIN).
2. Find employees who earn more than their department's average salary.
3. Count employees per department.
4. Find employees with no manager (top-level managers).
5. List employees and their manager's name (SELF JOIN).
6. Get total leave days per employee in 2024.
7. **Challenge:** Use `ROW_NUMBER()` to rank employees by salary within each department.

---

## Project 2: TechMart — E-Commerce Database

### Overview

TechMart is an online store selling electronics, clothing, and food. Builds on the e-commerce model from [Modeling Databases](06_Modeling_Databases.md).

### Schema Design

**ER Relationships:**

| Relationship | Type |
|--------------|------|
| Customer → Cart | 1:1 |
| Customer → Address | 1:N |
| Cart → Product | M:N (via cart_product) |
| Customer → Order | 1:N |
| Order → Order Item | 1:N |

### CREATE TABLES

```sql
USE techmart;

CREATE TABLE customer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL UNIQUE,
    phone VARCHAR(15),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE address (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    pin_code VARCHAR(10),
    city VARCHAR(100),
    is_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    brand VARCHAR(100),
    rating DECIMAL(3,1) DEFAULT 0,
    stock INT DEFAULT 0
);

CREATE TABLE cart (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL UNIQUE,
    total_price DECIMAL(12,2) DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE cart_product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1 CHECK (quantity > 0),
    FOREIGN KEY (cart_id) REFERENCES cart(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    total_amount DECIMAL(12,2),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE order_item (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id)
);
```

### Sample Data

```sql
INSERT INTO customer (name, email, phone) VALUES
('Ajay Reddy', 'ajay@email.com', '9876543210'),
('Meera Nair', 'meera@email.com', '9876543211');

INSERT INTO product (name, category, price, brand, rating, stock) VALUES
('Smart Watch', 'Gadgets', 17000, 'Apple', 4.9, 50),
('Blue Shirt', 'clothing', 750, 'Denim', 3.8, 200),
('Chocolate Cake', 'Food', 25, 'Britannia', 3.7, 100),
('Smart TV', 'Gadgets', 40000, 'Sony', 4.0, 30);

INSERT INTO cart (customer_id, total_price) VALUES (1, 17750);
INSERT INTO cart_product (cart_id, product_id, quantity) VALUES (1, 1, 1), (1, 2, 1);

INSERT INTO orders (customer_id, status, total_amount) VALUES (1, 'delivered', 17750);
INSERT INTO order_item (order_id, product_id, quantity, unit_price) VALUES (1, 1, 1, 17000), (1, 2, 1, 750);
```

### Practice Queries

1. List all products with price above the average price (subquery).
2. Get each customer's cart contents with product names (JOIN).
3. Find customers who have never placed an order (LEFT JOIN + IS NULL).
4. Get total revenue per product category.
5. Find the best-selling product by quantity sold.
6. Create a view `order_summary` showing order id, customer name, and total amount.
7. **Challenge:** Use a CTE to find customers who spent more than the average order value.

---

## Project 3A: MedCare — Hospital Management System

### Overview

MedCare manages patients, doctors, appointments, and prescriptions.

### CREATE TABLES

```sql
USE medcare;

CREATE TABLE doctor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    specialization VARCHAR(100),
    phone VARCHAR(15) UNIQUE
);

CREATE TABLE patient (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    age INT CHECK (age > 0),
    gender ENUM('M', 'F', 'Other'),
    phone VARCHAR(15),
    blood_group VARCHAR(5)
);

CREATE TABLE appointment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
    fee DECIMAL(10,2) DEFAULT 500,
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(id)
);

CREATE TABLE prescription (
    id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    medicine VARCHAR(200) NOT NULL,
    dosage VARCHAR(100),
    duration_days INT DEFAULT 7,
    FOREIGN KEY (appointment_id) REFERENCES appointment(id) ON DELETE CASCADE
);
```

### Practice Queries

1. List all appointments with patient and doctor names.
2. Count appointments per doctor.
3. Find doctors with no appointments (LEFT JOIN).
4. Get patients who have visited more than once.
5. Calculate total revenue per doctor from completed appointments.
6. **Challenge:** Use `DENSE_RANK()` to rank doctors by number of appointments.

---

## Project 3B: SecureBank — Banking System

### Overview

SecureBank manages accounts, transactions, and loans. Use this as an alternative to MedCare.

### CREATE TABLES

```sql
USE securebank;

CREATE TABLE customer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) UNIQUE,
    phone VARCHAR(15),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE account (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    account_type ENUM('savings', 'current') DEFAULT 'savings',
    balance DECIMAL(15,2) NOT NULL DEFAULT 0 CHECK (balance >= 0),
    opened_date DATE DEFAULT (CURDATE()),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE transaction_log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    from_account_id INT,
    to_account_id INT,
    amount DECIMAL(15,2) NOT NULL CHECK (amount > 0),
    transaction_type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account_id) REFERENCES account(id),
    FOREIGN KEY (to_account_id) REFERENCES account(id)
);

CREATE TABLE loan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    interest_rate DECIMAL(5,2) NOT NULL,
    start_date DATE NOT NULL,
    tenure_months INT NOT NULL,
    status ENUM('active', 'closed', 'defaulted') DEFAULT 'active',
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);
```

### Practice Queries

1. List all accounts with customer names and balances.
2. Write a transaction to transfer ₹5,000 between two accounts using `START TRANSACTION`, `COMMIT`, and `ROLLBACK`.
3. Use `SAVEPOINT` to demonstrate partial rollback during a transfer.
4. Find customers with total balance across all accounts greater than ₹1,00,000.
5. Get transaction history for a specific account.
6. Count active loans per customer.
7. **Challenge:** Create an index on `transaction_log(transaction_date)` and explain why it helps.

---

## Project Completion Checklist

| Task | AcmeHR | TechMart | MedCare / SecureBank |
|------|--------|----------|----------------------|
| Create database | ☐ | ☐ | ☐ |
| Run CREATE TABLE scripts | ☐ | ☐ | ☐ |
| Insert sample data | ☐ | ☐ | ☐ |
| Complete all practice queries | ☐ | ☐ | ☐ |
| Complete challenge query | ☐ | ☐ | ☐ |
| Create at least one VIEW | ☐ | ☐ | ☐ |
| Use a transaction with COMMIT/ROLLBACK | ☐ | ☐ | ☐ |
| Add an index and verify with EXPLAIN | ☐ | ☐ | ☐ |

**Note:** Run `EXPLAIN SELECT ...` before and after creating an index to see the performance difference.
