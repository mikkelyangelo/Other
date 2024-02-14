SELECT  * FROM session
WHERE (datediff(current_date(), date_time) <= '$days')
GROUP BY session_id

