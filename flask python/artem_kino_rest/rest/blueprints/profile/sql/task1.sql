SELECT Date, max(Price) as pr
FROM orders
WHERE YEAR(Date)= '$year' AND MONTH(Date)= '$month'
GROUP BY Date
