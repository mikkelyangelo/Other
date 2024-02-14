SELECT
    employee_name,
    employee_birthday,
    employee_address,
    employee_education,
    employee_salary,
    employee_date_of_enrollm
FROM
    employee
WHERE
    employee_date_of_dismissal IS NULL
    AND employee_name LIKE '%$name%';