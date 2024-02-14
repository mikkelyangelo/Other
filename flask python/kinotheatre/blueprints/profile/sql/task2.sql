SELECT id_r, date_of_arrival, date_of_leaving
FROM registration
WHERE (datediff(current_date(), date_of_arrival) <= '$days');