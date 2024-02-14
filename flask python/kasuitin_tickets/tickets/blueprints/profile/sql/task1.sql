SELECT *
FROM ticket
WHERE YEAR(purchase_date) = '$year' AND MONTH(purchase_date) = '$month';
