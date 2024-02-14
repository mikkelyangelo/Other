

SELECT t.seans_ID_seansa, s.date, zal.name, film.nazvanie, SUM(t.price) AS total_price
FROM ticket t
JOIN seans s ON t.seans_ID_seansa = s.ID_seansa JOIN zal ON s.zal_ID_zala=zal.ID_zala JOIN film ON film.ID_filma=s.film_ID_filma
WHERE t.status = 1  AND YEAR(s.date) = '$year' AND MONTH(s.date) = '$month'
GROUP BY t.seans_ID_seansa;