UPDATE service_connection_and_disconnection_history
SET Date_of_disconnection = '$user_date',  status = '0'
WHERE idService_connection_and_disconnection_history = '$id'