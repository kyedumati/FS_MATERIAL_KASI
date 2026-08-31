USE training_db;

SELECT m.full_name, b.title, l.due_date
FROM loans l
INNER JOIN members m ON m.member_id = l.member_id
INNER JOIN books b ON b.book_id = l.book_id
ORDER BY l.due_date;

SELECT m.full_name, m.email
FROM members m
LEFT JOIN loans l ON l.member_id = m.member_id
WHERE l.loan_id IS NULL;
