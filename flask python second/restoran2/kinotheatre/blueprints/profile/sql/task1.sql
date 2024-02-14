SELECT seans.time, seans.date, zal.name, film.nazvanie, director, film.year
FROM seans
JOIN zal ON zal_ID_zala = ID_zala
JOIN film ON film_ID_filma = ID_filma
WHERE seans.date BETWEEN '$date1' AND '$date2'
-- GROUP BY employee.employee_id;
