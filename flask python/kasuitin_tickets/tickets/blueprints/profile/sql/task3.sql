SELECT id_Passenger_balance, COUNT(*) FROM balance
WHERE balance.before < balance.after AND YEAR(balance.date) = '$year'
GROUP BY id_Passenger_balance;