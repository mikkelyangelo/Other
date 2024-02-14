SELECT fio
FROM driver
WHERE MONTH(date_acception) = '$month' and YEAR(date_acception) = '$year';
