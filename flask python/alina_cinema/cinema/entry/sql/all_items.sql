select `T_ID`, `ROW`, `SIT`, `PRICE`
from ticket
WHERE SESSION_ID='$id' and MARK = 'FREE'
AND (`T_ID`, `ROW`, `SIT`, `PRICE`) NOT IN (
    SELECT idtemp_table,temp_table.row,seat,price
    FROM temp_table
);