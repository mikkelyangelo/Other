SELECT order_list.order_id, user_date, order_list.id_seansa, ticket_id,user_id, film.nazvanie
FROM order_list join orders
ON orders.order_id = order_list.order_id JOIN seans ON seans.ID_seansa = order_list.id_seansa JOIN film ON film.ID_filma = seans.film_ID_filma
WHERE year(user_date) = '$year' and month(user_date) = '$month'