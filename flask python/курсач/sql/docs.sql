SELECT CONCAT(doctor.surname, ' ', doctor.name,' ', doctor.patronymic) as snp, IF(floor is null, 0, 1) AS if_manager
FROM doctor LEFT JOIN department
ON doctor.surname = department.manager
WHERE specialization = "$specialization"