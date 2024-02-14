SELECT *
FROM seans
WHERE (datediff(current_date(), seans.date) <= '$days');