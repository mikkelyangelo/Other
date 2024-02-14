SELECT *
FROM doctor
WHERE (year(Date_of_admission_to_work) = '$year' and month(Date_of_admission_to_work)='$month');