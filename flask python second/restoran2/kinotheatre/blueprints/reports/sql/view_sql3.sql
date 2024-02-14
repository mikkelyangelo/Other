SELECT month, year, sum, count, non_sold
FROM viruchka_report

WHERE month = '$month' AND year = '$year'