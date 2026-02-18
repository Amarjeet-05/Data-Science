-- An index in MySQL is a data structure that makes data retrieval faster—especially when you're using WHERE, JOIN, ORDER BY, or searching large tables.
-- Why Use Indexes?
-- Speed up queries that search, filter, or sort data.
-- Improve performance for frequent lookups or joins.
-- Enhance scalability of your database over time.


-- Use indexes when:

-- A column is often used in WHERE, JOIN, or ORDER BY clauses.
-- You're searching by unique fields like email, username, or ID.
-- You're filtering large tables for specific values regularly.
-- You want to improve performance of lookups and joins.


-- Avoid adding indexes when:

-- The table is small (MySQL can scan it quickly anyway).
-- The column is rarely used in searches or filtering.
-- You're indexing a column with very few unique values (like a gender field with just 'M' and 'F').
-- You’re inserting or updating very frequently—indexes can slow down writes because they also need to be updated.


-- creating index
CREATE INDEX name_ends ON std_data(name);

-- now whenever we use name column from std_data it make retrival fast

SELECT * FROM std_data WHERE name LIKE "%n";

-- Multi column(composite) index
CREATE INDEX name_age ON std_data(name, age);


-- how to delete index
DROP INDEX name_age ON std_data;


-- viewing existing indexs
SHOW INDEX FROM std_data;


