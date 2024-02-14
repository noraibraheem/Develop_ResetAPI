CREATE TABLE employees 
(
	id INT PRIMARY KEY,
	name VARCHAR(255),
	age INT,
	hiring_date DATE NOT NULL
);

INSERT INTO employees 
VALUES
	(1,'Nora',23,'2024-02-15'),
	(2,'Ahmed',26,'2024-02-12'),
	(3,'Ali',23,'2024-02-10'),
	(4,'Wafaa',25,'2024-01-23'),
	(5,'Yehia',22,'2024-12-30');

use Employees;
SELECT * FROM employees;


