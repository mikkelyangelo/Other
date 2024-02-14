CREATE DEFINER=`root`@`localhost` PROCEDURE `new_visits`(date_visit DATE)
BEGIN
	DECLARE pv INTEGER;
    DECLARE done INTEGER DEFAULT 0;
    DECLARE doc, office, card INTEGER;
    DECLARE v_date DATE;
    DECLARE v_time DATETIME;
    DECLARE cr CURSOR FOR
		SELECT doc_id, office_number, visit_date, visit_time, card_id
        FROM schedule
        WHERE visit_date = date_visit;
	DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done = 1;
    
    SELECT COUNT(*) INTO pv FROM visit_table WHERE vis_date = date_visit;
    IF pv = 0 THEN
		OPEN cr;
        WHILE done = 0 DO
			FETCH cr INTO doc, office, v_date, v_time, card;
            DROP TABLE IF EXISTS visit_table;
            CREATE TABLE visit_table (`visit_id` INT auto_increment, `doc_id` INT, `office_num` INT, `vis_date` DATE, `vis_time` DATETIME, `card_id`INT, `diagnosis` VARCHAR(100), `complaints` VARCHAR(100), `prescriptions` VARCHAR(100));
            INSERT INTO visit_table(`visit_id`, `doc_id`, `office_num`, `vis_date`, `vis_time`, `card_id`, `diagnosis`, `complaints`, `prescriptions`)
            VALUES (NULL, doc, office, v_date, v_time, card, NULL, NULL, NULL);
		END WHILE;
        CLOSE cr;
    ELSE
		SELECT 'This table already exists';
	END IF;
END