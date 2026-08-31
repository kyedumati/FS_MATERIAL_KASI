-- CampusCart catalog seed for JPA kit 18.
-- MySQL 8+ (see MYSQL/00). Same snack idea as module 02 / FS bridge products.
-- This table is campus_products so MYSQL homework `products` is not dropped.
--
-- Workbench: open and execute.
-- CLI: mysql -u root -p < campus_products.sql
--
-- If Boot already created the table (ddl-auto=update), the CREATE IF NOT EXISTS
-- is a no-op; INSERTs still load demo rows.

CREATE DATABASE IF NOT EXISTS training_db;
USE training_db;

CREATE TABLE IF NOT EXISTS campus_products (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(120) NOT NULL,
    price_inr INT NOT NULL
);

INSERT INTO campus_products (name, price_inr) VALUES
    ('Idli', 40),
    ('Filter coffee', 25),
    ('Masala dosa', 60);

SELECT id, name, price_inr FROM campus_products ORDER BY id;
