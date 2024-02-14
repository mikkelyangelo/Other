SELECT *
FROM employee
WHERE (datediff(current_date(), enrollment_date) <= '$days');