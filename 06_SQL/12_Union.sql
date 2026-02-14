SELECT stu_id, stu_name FROM student
UNION
SELECT class_id, class_name FROM class;


-- UNION operator is used to combine the result sets of two or more SELECT statements into a single result.

-- By default, UNION removes duplicate rows. If you want to keep duplicates, use UNION ALL:

-- When UNION Works
-- Same number of columns in all SELECT statements.
-- Compatible data types in corresponding columns.
-- Columns will be matched by position, not by name.



-- When UNION Doesn't Work
-- If the number of columns is different
-- If the data types don’t match

