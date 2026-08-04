-- Run inside training_db
CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;

DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
  member_id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(120) UNIQUE
);

CREATE TABLE books (
  book_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(150) NOT NULL,
  author VARCHAR(100)
);

CREATE TABLE loans (
  loan_id INT PRIMARY KEY AUTO_INCREMENT,
  member_id INT NOT NULL,
  book_id INT NOT NULL,
  due_date DATE NOT NULL,
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO members (full_name, email) VALUES
('Priya Sharma', 'priya@campus.in'),
('Rahul Verma', 'rahul@campus.in'),
('Asha Nair', 'asha@campus.in');

INSERT INTO books (title, author) VALUES
('Clean Code', 'Robert Martin'),
('Fluent Python', 'Luciano Ramalho'),
('Django for Beginners', 'William Vincent');

INSERT INTO loans (member_id, book_id, due_date) VALUES
(1, 1, '2026-08-15'),
(1, 2, '2026-08-20'),
(2, 3, '2026-08-18');
-- Asha has no loans on purpose
