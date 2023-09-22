DROP VIEW otlichniki;

CREATE VIEW otlichniki as 
SELECT name,COUNT(mark)
FROM journal
WHERE mark = 5
GROUP by name
HAVING COUNT(mark) > 2;

SELECT journal.name, COUNT(mark)
FROM journal
JOIN otlichniki ON
otlichniki.name = journal.name
GROUP BY journal.name, mark
HAVING journal.mark = 2;
