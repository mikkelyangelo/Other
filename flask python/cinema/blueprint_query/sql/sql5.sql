SELECT S_ID, DATA
FROM session left join ticket ON session.S_ID = ticket.SESSION_ID
WHERE YEAR(DATA) = '$year' AND T_ID IS NULL;
