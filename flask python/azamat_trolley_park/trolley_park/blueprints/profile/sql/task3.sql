SELECT bus.id, fio
FROM bus
join driver
ON b_driver_id = driver.id
WHERE name = '$title';
