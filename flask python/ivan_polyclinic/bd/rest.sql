create table order_lines(
	record_id INT AUTO_INCREMENT,
    order_id INT,
    dish_id INT,
    dishes_count INT,
    PRIMARY KEY (record_id)
);