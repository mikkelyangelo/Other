select service.idService, service.Name, Cost_per_day from service_connection_and_disconnection_history
join service on
service_connection_and_disconnection_history.idService = service.idService
where  service.idService = '$id'