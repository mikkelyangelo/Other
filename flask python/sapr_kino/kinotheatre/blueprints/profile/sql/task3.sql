SELECT distinct  ID_seansa, ratio * seats_number * price as mult, seans.date
FROM seans JOIN zal
ON ID_zala = zal_ID_zala
join zal_shema
on id_zala = zal_shema.zal_ID_zala
WHERE year(seans.date) = '$year' and month(seans.date)='$month'

