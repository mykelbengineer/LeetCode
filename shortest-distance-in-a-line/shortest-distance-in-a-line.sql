/* Write your T-SQL query statement below */

SELECT  min(abs(a.x - b.x))  AS 'shortest'
from point a 
inner join point b on a.x != b.x

