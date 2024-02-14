SELECT TIME_FORMAT(time, "%H:%i") as time
FROM work_hours JOIN doctor
ON work_hours.doc_id = doctor.doc_id
WHERE CONCAT(surname, ' ', name, ' ', patronymic) = "$snp" AND date = "$date" AND taken = 0