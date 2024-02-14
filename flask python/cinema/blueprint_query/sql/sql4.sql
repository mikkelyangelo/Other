SELECT HALL_ID, HALL_NAME, KOL_SITS
FROM hall left join session ON hall.HALL_ID = session.HALL
WHERE S_ID IS NULL;
