Select ID_Department, NAME_Department, typeWard, count(TypeWard)
FROM department
JOIN ward
using(ID_Department)
WHERE NAME_Department = '$title'
Group BY ID_department, TypeWard;