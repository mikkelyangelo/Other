select `T_ID`, `ROW`, `SIT`, `PRICE`
from ticket
WHERE T_ID = '$id'
AND (T_ID, ticket.ROW, SIT, PRICE) NOT IN (
    SELECT idtemp_table,temp_table.row,seat,price
    FROM temp_table
);