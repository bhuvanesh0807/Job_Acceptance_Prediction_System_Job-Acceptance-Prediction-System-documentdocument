CREATE DATABASE company_db;
USE company_db;
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    salary DECIMAL(10,2),
    department VARCHAR(100),
    hire_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO employees (name, age, salary, department, hire_date)
VALUES 
('Alice Johnson', 30, 65000.00, 'HR', '2022-01-15'),
('Bob Smith', 40, 85000.00, 'IT', '2021-03-10');

SELECT * FROM employees;

SELECT COUNT(*) FROM employees;

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

SELECT * FROM employees
WHERE hire_date > '2022-01-01';

