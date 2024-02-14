SELECT *
FROM izdatel
WHERE (datediff(current_date(), date_of_start_contract) <= '$days');