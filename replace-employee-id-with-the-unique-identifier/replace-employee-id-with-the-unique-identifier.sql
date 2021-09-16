/* Write your T-SQL query statement below */

SELECT case when eu.unique_id = null then null else eu.unique_id end unique_id, e.name
from Employees e
left join EmployeeUNI eu on e.id = eu.id