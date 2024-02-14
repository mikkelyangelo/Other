SELECT count(Seller_id), year(Contract_Date), month(Contract_Date)
FROM seller_contract
WHERE year(Contract_Date) = '$year' and month(Contract_Date)='$month'
GROUP BY year(Contract_Date), month(Contract_Date)