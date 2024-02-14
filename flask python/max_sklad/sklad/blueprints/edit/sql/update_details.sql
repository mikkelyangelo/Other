UPDATE details
SET amount = amount + '$count_tovar', Fix_Date = '$user_date'
WHERE (SELECT Product_id FROM product WHERE Product_name = '$tovar_name') = details.Product_id