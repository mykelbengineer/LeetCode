/* Write your T-SQL query statement below */

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE SALARY < (SELECT MAX(Salary) from Employee)
        