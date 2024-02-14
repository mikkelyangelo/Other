select t_id, t_row, t_place,t_price
from ticket
WHERE ticket_session = '$id' and status = '0'