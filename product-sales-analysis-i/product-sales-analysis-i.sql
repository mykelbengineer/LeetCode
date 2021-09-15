/* Write your T-SQL query statement below */

SELECT P.product_name, S.year, S.price
FROM Sales S
LEFT join Product P on P.product_id = S.product_id