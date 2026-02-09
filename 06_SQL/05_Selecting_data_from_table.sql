-- DESCRIBE std_data;

-- Filtering 
SELECT * FROM std_data WHERE age > 20;  -- * means all

-- if want specific columns
SELECT name, age, result FROM std_data WHERE age > 19 and age != 21;


-- we can use all comparision operators in filtering 

-- some more operators are
-- BETWEEN	         Within a range (inclusive)	                 WHERE age BETWEEN 15 AND 17
-- IN				 Matches any in a list						 WHERE grade IN ('10th', '12th')
-- NOT IN			 Excludes list items						 WHERE grade NOT IN ('9th', '11th')
-- LIKE				 Pattern matching							 WHERE name LIKE 'A%' (names starting with A)
-- NOT LIKE			 Pattern not matching						 WHERE name NOT LIKE '%a' (names not ending in a)


-- NAME STARTS WITH AND WITH 
SELECT * FROM std_data WHERE name LIKE "A%";     -- "a%" means name starts with a.    "%a" means name ends with a.
SELECT * FROM std_data WHERE name LIKE "%n";

SELECT * FROM std_data WHERE name NOT LIKE "Am%";
SELECT * FROM std_data WHERE name NOT LIKE "%an";

-- WE CAN COMPARE MULTIPLE CONDITIONS
SELECT * FROM std_data WHERE (age BETWEEN 16 AND 22) AND age != 21;



-- Correct Ways to Handle NULL
-- Condition				Correct Syntax
-- Is NULL					WHERE grade IS NULL
-- Is NOT NULL				WHERE grade IS NOT NULL 



-- SORTING 

SELECT * FROM std_data ORDER BY age DESC;  -- descending
SELECT name, age FROM std_data ORDER BY age ASC; -- ascending

-- LIMIT (NO. OF ROWS)
SELECT * FROM std_data LIMIT 2; -- SHOW FIRST 2 ROWS
SELECT * FROM std_data LIMIT 2,3; -- SHOWS 3 ROWS AFTER THE 2ND ROW 