SELECT division_code, SUM(salary)
FROM employee, staffing
WHERE employee.job_id = staffing.job_id and division_code = '$title'
GROUP BY division_code
ORDER BY division_code;
