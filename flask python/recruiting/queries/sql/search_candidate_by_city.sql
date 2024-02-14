SELECT
    candidate_name,
    candidate_living_place,
    candidate_age,
    candidate_sex
FROM
    candidate
WHERE
    candidate_living_place LIKE '%$city%'