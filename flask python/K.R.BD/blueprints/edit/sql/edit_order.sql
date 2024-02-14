UPDATE account
SET balance = balance + '$sum' * '$exchange_rate'
WHERE account_number = '$rek'
