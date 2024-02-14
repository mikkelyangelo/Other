SELECT *
FROM tickets
WHERE (datediff(current_date(), purchase_date) <= '$days');
