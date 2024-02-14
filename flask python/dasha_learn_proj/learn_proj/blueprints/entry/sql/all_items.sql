select theme,student.id, student_card_number, student.last_name, group_name FROM project_student JOIN
project
ON project_id = project.id
JOIN teacher
ON teacher_id = teacher.id
JOIN student
ON student_id = student.id
where status = 0
  and theme='$theme'
AND (student.id, student_card_number, student.last_name, group_name, theme) NOT IN (
    SELECT idtemp_table, student_card, last_name, group_name, theme
    FROM temp_table
);