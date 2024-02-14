select speciality,sum(number_of_hours), surnamee, birthday,date_of_employment
from tabel
join employee
ON employee_id_e = id_e
where YEAR(date_of_start_of_work) = '$year' AND month(date_of_start_of_work) = '$month'
group by employee_id_e
order by employee_id_e
