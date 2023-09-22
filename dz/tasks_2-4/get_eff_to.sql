SELECT *,
	CASE
	WHEN id_1 = LEAD(id_1,1) OVER(ORDER BY id_1, eff_from)
	THEN LEAD(eff_from,1,'5999-12-30') OVER(ORDER BY eff_from) + 1
	ELSE '5999-12-30'
	END eff_to
FROM prices
