SELECT
    interview_date,
    interview_result,
    employee_name,
    vacancy_name,
    candidate_name
FROM
    interview
    JOIN employee ON(idemployee = employee_idemployee)
    JOIN vacancy ON(idvacancy = vacancy_idvacancy)
    JOIN candidate ON(idcandidate = candidate_idcandidate)
WHERE
    MONTH(interview_date) = MONTH('$date-01')
    AND YEAR(interview_date) = YEAR('$date-01')