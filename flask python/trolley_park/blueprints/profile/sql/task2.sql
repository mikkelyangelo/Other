SELECT *
FROM driver
WHERE (datediff(current_date(), date_acception) <= '$days');