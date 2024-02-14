SELECT
Internet_Service_Provider.Client.idClient,
CONCAT(Internet_Service_Provider.Client.Passport_data, ' и ', Internet_Service_Provider.Client.Contacts) AS client_info,
SUM(IF(MONTH(Internet_Service_Provider.Balance_history.Replenishment_date) = 1, Internet_Service_Provider.Balance_history.Balance_before_payment, 0) +
IF(MONTH(Internet_Service_Provider.Balance_history.Payment_date) = 1, Internet_Service_Provider.Balance_history.Balance_after_payment, 0)) AS total_replenishments_january
FROM Internet_Service_Provider.Client
LEFT JOIN Internet_Service_Provider.Balance_history ON Internet_Service_Provider.Client.idClient = Internet_Service_Provider.Balance_history.IDClient
WHERE Internet_Service_Provider.Client.idClient BETWEEN '$start' AND '$finish' AND YEAR(Internet_Service_Provider.Balance_history.Replenishment_date) = 2020
GROUP BY Internet_Service_Provider.Client.idClient;