select ticket_num, price, purchase.row, seat, id_dep from departure
join purchase
ON id_departure=id_dep
where status = 0 and ticket_num = '$id'
AND (ticket_num, price, purchase.row, seat) NOT IN (
    SELECT idtemp_table, temp_table.row, seat, price
    FROM temp_table
);