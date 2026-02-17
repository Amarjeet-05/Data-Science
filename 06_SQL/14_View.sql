-- A View in MySQL is like a virtual table. It doesn’t store data by itself but instead shows data from one or more tables through a saved SQL query.

-- we can use a view just like a regular table: SELECT from it, filter it, join it, etc.

-- Why Use Views?
-- To simplify complex queries by giving them a name.
-- To hide sensitive columns from users.
-- To show only specific rows/columns from a table.
-- To reuse common query logic across your app or reports.




-- Creating a view
CREATE VIEW data as SELECT name, age FROM std_data;
SELECT * FROM data;

-- we can perform operations on vuew table that cannot affect the parent table. but if the parent table will update then the view also update

-- updating view table
CREATE OR REPLACE VIEW data as SELECT name, age FROM std_data WHERE age>20;
SELECT * FROM data;


-- Dropping (Deleting) a View
DROP VIEW data;