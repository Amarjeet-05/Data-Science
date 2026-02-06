CREATE TABLE student_data (id INT AUTO_INCREMENT PRIMARY KEY, 
							name VARCHAR(30) NOT NULL DEFAULT "NO NAME",
                            age INT,
                            email VARCHAR(50) UNIQUE,
                            admission_date DATE);



SELECT * FROM student_data;

-- syntax for creating table
-- CREATE TABLE table_name (column1 datatype constrants, column2 datatype constrants,...);
-- constrants are not null, primary key, default etc.



-- for viewing  tables:
-- SHOW tables;

-- for viewing table structure:
-- DESCRIBE student_data;  

-- for viewing the table data
-- SELECT * FROM table_name;


-- Data Types:
-- INT – Whole numbers (e.g., age, quantity)
-- VARCHAR(n) – Variable-length string (e.g., names, emails)
-- TEXT – Long text strings (e.g., descriptions)
-- DATE – Stores date values (YYYY-MM-DD)
-- DATETIME – Stores date and time values
-- BOOLEAN – Stores TRUE or FALSE



-- Common Constraints
-- PRIMARY KEY – Uniquely identifies each record
-- NOT NULL – Ensures the column cannot be left empty
-- UNIQUE – Ensures all values in a column are different
-- AUTO_INCREMENT – Automatically increases numeric values
-- DEFAULT – Sets a default value for the column
-- FOREIGN KEY – Enforces relationships between tables (connecting one table to another)



