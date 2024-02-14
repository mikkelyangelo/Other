SELECT * FROM Internet_Service_Provider.Client INNER JOIN Internet_Service_Provider.Contract ON Internet_Service_Provider.Client.Passport_data = Internet_Service_Provider.Contract.Passport_data
WHERE Date_of_conclusion_of_the_contract BETWEEN DATE_SUB(NOW(), INTERVAL 60 DAY) AND NOW()