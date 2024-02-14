UPDATE
    candidate
SET
    candidate_name = '$candidate_name',
    candidate_living_place = '$candidate_living_place',
    candidate_age = '$candidate_age',
    candidate_sex = '$candidate_sex',
    candidate_email = '$candidate_email'
WHERE
    username = '$username';