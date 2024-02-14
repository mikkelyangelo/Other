SELECT
    candidate_name,
    candidate_living_place,
    candidate_age,
    candidate_sex,
    candidate_email
FROM
    candidate
WHERE
    username = '$username'