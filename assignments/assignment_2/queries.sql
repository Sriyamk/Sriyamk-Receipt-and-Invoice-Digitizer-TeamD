
-- ========================================
-- ASSIGNMENT 2: SQL Database Operations
-- ========================================

-- Create Table1: Books
CREATE TABLE BOOKS (
    empId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dept TEXT NOT NULL
);

-- Create Table2: Authors
CREATE TABLE AUTHORS (
    empId INTEGER,
    author_name TEXT NOT NULL,
    country TEXT
);

-- ------------------------------------

-- Inserting data

-- Insert books data
INSERT INTO BOOKS VALUES (0001, 'Dark Knight', 'Fantasy');
INSERT INTO BOOKS VALUES (0002, 'Steve Jobs', 'Biography');
INSERT INTO BOOKS VALUES (0003, 'The Monk who sold a Ferrari', 'non-fiction');
INSERT INTO BOOKS VALUES (0004, 'Harry Potter', 'Fantasy');
INSERT INTO BOOKS VALUES (0005, 'Becoming', 'Biography');

-- Insert authors data 
INSERT INTO AUTHORS VALUES (0001, 'Christopher Nolan', 'USA');
INSERT INTO AUTHORS VALUES (0002, 'Walter Isaacson', 'USA');
INSERT INTO AUTHORS VALUES (0003, 'Robin Sharma', 'Canada');
INSERT INTO AUTHORS VALUES (0004, 'J.K. Rowling', 'UK');

-- ------------------------------------

-- Test1: BASIC SELECT QUERIES

-- Show all books
SELECT * FROM BOOKS;

-- Show only Fantasy books (using WHERE clause)
SELECT * FROM BOOKS WHERE dept = 'Fantasy';

-- Show books sorted by name (using ORDER BY)
SELECT * FROM BOOKS ORDER BY name ASC;

-- ------------------------------------

-- Test2: INNER JOIN
-- ------------------------------------

-- INNER JOIN shows ONLY books that have authors in our AUTHORS table
SELECT B.empId, B.name, B.dept, A.author_name, A.country
FROM BOOKS B
INNER JOIN AUTHORS A
ON B.empId = A.empId;

-- ------------------------------------

-- Test3: LEFT JOIN

-- LEFT JOIN shows ALL books, even if they don't have an author
SELECT B.empId, B.name, B.dept, A.author_name, A.country
FROM BOOKS B
LEFT JOIN AUTHORS A
ON B.empId = A.empId;

-- ------------------------------------

-- Test4: RIGHT JOIN 

-- RIGHT JOIN shows all authors, even if their books aren't in BOOKS table
SELECT B.empId, B.name, B.dept, A.author_name, A.country
FROM BOOKS B
RIGHT JOIN AUTHORS A
ON B.empId = A.empId;

-- ------------------------------------

-- Test5: AGGREGATE FUNCTIONS

-- COUNT: How many books total?
SELECT COUNT(*) AS total_books FROM BOOKS;

-- MIN: What's the lowest book ID?
SELECT MIN(empId) AS lowest_id FROM BOOKS;

-- MAX: What's the highest book ID?
SELECT MAX(empId) AS highest_id FROM BOOKS;

-- ------------------------------------

-- Test6: GROUP BY

-- Count how many books in each department
SELECT dept, COUNT(*) AS books_count
FROM BOOKS
GROUP BY dept;

-- ------------------------------------

-- Test7: GROUP BY with HAVING (filters groups)

-- Show only departments with MORE than 1 book
SELECT dept, COUNT(*) AS books_count
FROM BOOKS
GROUP BY dept
HAVING COUNT(*) > 1;

-- ------------------------------------

-- Test8: COMBINED QUERY (Shows multiple concepts together)

-- Find departments with multiple books and show author countries
SELECT B.dept, COUNT(*) AS book_count, GROUP_CONCAT(A.country) AS countries
FROM BOOKS B
LEFT JOIN AUTHORS A ON B.empId = A.empId
GROUP BY B.dept
HAVING COUNT(*) > 1;

-- ------------------------------------

-- Test9: OPERATORS
-- ------------------------------------

-- Books from USA or UK authors
SELECT B.name, A.author_name, A.country
FROM BOOKS B
INNER JOIN AUTHORS A ON B.empId = A.empId
WHERE A.country IN ('USA', 'UK');

-- Books with names starting with 'The' (LIKE operator)
SELECT * FROM BOOKS WHERE name LIKE 'The%';

-- Books with IDs between 2 and 4 (BETWEEN operator)
SELECT * FROM BOOKS WHERE empId BETWEEN 2 AND 4;


-- ========================================
-- ONCEPTS DEMONSTRATED:
-- ========================================
-- CREATE TABLE (2 tables)
-- INSERT data
-- SELECT with WHERE
-- ORDER BY
-- INNER JOIN
-- LEFT JOIN
-- RIGHT JOIN
-- Aggregate functions (COUNT, MIN, MAX)
-- GROUP BY
-- HAVING
-- Operators (IN, LIKE, BETWEEN)
-- ========================================