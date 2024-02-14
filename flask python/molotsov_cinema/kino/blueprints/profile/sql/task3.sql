SELECT session_hall, COUNT(*) AS total_sessions FROM session
WHERE YEAR(date_time)= '$year' AND MONTH(date_time)= '$month'
GROUP BY session_hall