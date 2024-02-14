SELECT Seller_name, City_of_Seller,  Number_of_Seller
FROM seller_contract
WHERE YEAR(Contract_Date) =  '$year' and month(Contract_Date) = '$month'