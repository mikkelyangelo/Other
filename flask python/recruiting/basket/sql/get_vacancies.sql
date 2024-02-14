SELECT
    idvacancy,
    vacancy_name,
    description
FROM
    vacancy
WHERE
    vacancy_closing_date IS NULL