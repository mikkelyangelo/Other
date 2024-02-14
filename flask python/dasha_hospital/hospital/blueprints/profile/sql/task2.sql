SELECT *
FROM medicalcard
WHERE (datediff(current_date(), date_of_discharge) <= '$days');