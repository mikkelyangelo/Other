SELECT project.*
FROM project
JOIN project_student ON project.id = project_student.project_id 
JOIN teacher ON teacher.id = project_student.teacher_id 
WHERE teacher.last_name = 'Иванова' AND YEAR(project.defense_date) = 2020;
