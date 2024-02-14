SELECT visit.visit_date as vis_date, complaints, diagnosis, prescriptions
FROM visit JOIN schedule
ON visit.appointment_id = schedule.appointment_id
JOIN patient
ON patient.card_id = schedule.card_id
WHERE CONCAT(surname, ' ', name, ' ', patronymic) = "$snp" and diagnosis is not NULL