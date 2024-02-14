SELECT *
FROM teacher
WHERE teacher.employment_date = (
  SELECT MIN(employment_date)
  FROM teacher
) AND employment_date <= NOW()
