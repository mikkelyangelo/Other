SELECT Seller_name,City_of_Seller, SUM(S_Count * Price) as Count_sum
FROM sklad.supply_product
JOIN product ON supply_product.product_id = product.Product_id
JOIN supply ON supply_product.supply_id = supply.Supply_id
JOIN seller_contract ON supply.seller_id = seller_contract.seller_id
WHERE year(S_Date) ='$year' and month(S_Date) = '$month'
GROUP BY Seller_name,City_of_Seller