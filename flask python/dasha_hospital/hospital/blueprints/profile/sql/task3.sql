Select TypeWard
FROM department
INNER JOIN ward
ON department.ID_department = ward.ID_department
WHERE NAME_Department = '$title'