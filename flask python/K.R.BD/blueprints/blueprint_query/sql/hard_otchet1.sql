SELECT
  MONTH(Internet_Service_Provider.Service_connection_and_disconnection_history.Date_of_connection) AS Month,
  Internet_Service_Provider.Service.idService,
  Internet_Service_Provider.Service.Name,
  COUNT(IF(Internet_Service_Provider.Service_connection_and_disconnection_history.Date_of_connection IS NOT NULL, 1, NULL)) AS Connections,
  COUNT(IF(Internet_Service_Provider.Service_connection_and_disconnection_history.Date_of_disconnection IS NOT NULL, 1, NULL)) AS Disconnections
FROM
  Internet_Service_Provider.Service
  LEFT JOIN Internet_Service_Provider.Service_connection_and_disconnection_history ON Internet_Service_Provider.Service.idService = Internet_Service_Provider.Service_connection_and_disconnection_history.idService
WHERE
  YEAR(Internet_Service_Provider.Service_connection_and_disconnection_history.Date_of_connection) = 2020
GROUP BY
  Month,
  Internet_Service_Provider.Service.idService