select theme,student.id, student_card_number, student.last_name, group_name FROM project_student JOIN
project
ON project_id = project.id
JOIN teacher
ON teacher_id = teacher.id
JOIN student
ON student_id = student.id
where status = 0 and student.id !='$id'