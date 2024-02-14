SELECT t.last_name, t.employment_date, t.department_code, v.excellent_project_count
FROM teacher t
JOIN (
    SELECT teacher_id, excellent_project_count
    FROM teacher_excellent_project_count
    WHERE excellent_project_count = (
        SELECT MAX(excellent_project_count)
        FROM teacher_excellent_project_count
    )
) v ON v.teacher_id = t.id;