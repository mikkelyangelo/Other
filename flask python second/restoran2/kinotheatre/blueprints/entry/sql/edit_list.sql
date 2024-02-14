SELECT ID_seansa,date,director,studio, nazvanie, (zal.seats_number - temp.count_ID_ticket) as ostatok_biletov, zal.seats_number as bilety
FROM seans LEFT JOIN (SELECT seans_ID_seansa, COUNT(ID_ticket) AS count_ID_ticket
    FROM ticket
    WHERE status=1
    GROUP BY seans_ID_seansa) as temp ON seans.ID_seansa = temp.seans_ID_seansa
JOIN film
ON seans.film_ID_filma = film.ID_filma JOIN zal ON seans.zal_ID_zala = zal.ID_zala
WHERE date > CURDATE()