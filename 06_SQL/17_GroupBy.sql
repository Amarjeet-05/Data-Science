-- The GROUP BY clause is used when you want to group rows that have the same values in specified columns.
-- It’s usually combined with aggregate functions like COUNT(), SUM(), AVG(), MAX(), or MIN().

-- Count of employees in each department
SELECT department, COUNT(*) AS total_emp FROM employees GROUP BY department;


-- HAVING is like WHERE, but it works after the grouping is done. if you are using WHER after grouping it gives error.
SELECT department, COUNT(*) AS tot_emp FROM employees GROUP BY department HAVING COUNT(*) > 2;
-- or
SELECT department, COUNT(*) AS tot_emp FROM employees GROUP BY department HAVING tot_emp > 2;


SELECT department, name, AVG(salary) AS avg_sal FROM employees GROUP BY department, name HAVING avg_sal > 50000;

-- IT GIVES THE SUM OF ALL THE DEPARTMENTWISE SALARY (WITH ROLLUP)
SELECT department, name, SUM(salary) AS tot_sal FROM employees GROUP BY department, name  WITH ROLLUP;
