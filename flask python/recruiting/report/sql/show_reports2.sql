SELECT *
FROM
    recruiting.reports2
WHERE
    rep_year = YEAR('$date-01')
    AND rep_month = MONTH('$date-01')