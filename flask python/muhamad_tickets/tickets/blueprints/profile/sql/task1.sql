SELECT *
FROM tickets
WHERE YEAR(purchase_date) = '$year' AND MONTH(purchase_date) = '$month';
