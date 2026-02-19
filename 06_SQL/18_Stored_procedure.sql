-- A Stored Procedure is a saved block of SQL code that you can execute later by calling its name.
-- It allows you to group SQL statements and reuse them—just like a function in programming.

-- Creating a Stored Procedure
-- When you create a stored procedure, you need to temporarily change the SQL statement delimiter from ; to something else like // or $$.

-- Why change the DELIMITER?
-- MySQL ends a command at the first ;.
-- Since stored procedures contain multiple SQL statements (each ending in ;), we need to tell MySQL not to end the procedure too early.
-- So we temporarily change the delimiter to something else—then switch it back


DELIMITER //
CREATE PROCEDURE emp_list()
BEGIN
	SELECT * FROM employees;
END // 
DELIMITER ; 

-- Calling a Stored Procedure
CALL emp_list();

-- Get details of an employee by ID
DELIMITER //
CREATE PROCEDURE get_emp_details(IN emp_id INT)
BEGIN
	SELECT * FROM employees WHERE id = emp_id;
END //
DELIMITER ;

CALL get_emp_details(2);


-- To delete a stored procedure
DROP PROCEDURE IF EXISTS emp_list;

