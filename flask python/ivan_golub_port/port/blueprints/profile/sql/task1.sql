select id_r, date_of_arrival, date_of_leaving
from registration
where year(date_of_arrival) = '$year' and month(date_of_arrival) = '$month'
