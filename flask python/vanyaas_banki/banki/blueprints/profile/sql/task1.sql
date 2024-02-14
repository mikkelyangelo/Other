SELECT COUNT(idclient) as number_of_clients, EXTRACT(MONTH FROM contract_date) as month
FROM client
WHERE YEAR(contract_date) = '$year' AND MONTH(contract_date) = '$month'
GROUP BY month
ORDER BY month;
