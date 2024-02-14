select emp_id, emp_surname, emp_profession, emp_birthdate, emp_adress, emp_recruit_date
from employee WHERE emp_recruit_date
BETWEEN '$date1' AND '$date2';
