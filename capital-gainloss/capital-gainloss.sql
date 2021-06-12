/* Write your T-SQL query statement below */

SELECT stock_name, 
'capital_gain_loss' = SUM(CASE WHEN stk.operation = 'Buy' THEN price * -1  ELSE price  END)
FROM Stocks stk
GROUP BY stock_name
