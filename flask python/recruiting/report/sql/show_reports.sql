SELECT
    rep_year,
    rep_month,
    employee_name,
    employee_date_of_enrollm,
    COUNT(emp_id) as count
FROM
    recruiting.reports
    JOIN employee ON(emp_id = idemployee)
WHERE
    rep_year = YEAR('$date-01')
    AND rep_month = MONTH('$date-01')
GROUP BY
    emp_id