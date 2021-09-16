/* Write your T-SQL query statement below */
SELECT s.id, s.name 
from Students s
left join Departments d on d.id = s.department_id
where s.department_id not in 
(select id from Departments)