-- SHOW TABLES;
-- DESCRIBE std_data;


-- inserting 1 row in the table  
INSERT INTO std_data(name, age, email, result) VALUES("Amarjeet", 20, "asdhfjku@ads.com", "pass");


-- inserting multiple records.

INSERT INTO std_data(name, age, email, result) 
VALUES("Aman", 20, "asdhfsau@ads.com", "pass"),
("Anurag", 21, "iuerhdf@as.com", "pass"),
("Jishan", 19, "iasha@as.com", "fail"),
("Abhay", 20, "akjshdfu@adjsf", "await");



SELECT * FROM std_data;