SELECT *
FROM teacher
WHERE YEAR(employment_date) = '$year' AND MONTH(employment_date) = '$month';
