SELECT commission_id, COUNT(*) as schedule_entries
FROM defense_schedule
WHERE YEAR(date_sh) = 2013 AND MONTH(date_sh) = 3
GROUP BY commission_id;
