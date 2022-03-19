# Write your MySQL query statement below
#  https://leetcode.com/problems/exchange-seats/
SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)



select row_number() over() id,
student
from Seat
order by
CASE WHEN mod(id,2) != 0 THEN id + 1
WHEN mod(id,2) = 0 THEN id - 1
ELSE NULL END;
