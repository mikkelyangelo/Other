SELECT TIME_FORMAT(time, "%H:%i") as time, IF(schedule.card_id is null, 'нет записи', CONCAT(patient.surname, ' ', patient.name, ' ', patient.patronymic)) AS schedule
FROM work_hours JOIN doctor
	ON work_hours.doc_id = doctor.doc_id
		LEFT JOIN schedule
			ON work_hours.date = schedule.visit_date AND work_hours.time = schedule.visit_time
				LEFT JOIN patient
					ON schedule.card_id = patient.card_id
WHERE CONCAT(doctor.surname, ' ', doctor.name, ' ', doctor.patronymic) = "$snp" AND work_hours.date = "$date"