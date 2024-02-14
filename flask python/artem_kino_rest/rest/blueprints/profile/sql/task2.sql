SELECT passport,appldate,Birthday,name,surname
FROM waiter
WHERE YEAR(appldate)= '$year' AND MONTH(appldate)= '$month'
