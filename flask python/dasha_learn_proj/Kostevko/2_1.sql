SELECT project.theme, student.last_name AS student_last_name, student.group_name, teacher.last_name AS teacher_last_name, defense_schedule.date_sh AS defense_date, defense_protocol.grade 
FROM project 
JOIN project_student ON project.id = project_student.project_id 
JOIN student ON student.id = project_student.student_id 
JOIN teacher ON teacher.id = project_student.teacher_id 
JOIN defense_schedule ON defense_schedule.commission_id = project.id 
JOIN defense_protocol ON defense_protocol.project_id = project.id 
WHERE YEAR(defense_schedule.date_sh) = 2020 AND MONTH(defense_schedule.date_sh) = 5;

