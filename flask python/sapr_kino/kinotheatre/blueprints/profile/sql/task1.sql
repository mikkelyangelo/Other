SELECT seans.time,zal.name,seats_number, director, studio, country, film.year
FROM seans JOIN zal
ON zal_ID_zala = ID_zala
JOIN film ON
film_ID_filma = ID_filma
WHERE YEAR(seans.date) = '$year' AND
      MONTH(seans.date) = '$month'
-- GROUP BY employee.employee_id;
