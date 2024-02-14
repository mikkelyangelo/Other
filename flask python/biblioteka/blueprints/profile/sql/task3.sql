select count(name_izd) as Cnt
FROM izdatel
WHERE address = '$city'
group by address
