SELECT Internet_Service_Provider.Client.* FROM Internet_Service_Provider.Client
LEFT JOIN Internet_Service_Provider.Balance_history ON Internet_Service_Provider.Client.idClient = Internet_Service_Provider.Balance_history.IDClient
WHERE Internet_Service_Provider.Balance_history.idBalance_history IS NULL