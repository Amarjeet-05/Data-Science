-- A subquery is a query nested inside another SQL query.
-- It helps you perform complex filtering, calculations, or temporary data shaping by breaking down the logic into smaller steps.
-- You can use subqueries in SELECT, FROM, or WHERE clauses.



-- SELECT * FROM employees;

-- Subquery in the WHERE Clause
-- SELECT AVG(salary) FROM employees WHERE department = "Marketing";     -- 50000

-- EMPLOYEE WHO EARN MORE THAN AVERGAE
SELECT name, department, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);  




-- Correlated Subqueries
-- Departmentwise employee who earn more than average

SELECT name, department, salary FROM employees e
WHERE SALARY >= (SELECT AVG(salary) FROM employees WHERE department = e.department);

-- in this case here e refers to the employee table or records. 






-- SELECT name
-- FROM employees
-- WHERE dept_id IN (
--     SELECT dept_id
--     FROM departments
--     WHERE status = 'active'
-- );


-- = → one value
-- IN → multiple values



