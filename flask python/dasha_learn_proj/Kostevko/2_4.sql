SELECT teacher.*
FROM teacher
LEFT JOIN project_student ON teacher.id = project_student.teacher_id
WHERE project_student.teacher_id IS NULL;
