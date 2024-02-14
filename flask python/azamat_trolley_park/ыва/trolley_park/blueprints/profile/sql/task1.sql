SELECT Full_name,
FROM Drivers
WHERE MONTH(Hire_date) = '$month' and YEAR(Hire_date) = '$year';