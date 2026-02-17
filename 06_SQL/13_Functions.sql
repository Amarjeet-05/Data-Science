-- CREATE TABLE students (id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50));


-- INSERT INTO students (id, first_name, last_name) VALUES
-- (1, 'Rohan', 'Kumar'),
-- (2, 'Aakash', 'Tiwari'),
-- (3, 'Priya', 'Sain'),
-- (4, 'Sneha', 'Negi'),
-- (5, 'Rahul', 'Gupta'),
-- (6, 'Anjali', 'Agrwal'),
-- (7, 'Vikram', 'Roy'),
-- (8, 'Simran', 'Ahuja'),
-- (9, 'Karan', 'Aujla'),
-- (10, 'Neha','Gupta');


SELECT CONCAT(first_name, " ", last_name) as name FROM students;

SELECT first_name, last_name, CONCAT(first_name, " ", last_name) as name FROM students;

SELECT first_name, length(first_name) as length FROM students;



-- INSERT INTO std_data(adm_date) VALUES ('2009-01-05'), ('2009-01-05'), ('2009-03-05'), ('2010-06-03'), ('2011-12-07'), ('2010-11-08'), ('2012-01-05'), ('2019-01-05'),('2020-01-05');

-- DATEDIFF() – Difference between two dates (in days)

SELECT DATEDIFF(Now(), adm_date) as days FROM std_data;    -- gives how many many days from admission date to now.

SELECT DATEDIFF(NOW(), adm_date)/365 as years FROM std_data; -- no. of years from admission date to now

SELECT ROUND(DATEDIFF(NOW(), adm_date)/365, 1) as years FROM std_data;

SELECT MAX(age) as max_age FROM std_data;
SELECT MIN(age) FROM std_data;

SELECT REPLACE("Aman", "n", "r");














-- Comprehensive List of Useful MySQL Functions

-- Function						Description								Example Usage
-- CONCAT()				Combine multiple strings					CONCAT('A', 'B') → 'AB'
-- LENGTH()				Length of a string (in bytes)				LENGTH('Hi') → 2
-- CHAR_LENGTH()		Number of characters in a string			CHAR_LENGTH('हिंदी') → 5
-- LOWER()				Convert string to lowercase					LOWER('MySQL') → mysql
-- UPPER()				Convert string to uppercase					UPPER('hello') → HELLO
-- REPLACE()			Replace part of a string					REPLACE('abc', 'b', 'x') → axc
-- TRIM()				Remove leading/trailing spaces				TRIM('  hello  ') → hello
-- NOW()				Current date and time						NOW()
-- CURDATE()			Current date only							CURDATE()
-- CURTIME()			Current time only							CURTIME()
-- DATE()				Extract date from datetime					DATE(NOW())
-- MONTHNAME()			Get month name from date					MONTHNAME('2025-05-03') → May
-- YEAR()				Extract year from date						YEAR(NOW())
-- DAY()				Extract day of month						DAY('2025-05-03') → 3
-- DATEDIFF()			Days between two dates						DATEDIFF('2025-06-01', '2025-05-01')
-- ROUND()				Round to decimal places						ROUND(5.678, 2) → 5.68
-- FLOOR()				Round down to nearest whole number			FLOOR(5.9) → 5
-- CEIL()				Round up to nearest whole number			CEIL(5.1) → 6
-- ABS()				Absolute value								ABS(-10) → 10
-- MOD()				Get remainder								MOD(10, 3) → 1
-- RAND()				Random decimal between 0 and 1				RAND()
-- IFNULL()				Replace NULL with a default value	I		FNULL(NULL, 'N/A') → N/A
-- COALESCE()			Return first non-NULL value in a list		COALESCE(NULL, '', 'Hello') → ''
-- COUNT()				Count rows									COUNT(*)
-- AVG()				Average of a numeric column					AVG(score)
-- SUM()				Total sum of values							SUM(score)
-- MIN()				Smallest value								MIN(score)
-- MAX()				Largest value								MAX(score)