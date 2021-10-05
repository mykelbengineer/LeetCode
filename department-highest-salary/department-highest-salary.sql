# Write your MySQL query statement below


select d.Name as 'Department', e.Name as 'Employee', e.Salary 
from Employee e
join Department d on e.DepartmentId = d.Id
where (e.DepartmentId, e.Salary) IN (
select DepartmentId, max(Salary)
from Employee
group by DepartmentId )

