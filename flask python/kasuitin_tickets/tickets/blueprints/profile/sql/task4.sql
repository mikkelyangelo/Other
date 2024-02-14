SELECT id_flight, class, COUNT(*) FROM ticket
WHERE YEAR(purchase_date) = '$year' and month(purchase_date) = '$month'
GROUP BY id_flight, class;