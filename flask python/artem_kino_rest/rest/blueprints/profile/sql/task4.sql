SELECT name,surname, sum(PRICE) FROM mydb.orders
join waiter on waiter_idwaiter = idwaiter
where year(orders.Date) = '$year' and month(orders.Date) = '$month'

group by waiter_idwaiter;
