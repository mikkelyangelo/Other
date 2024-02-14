SELECT *
FROM client
WHERE (datediff(current_date(), contract_date) <= '$days');