SELECT
    rep_year,
    rep_month,
    code,
    name,
    material,
    detail_type.price as price,
    amount
FROM
    reports_sales
    JOIN orders_by_users USING(order_id)
    JOIN detail_type USING(code)
WHERE
    rep_year = YEAR('$date-01')
    AND rep_month = MONTH('$date-01')
GROUP BY
    username,
    detail_type_id,
    name,
    price,
    amount,
    date
ORDER BY
    amount DESC