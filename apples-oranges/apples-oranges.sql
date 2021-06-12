/* Write your T-SQL query statement below */


SELECT s1.sale_date, (s1.sold_num - s2.sold_num) as diff
FROM Sales s1
INNER JOIN Sales s2 ON s1.fruit = 'apples' AND s2.fruit = 'oranges' AND s1.sale_date = s2.sale_date
ORDER BY sale_date
