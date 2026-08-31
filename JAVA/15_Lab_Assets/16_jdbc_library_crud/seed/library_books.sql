-- Campus library seed for JDBC kit 16.
-- MySQL 8+ (see MYSQL/00). PK/FK ideas: MYSQL/06. Do not treat this file as a SQL textbook.
--
-- Workbench: open and execute.
-- CLI: mysql -u root -p < library_books.sql

CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;

DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(120) NOT NULL,
    author VARCHAR(80) NOT NULL,
    copies INT NOT NULL,
    price_inr DECIMAL(10, 2) NOT NULL
);

INSERT INTO books (title, author, copies, price_inr) VALUES
    ('The White Tiger', 'Aravind Adiga', 3, 399.00),
    ('The Guide', 'R. K. Narayan', 2, 299.00),
    ('Malgudi Days', 'R. K. Narayan', 5, 249.00),
    ('Five Point Someone', 'Chetan Bhagat', 4, 199.00),
    ('The Palace of Illusions', 'Chitra Banerjee Divakaruni', 2, 450.00),
    ('Interpreter of Maladies', 'Jhumpa Lahiri', 3, 350.00);

-- Stretch only (JOIN). Core path CRUD uses books.
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(80) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE
);

INSERT INTO members (full_name, email) VALUES
    ('Priya Rao', 'priya@campus.edu'),
    ('Ravi Kumar', 'ravi@campus.edu');

CREATE TABLE loans (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    loan_date DATE NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO loans (member_id, book_id, loan_date) VALUES
    (1, 1, '2026-08-01'),
    (2, 4, '2026-08-10');

SELECT book_id, title, author, copies, price_inr FROM books ORDER BY book_id;
