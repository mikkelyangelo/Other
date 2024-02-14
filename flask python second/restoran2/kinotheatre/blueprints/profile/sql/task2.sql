



SELECT s.ID_seansa, s.date, zal.name, zal.seats_number, t.count_ID_ticket, s.ratio, film.nazvanie, film.director, film.duration
FROM (
    SELECT seans_ID_seansa, COUNT(ID_ticket) AS count_ID_ticket
    FROM ticket
    WHERE status=1
    GROUP BY seans_ID_seansa
) AS t
RIGHT JOIN seans s ON t.seans_ID_seansa = s.ID_seansa JOIN zal ON zal_ID_zala=ID_zala JOIN film ON film_ID_filma=ID_filma WHERE (datediff(current_date(), s.date) <= '$days')ORDER BY s.ID_seansa;