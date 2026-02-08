-- RENAME TABLE student_data TO  std_data;

-- RENAME COLUMN 
ALTER TABLE std_data RENAME COLUMN admission_date to adm_date;

-- ADDING NEW COLUMN
ALTER TABLE std_data ADD COLUMN result VARCHAR(10) NOT NULL;
ALTER TABLE std_data ADD COLUMN gender VARCHAR(10) NOT NULL;


-- MODIFYING COLUMN. (To change the data type or constraints of an existing column) 
ALTER TABLE std_data MODIFY COLUMN result VARCHAR(5) DEFAULT "AWAIT";


-- Changing the Order of Columns
-- To change the order of columns in a table, you can use the MODIFY command with the AFTER keyword
ALTER TABLE std_data MODIFY COLUMN adm_date DATE AFTER result;
-- ALTER TABLE table_name MODIFY COLUMN column_name datatype AFTER another_column_name;


-- dropping column
ALTER TABLE std_data DROP COLUMN gender; 
