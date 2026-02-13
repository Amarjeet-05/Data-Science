-- CREATE DATABASE school;

-- USE school;


CREATE TABLE class(class_id INT AUTO_INCREMENT PRIMARY KEY, class_name varchar(20));

CREATE TABLE student(stu_id INT AUTO_INCREMENT PRIMARY KEY, stu_name VARCHAR(20) NOT NULL, stu_class_id INT, 
					FOREIGN KEY (stu_class_id) REFERENCES class(class_id)
                    ON DELETE SET NULL
                     ON UPDATE CASCADE);


-- -- ON DELETE SET NULL: If a class is deleted, the related students will have class_id set to NULL.
-- -- ON UPDATE CASCADE: If a class ID changes, it will update automatically in the students table.




 INSERT INTO class(class_name) VALUES ('Mathematics'), ('Science'), ('History');

 INSERT INTO student (stu_name, stu_class_id) VALUES 
('Alice', 1),
('Bob', 2),
('Charlie', 1);


-- SELECT * FROM student;
-- SELECT * FROM class;

DELETE FROM CLASS WHERE class_id = 2;

SELECT * FROM student;

                    