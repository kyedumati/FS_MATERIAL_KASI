# BROKEN — intentional SQL mistakes for debug lab
-- Run seed first, then fix these queries.

-- Bug 1: Cartesian product (missing ON)
SELECT m.name, b.title, l.due_date
FROM members m, loans l, books b;

-- Bug 2: INNER JOIN that hides members with no loans (OK for report A)
-- but learner often uses wrong FK column names — fix to match seed schema.
SELECT m.name, b.title, l.due_date
FROM members m
INNER JOIN loans l ON m.id = l.member_id_WRONG
INNER JOIN books b ON b.id = l.book_id;

-- Bug 3: LEFT JOIN missing IS NULL filter for "no loans"
SELECT m.name
FROM members m
LEFT JOIN loans l ON m.id = l.member_id;
