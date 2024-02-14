select `ID_ticket`, `row`, `seat`, `price`
from ticket where ID_ticket = '$id'
AND (`ID_ticket`, `row`, `seat`, `price`) NOT IN (
    SELECT ID_temple, row_t, seat_t, price_t
    FROM temp_table
);