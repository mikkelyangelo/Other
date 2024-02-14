SELECT Surname_Pt, Name_P, Patronymic_P, Passport, Birthday, Diagnosis, Date_of_admission, Date_of_discharge, Surname_D, Name_D, Patronymic_D, adress, ID_Ward
FROM medicalcard join doctor using(ID_Doctor)
WHERE (datediff(current_date(), date_of_discharge) <= '$days');