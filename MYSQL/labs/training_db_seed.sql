-- Sample rows for MYSQL homework (modules 03+).
-- Does not create player or employee — those are module 02 CREATE TABLE drills.
-- Re-run is safe: only the tables listed below are dropped and rebuilt.

CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS product_order;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS student_course;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS movie_actor;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS player_match_details;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS product;
SET FOREIGN_KEY_CHECKS = 1;

-- Chapter 03 / 08 / 11 — catalogue drills
CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    brand VARCHAR(50),
    rating DECIMAL(3, 1)
);

INSERT INTO product (name, category, price, brand, rating) VALUES
('Chocolate cake', 'Food', 25.00, 'Britannia', 3.7),
('Strawberry cake', 'Food', 60.00, 'Cadbury', 4.1),
('Chocolate cake', 'Food', 60.00, 'Cadbury', 2.5),
('Blue shirt', 'clothing', 750.00, 'Denim', 3.8),
('Blue Jeans', 'clothing', 200.00, 'puma', 3.6),
('Black jeans', 'clothing', 750.00, 'Denim', 4.5),
('iPhone', 'Gadgets', 70000.00, 'Apple', 4.8),
('USB cable', 'Gadgets', 199.00, NULL, 3.2),
('Running shoes', 'clothing', 899.00, 'puma', 4.2),
('Protein bar', 'Food', 120.00, 'Muscle', 4.3),
('Laptop sleeve', 'Gadgets', 450.00, 'puma', 4.0),
('Fruit cake', 'Food', 40.00, 'Local', 4.6);

-- Chapter 08 — products with no order (NOT EXISTS)
CREATE TABLE product_order (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product (id)
);

INSERT INTO product_order (product_id) VALUES (1), (2), (4), (7), (9);

-- Chapter 04 — aggregations (18 matches; Ram totals 221; one NULL score)
CREATE TABLE player_match_details (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    score INT,
    year INT NOT NULL
);

INSERT INTO player_match_details (name, score, year) VALUES
('Ram', 80, 2010),
('Ram', 75, 2011),
('Ram', 66, 2012),
('Virat', 62, 2011),
('Virat', 51, 2010),
('Virat', 45, 2012),
('Rohit', 62, 2011),
('Rohit', 70, 2011),
('Rohit', 30, 2012),
('Dhoni', 40, 2010),
('Dhoni', 63, 2011),
('Dhoni', NULL, 2012),
('KL', 12, 2010),
('KL', 64, 2011),
('KL', 8, 2012),
('Rahul', 90, 2010),
('Rahul', 65, 2011),
('Rahul', 22, 2012);

-- Chapter 05 — expressions, dates, set ops
CREATE TABLE movie (
    id INT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    genre VARCHAR(50),
    budget_in_cr DECIMAL(8, 2),
    collection_in_cr DECIMAL(8, 2),
    rating DECIMAL(3, 1),
    release_date DATE
);

INSERT INTO movie (id, name, genre, budget_in_cr, collection_in_cr, rating, release_date) VALUES
(1, 'The Matrix', 'Sci-fi', 6.30, 46.61, 8.7, '1999-03-31'),
(2, 'Inception', 'Action', 16.00, 83.68, 8.8, '2010-07-14'),
(3, 'The Dark Knight', 'Action', 18.00, 100.50, 9.0, '2008-07-16'),
(4, 'Toy Story 3', 'Animation', 20.00, 106.70, 8.5, '2010-06-25'),
(5, 'Interstellar', 'Sci-fi', 16.50, 67.70, 8.6, '2014-11-07'),
(6, 'The Avengers', 'Action', 22.00, 151.80, 8.0, '2012-05-04'),
(7, 'Coco', 'Animation', 17.50, 80.70, 8.4, '2017-11-22'),
(15, 'Avengers Endgame', 'Action', 35.60, 279.80, 8.4, '2019-04-26');

CREATE TABLE movie_actor (
    movie_id INT NOT NULL,
    actor_id INT NOT NULL,
    PRIMARY KEY (movie_id, actor_id)
);

INSERT INTO movie_actor (movie_id, actor_id) VALUES
(6, 1), (6, 2), (6, 3),
(15, 2), (15, 3), (15, 4);

-- Chapter 07 — e-learning joins
CREATE TABLE instructor (
    instructor_id INT PRIMARY KEY,
    instructor_full_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(100) NOT NULL
);

INSERT INTO instructor (instructor_id, instructor_full_name, full_name) VALUES
(1, 'Alex', 'Alex'),
(2, 'Ann', 'Ann'),
(102, 'Arun', 'Arun');

CREATE TABLE course (
    id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    instructor_id INT NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES instructor (instructor_id)
);

INSERT INTO course (id, course_name, name, instructor_id) VALUES
(11, 'Machine Learning', 'machine learning', 102),
(15, 'Cyber Security', 'Cyber Security', 1),
(20, 'Data Analysis', 'Data Analysis', 2);

CREATE TABLE student (
    id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL
);

INSERT INTO student (id, full_name) VALUES
(1, 'Varun'),
(2, 'Ajay'),
(3, 'Sandya'),
(4, 'Afrin');

CREATE TABLE student_course (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score INT,
    FOREIGN KEY (student_id) REFERENCES student (id),
    FOREIGN KEY (course_id) REFERENCES course (id)
);

INSERT INTO student_course (student_id, course_id, score) VALUES
(1, 11, 90),
(3, 11, 85),
(2, 15, 88),
(1, 15, 70);

CREATE TABLE review (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    content VARCHAR(255) NOT NULL,
    created_at DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student (id),
    FOREIGN KEY (course_id) REFERENCES course (id)
);

INSERT INTO review (student_id, course_id, content, created_at) VALUES
(2, 15, 'Good explanation', '2021-01-19'),
(2, 15, 'cyber security is awesome', '2021-01-20');

-- Chapter 09 — transfers
CREATE TABLE accounts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL
);

INSERT INTO accounts (name, balance) VALUES
('Sam', 2000.00),
('David', 1500.00);
