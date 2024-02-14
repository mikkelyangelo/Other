SELECT
    vacancy_id,
    vacancy_name,
    candidate_name,
    username,
    status
FROM
    responses
    JOIN vacancy ON(vacancy_id = idvacancy)
    JOIN candidate USING(username)