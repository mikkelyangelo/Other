SELECT *
FROM ticket
WHERE (datediff(current_date(), purchase_date) <= '$days');
