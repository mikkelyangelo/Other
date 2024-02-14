SELECT employee.employee_id, name, COUNT(employee.employee_id) as 'interview_count'
FROM employee, interview
WHERE interview.employee_id = employee.employee_id AND
      YEAR(interview.date) = '$year' AND
      MONTH(interview.date) = '$month'
GROUP BY employee.employee_id;
