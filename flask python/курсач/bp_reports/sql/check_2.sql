SELECT COUNT(*) AS count
FROM report_2
WHERE MONTH(date) = '$month' AND YEAR(date) = '$year'