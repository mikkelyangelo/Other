SELECT client.idclient, COUNT(account.idaccount) as number_of_accounts
FROM client
JOIN account  ON client.idclient = account.client_id
WHERE client.last_name ='$client'
GROUP BY client.idclient
ORDER BY client.idclient;
