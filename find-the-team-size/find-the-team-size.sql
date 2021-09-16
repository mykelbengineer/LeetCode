/* Write your T-SQL query statement below */
SELECT employee_id, count(team_id) over(partition by team_id) as 'team_size'
from Employee