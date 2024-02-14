SELECT distinct *
FROM report
WHERE months = '$month' AND years = '$year'



SELECT count(theme) as cnt
from report
WHERE months = '$month' AND years = '$year'
group by theme