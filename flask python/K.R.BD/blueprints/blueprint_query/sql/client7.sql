SELECT IDClient, COUNT(idBalance_history) AS Number_of_Balance_Changes
FROM Internet_Service_Provider.Balance_history WHERE Payment_date BETWEEN '2020-03-01' AND '2020-03-31' GROUP BY IDClient