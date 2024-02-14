SELECT department_code, COUNT(*) as associate_professors
FROM teacher
WHERE department_code IN (
  SELECT department_code
  FROM teacher
  WHERE title = 'Доцент'
)
GROUP BY department_code;