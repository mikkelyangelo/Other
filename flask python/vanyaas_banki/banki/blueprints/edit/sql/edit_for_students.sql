UPDATE account
SET balance = balance - '$sum'
WHERE idaccount = '$card_id';

