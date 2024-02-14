SELECT group_name, MIN(birth_date) as youngest_student_birthdate
FROM student
GROUP BY group_name;
