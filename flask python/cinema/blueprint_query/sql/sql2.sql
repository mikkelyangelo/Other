SELECT S_ID, DATA, SUM(PRICE)
FROM session join ticket ON S_ID = ticket.SESSION_ID
WHERE MONTH(DATA) = '$month' AND YEAR(DATA) = '$year' AND MARK = 'SOLD'
GROUP BY SESSION_ID, DATA;
