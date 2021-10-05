# Write your MySQL query statement below



select e2.Name AS Employee
from Employee e1
join Employee e2 on e1.id = e2.ManagerId
where e1.Salary < e2.Salary
    
