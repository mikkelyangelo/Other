select  max(ticket.row) as max_row, max(seat) as max_seat
from ticket
WHERE seans_ID_seansa='$id'
group by seans_ID_seansa