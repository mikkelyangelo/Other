SELECT
    vacancy_name,
    vacancy_opening_date,
    description
FROM
    vacancy
WHERE
    vacancy_closing_date IS NULL
    AND vacancy_name LIKE '%$vacancy%'