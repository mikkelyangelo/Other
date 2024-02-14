SELECT Seller_name, City_of_Seller, Contract_Date, Number_of_Seller
FROM seller_contract
WHERE Number_of_Seller LIKE '$prefix%'