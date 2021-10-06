# Write your MySQL query statement below


select Name from Employee
where Id IN (

Select ManagerId from (
select ManagerId, count(ManagerId) as 'Count'
from Employee
Group by ManagerId ) A
Where Count >= 5 )

#where Count >= 5
