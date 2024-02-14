SELECT * FROM internal_users
WHERE login='$login' and password='$password'
UNION
SELECT * FROM external_users
WHERE login='$login' and password='$password'
