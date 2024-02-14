SELECT *
FROM Drivers
WHERE (datediff(current_date(), hire_date) <= '$days');