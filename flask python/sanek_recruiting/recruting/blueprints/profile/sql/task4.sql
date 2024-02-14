SELECT job_name, user_date, user_id
FROM order_list JOIN
orders
    ON order_list.order_id = orders.order_id
JOIN staffing
    ON order_list.job_id = staffing.job_id
