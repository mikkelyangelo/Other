SELECT Specialization, Surname_D, Name_D, Patronymic_D, Passport_D, Adress_D, Birthday_D, Date_of_admission_to_work, Date_of_dismissal, ID_Department, Worktime, ID_Service
FROM doctor
WHERE (year(Date_of_admission_to_work) = '$year' and month(Date_of_admission_to_work)='$month');