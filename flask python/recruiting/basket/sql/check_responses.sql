SELECT
    vacancy_id,
    vacancy_name,
    status
FROM
    responses
    JOIN vacancy ON(idvacancy = vacancy_id)
WHERE
    username = '$username'