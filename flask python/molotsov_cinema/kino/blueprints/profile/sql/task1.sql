SELECT * FROM session
WHERE YEAR(date_time)= '$year' AND MONTH(date_time)= '$month'
GROUP BY session_id
