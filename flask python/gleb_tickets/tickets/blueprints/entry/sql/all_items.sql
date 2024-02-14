select ticket_num, price, purchase.row, seat, id_dep from departure
join purchase
ON id_departure=id_dep
where status = 0 and flight_number='$id'
AND (ticket_num, price, purchase.row, seat) NOT IN (
    SELECT idtemp_table, price, temp_table.row, seat
    FROM temp_table
);