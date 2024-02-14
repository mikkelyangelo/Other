SELECT DISTINCT teacher.*
FROM teacher
LEFT JOIN project_student ON teacher.id = project_student.teacher_id
JOIN project 
WHERE project_student.teacher_id IS NULL OR (project_student.teacher_id IS NOT NULL AND YEAR(project.defense_date) != 2020);

