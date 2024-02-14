SELECT distinct driver.fio,address,trail_name
from order_list join driver
on id_driver = driver.id
join trail on
id_trail = trail.id
join orders on orders.id_order = order_list.order_id
where year(user_date) = '$year' and month(user_date) = '$month'