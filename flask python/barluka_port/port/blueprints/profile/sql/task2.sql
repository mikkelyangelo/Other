SELECT *
FROM ShipsRegJournalRecord
WHERE (datediff(current_date(), ship_arrived) <= '$diff');
