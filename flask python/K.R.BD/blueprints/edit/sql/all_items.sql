select distinct service.idService, service.Name, Cost_per_day from service_connection_and_disconnection_history
join service on
service_connection_and_disconnection_history.idService = service.idService
WHERE  (service.idService, service.Name, Cost_per_day ) NOT IN (
    select service.idService, service.Name, Cost_per_day from service_connection_and_disconnection_history
join service on
service_connection_and_disconnection_history.idService = service.idService
where (IDclient_1 = '$id' and  Date_of_disconnection is  NULL)
)
-- where (IDclient_1 != '$id') or (IDclient_1 = '$id' and Date_of_disconnection is not NULL)
AND (service.idService, service.Name, Cost_per_day) NOT IN (
    SELECT idserv,sname,cost_d
    FROM temp_table
);