SELECT  DishCol, Date, Price FROM orders
WHERE (datediff(current_date(), Date) <= '$days')

