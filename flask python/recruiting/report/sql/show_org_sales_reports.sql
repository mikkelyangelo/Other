SELECT
    rep_year,
    rep_month,
    customer.name as customer,
    detail_type.code as code,
    detail_type.name as name,
    price as price,
    invoice_detail.quantity as amount
FROM
    reports_sales_org
    JOIN invoice USING(invoice_id)
    JOIN invoice_detail USING(invoice_id)
    JOIN detail_type USING(detail_type_id)
    JOIN customer USING(customer_id)
WHERE
    rep_year = YEAR('$date-01')
    AND rep_month = MONTH('$date-01')
ORDER BY
    customer.name