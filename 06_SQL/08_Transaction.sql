-- A transaction is a sequence of one or more SQL statements that are executed as a single unit. A transaction has four key properties, known as ACID:

-- Atomicity: All or nothing.
-- Consistency: Valid state before and after.
-- Isolation: Transactions do not interfere.
-- Durability: Changes persist after commit.




-- COMMIT IS LIKE DOING FINAL THING IF THE CODE WILL EXECUTES THEN IT PERMENANTLY CHANGE THE DATA IN DATABASE AND AFTER THAT WE CAN NOT CHANGE THEM OR UNDO THAT.
-- check autocommit status
-- SELECT @@autocommit;       -- if it shows 1 means it is enable. By default, MySQL runs in autocommit mode 

-- DISABLE AUTOCOMMIT
-- SET autocommit = 0;    -- it will disable auto commit.

-- for enable autocommit
-- SET autocommit = 1;


-- After disable commit if we do mistake in any condition which are going to apply on data then we can undo/rollback that, untill unless we commit it. 
-- UPDATE std_data SET age = age+1 WHERE age > 21;
-- SELECT * FROM std_data;
-- ROLLBACK;
-- SELECT * FROM std_data;
-- now after rollback it the age which increament by 1 no rollback. if we commit that then rollback will not work so thats why we disable autocommit to use rollback function.



-- how can we commit manually
-- START TRANSACTION;
-- UPDATE std_data SET age = age-1;
-- COMMIT;
-- NOW AFTER THIS COMMIT WE CANNOT ROLLBACK.
SELECT * FROM std_data;

