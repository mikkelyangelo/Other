select `ID_ticket`, `row`, `seat`, `price`,`status`
from ticket
WHERE seans_ID_seansa='$id' and status = '0'
AND (`ID_ticket`, `row`, `seat`, `price`) NOT IN (
    SELECT ID_temple, row_t, seat_t, price_t
    FROM temp_table
);