SELECT MAX(balance),account_number
FROM account join
account_history on idaccount = account_id
group by account_number
