SELECT flights.flight_number, SUM(tickets.actual_price) AS total_price
FROM tickets
INNER JOIN departure ON tickets.departure = departure.id_departure
INNER JOIN flights ON departure.flight_number = flights.flight_number
WHERE YEAR(tickets.purchase_date) = '$year'
GROUP BY flights.flight_number;